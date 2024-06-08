import os

# Define the path to the folder containing the images
folder_path = "./images/"

# Get a list of all JPG files in the folder
jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

# Ensure there are at most 10000 JPG files
if len(jpg_files) > 10000:
    raise ValueError("The folder contains more than 10000 JPG files. Please reduce the number of files.")

# Sort the files to maintain a consistent order
jpg_files.sort()

# Rename each file
i, j = 1, 1
for index, filename in enumerate(jpg_files):
    # Create the new file name
    new_filename = f"{i}-{j}.jpg"
    # Define the full old and new file paths
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_filename)
    # Rename the file
    os.rename(old_file_path, new_file_path)
    
    # Update i and j
    j += 1
    if j > 100:
        j = 1
        i += 1

# Ensure no more than 100 * 100 files are present
if i > 100:
    raise ValueError("The folder contains more than 10000 JPG files. Please reduce the number of files.")
