import os
import shutil
import logging

SUPPORTED_EXTENSIONS = {'.pdf', '.docx'}

def get_submission_files(upload_dir):
    """
    Scans the upload directory and returns a list of valid PDF and DOCX file paths.
    """
    if not os.path.exists(upload_dir):
        logging.error(f"Upload directory does not exist: {upload_dir}")
        return []

    valid_files = []
    for root, _, files in os.walk(upload_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                valid_files.append(os.path.join(root, file))
            else:
                logging.warning(f"Ignoring unsupported file type: {file}")

    return valid_files


def clear_directory(folder_path):
    """
    Utility to purge all files inside a directory (e.g., clearing temporary processing files).
    """
    if not os.path.exists(folder_path):
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logging.error(f"Failed to delete {file_path}: {e}")
