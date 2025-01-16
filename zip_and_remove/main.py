import os
from zipfile import ZipFile


class DirectoryNotFound(Exception):
    def __init__(self, directory):
        self.directory = directory
        self.message = f"The \"{self.directory}\" directory does not exist!"
        super().__init__(self.message)


class FileExtensionNotFound(Exception):
    def __init__(self, file_extension):
        self.file_extension = file_extension
        self.message = f"No \"{self.file_extension}\" files found in the directory!"
        super().__init__(self.message)


def zip_and_remove(directory, file_extension):
    """
    Recursively zips all files with a specific extension in the given directory and deletes the original files.

    Args:
        directory (str): The path to the directory where the files are located.
        file_extension (str): The file extension (without the dot) of the files to zip and delete.

    Returns:
        None

    If no files with the specified extension are found, a message will be printed indicating so. If
    the specified directory does not exist, an error message will be printed.
    """

    if not os.path.exists(directory):
        raise DirectoryNotFound(directory)

    files_found = False  # Flag to check if we have any files to zip

    # List all files recursively, zip them, and delete after zipping
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(f".{file_extension}"):  # Ensure it matches the file extension exactly
                files_found = True  # Mark that we found a file to process

                file_path = os.path.join(root, file)

                # Create the .zip file path
                # zip_path = os.path.join(root, f"{file}.zip")  # path name + extension + zip
                zip_path = os.path.join(root, f"{os.path.splitext(file)[0]}.zip")  # # path name + zip
                # Zip the file
                with ZipFile(zip_path, 'w') as ziper:
                    ziper.write(str(file_path), arcname=file)  # Use arcname to avoid including the full path

                print(f"Zipped: {file_path} -> {zip_path}")

                # Delete the original file
                os.remove(file_path)
                print(f"Deleted: {file_path}")

    if not files_found:
        raise FileExtensionNotFound(file_extension)


if __name__ == "__main__":
    zip_and_remove("data_analysis", "html")
