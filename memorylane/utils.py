import os


def get_filename_from_path(file_path):
    file_name = os.path.basename(file_path)
    return file_name