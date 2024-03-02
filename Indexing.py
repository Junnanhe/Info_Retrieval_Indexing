
import os

def list_files(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    # Sort the file paths by the file name converted to an integer
    file_paths.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
    return file_paths

input_dir = "HillaryEmails/HillaryEmails"

file_paths = list_files(input_dir)

# Print the first 100 file paths
for path in file_paths[:100]:
    print(path)


