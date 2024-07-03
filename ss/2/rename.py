import os

# Define the path to the folder containing the images
folder_path = "./images/"
# Define valid extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.svg']
# List to keep track of deleted files
deleted_files = []

try:
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Sort the files to ensure they're in the correct order
    files.sort()

    # Counter for renaming
    counter = 1

    # First pass: Rename each file to a temporary unique name
    for filename in files:
        # Split the file name and its extension
        name, ext = os.path.splitext(filename)

        # Check if it's a file (and not a directory)
        if os.path.isfile(os.path.join(folder_path, filename)):
            if ext.lower() in valid_extensions:
                # Temporary new name for the file
                temp_name = f"temp_{counter}{ext}"

                # Construct the full path for both old and temporary names
                old_path = os.path.join(folder_path, filename)
                temp_path = os.path.join(folder_path, temp_name)

                # Rename the file to the temporary name
                os.rename(old_path, temp_path)

                print(f"Temporarily renamed '{filename}' to '{temp_name}'")

                # Increment counter for the next file
                counter += 1
            else:
                # Delete the file with invalid extension
                os.remove(os.path.join(folder_path, filename))
                deleted_files.append(filename)
                print(f"Deleted file with invalid extension: '{filename}'")

    # Reset counter for the second pass
    counter = 1

    # Second pass: Rename each file from the temporary name to the final name
    for filename in os.listdir(folder_path):
        # Split the file name and its extension
        name, ext = os.path.splitext(filename)

        # Check if the file has the temporary prefix
        if name.startswith("temp_"):
            # Final new name for the file
            new_name = f"{counter}{ext}"

            # Construct the full path for both temporary and final names
            temp_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            # Rename the file to the final name
            os.rename(temp_path, new_path)

            print(f"Renamed '{filename}' to '{new_name}'")

            # Increment counter for the next file
            counter += 1

    print("All files renamed successfully.")

    # Log the deleted files
    if deleted_files:
        print("\nDeleted files:")
        for file in deleted_files:
            print(file)
    else:
        print("\nNo files were deleted.")

except FileNotFoundError:
    print("The specified folder does not exist.")
except PermissionError:
    print("You do not have the necessary permissions to access the files.")
except Exception as e:
    print(f"An error occurred: {e}")
