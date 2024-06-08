import json
import os

def generate_blocks(n, m, space, max_blocks):
    blocks = []
    img_index = 1  # Start index for images
    extensions = ['.jpg', '.jpeg', '.png', '.webp','.svg']  # Supported image formats
    
    for i in range(1, (n // (m + space)) + 1):
        for j in range(1, (n // (m + space)) + 1):
            if len(blocks) >= max_blocks:
                return blocks  # Stop if max_blocks limit is reached
            
            # Calculate block position
            x = (m + space) * (j - 1) + 1
            y = (m + space) * (i - 1) + 1
            
            # Check if placing MxM block is possible at (x, y)
            if x + m - 1 <= n and y + m - 1 <= n:
                for ext in extensions:
                    img_filename = f"{img_index}{ext}"
                    img_path = f"./images/{img_filename}"
                    if os.path.exists(img_path):  # Check if image file exists
                        block = {
                            "x": x,
                            "y": y,
                            "width": m,
                            "height": m,
                            "imageUrl": img_path,
                            "linkUrl": f"/images/{img_filename}",
                            "title": ""
                        }
                        blocks.append(block)
                        img_index += 1  # Move to the next image
                        break  # Stop checking other extensions for this index
    return blocks

def save_blocks_to_json(blocks, filename):
    with open(filename, 'w') as json_file:
        json.dump(blocks, json_file, indent=4)

# Example usage
n = 100  # Size of the board
m = 4  # Size of each block
space = 0  # Space between blocks
max_blocks = 1000  # Maximum number of blocks to generate
blocks = generate_blocks(n, m, space, max_blocks)
total_blocks = len(blocks)  # Calculate total number of blocks
print(f"Total number of blocks generated: {total_blocks}")
save_blocks_to_json(blocks, 'blocks.json')
