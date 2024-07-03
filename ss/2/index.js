// Define variables
let pixelsData = [];
let selectedPixel = null;
let selectedData = null;

// Fetch data from blocks.json
fetch('blocks.json')
    .then(response => response.json())
    .then(data => {
        pixelsData = data;
        renderPixels(); // Render pixels initially
    })
    .catch(error => console.error('Error fetching blocks.json:', error));

// Render pixels on the page
function renderPixels() {
    document.getElementById('container').innerHTML = ''; // Clear previous pixels
    pixelsData.forEach(imageData => {
        createPixel(imageData);
    });
}

// Click event listener to hide edit form when clicking around
document.body.addEventListener('click', (event) => {
    // Check if clicked element is not the edit form or its children
    if (!event.target.closest('#edit-form') && selectedPixel) {
        hideEditForm();
    }
});

// Function to create a pixel
function createPixel(data) {
    const pixel = document.createElement('div');
    pixel.className = 'pixel';
    pixel.style.top = `${(data.y - 1) * 10}px`;
    pixel.style.left = `${(data.x - 1) * 10}px`;
    pixel.style.width = `${data.width * 10}px`;
    pixel.style.height = `${data.height * 10}px`;

    const img = document.createElement('img');
    img.src = data.imageUrl;
    img.alt = data.title;
    img.className = 'img1';
    pixel.appendChild(img);

    // Make pixel draggable
    pixel.draggable = true;
    pixel.addEventListener('dragstart', (event) => {
        event.dataTransfer.setData('text/plain', JSON.stringify(data));
        selectedPixel = pixel;
        selectedData = data;
    });

    pixel.addEventListener('dragend', (event) => {
        const rect = container.getBoundingClientRect();
        const newX = Math.round((event.clientX - rect.left) / 10);
        const newY = Math.round((event.clientY - rect.top) / 10);
        data.x = newX;
        data.y = newY;
        pixel.style.left = `${(newX - 1) * 10}px`;
        pixel.style.top = `${(newY - 1) * 10}px`;
    });

    pixel.addEventListener('click', (event) => {
        // Prevent click event from propagating to the body
        event.stopPropagation();

        selectedPixel = pixel;
        selectedData = data;
        showEditForm();
    });

    document.getElementById('container').appendChild(pixel);
}

// Arrow key movement
document.addEventListener('keydown', (event) => {
    if (selectedPixel && selectedData && ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
        event.preventDefault();
        let moved = false;
        switch (event.key) {
            case 'ArrowUp':
                if (selectedData.y > 1) {
                    selectedData.y--;
                    moved = true;
                }
                break;
            case 'ArrowDown':
                if (selectedData.y < 100) {
                    selectedData.y++;
                    moved = true;
                }
                break;
            case 'ArrowLeft':
                if (selectedData.x > 1) {
                    selectedData.x--;
                    moved = true;
                }
                break;
            case 'ArrowRight':
                if (selectedData.x < 100) {
                    selectedData.x++;
                    moved = true;
                }
                break;
        }
        if (moved) {
            selectedPixel.style.top = `${(selectedData.y - 1) * 10}px`;
            selectedPixel.style.left = `${(selectedData.x - 1) * 10}px`;
        }
    }
});

// Show edit form with current pixel data
function showEditForm() {
    const editForm = document.getElementById('edit-form');
    editForm.style.display = 'flex';
    document.getElementById('pixel-width').value = selectedData.width;
    document.getElementById('pixel-height').value = selectedData.height;
    document.getElementById('pixel-imageUrl').value = selectedData.imageUrl;
    document.getElementById('pixel-linkUrl').value = selectedData.linkUrl;
    document.getElementById('pixel-title').value = selectedData.title;
}

// Upload image using URL
document.getElementById('upload-btn').addEventListener('click', () => {
    const imageUrl = document.getElementById('upload-url').value.trim();
    if (imageUrl !== '') {
        const newPixel = {
            x: 1,
            y: 1,
            width: 5, // Default width
            height: 5, // Default height
            imageUrl: imageUrl,
            linkUrl: '',
            title: 'New Pixel'
        };
        pixelsData.push(newPixel);
        renderPixels(); // Render pixels with updated data
    } else {
        alert('Please enter a valid image URL.');
    }
});

// Download updated JSON
document.getElementById('download-btn').addEventListener('click', () => {
    const updatedJson = JSON.stringify(pixelsData, null, 2);
    const blob = new Blob([updatedJson], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'updated_blocks.json';
    a.click();
    URL.revokeObjectURL(url);
});

// Save edited pixel data
document.getElementById('save-btn').addEventListener('click', () => {
    selectedData.width = parseInt(document.getElementById('pixel-width').value);
    selectedData.height = parseInt(document.getElementById('pixel-height').value);
    selectedData.imageUrl = document.getElementById('pixel-imageUrl').value;
    selectedData.linkUrl = document.getElementById('pixel-linkUrl').value;
    selectedData.title = document.getElementById('pixel-title').value;

    selectedPixel.style.width = `${selectedData.width * 10}px`;
    selectedPixel.style.height = `${selectedData.height * 10}px`;
    selectedPixel.querySelector('img').src = selectedData.imageUrl;
    selectedPixel.querySelector('img').alt = selectedData.title;

    // Hide the edit form after saving
    hideEditForm();
});

// Delete button click event
document.getElementById('delete-btn').addEventListener('click', () => {
    if (selectedPixel && selectedData) {
        // Remove selected pixel from pixelsData array
        const index = pixelsData.indexOf(selectedData);
        if (index !== -1) {
            pixelsData.splice(index, 1);
        }

        // Remove selected pixel from the DOM
        selectedPixel.remove();

        // Hide the edit form and clear selection
        hideEditForm();
    }
});

// Function to hide edit form
function hideEditForm() {
    document.getElementById('edit-form').style.display = 'none';
    selectedPixel = null;
    selectedData = null;
}
