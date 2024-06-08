import os

# Define the path to the folder containing the images
folder_path = "./images/"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Sort the files to ensure they're in the correct order
files.sort()

# Counter for renaming
counter = 1

# Iterate over each file and rename
for filename in files:
    # Split the file name and its extension
    name, ext = os.path.splitext(filename)
    # New name for the file
    new_name = str(counter) + ext
    # Construct the full path for both old and new names
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    # Rename the file
    os.rename(old_path, new_path)
    # Increment counter for the next file
    counter += 1

print("All files renamed successfully.")
