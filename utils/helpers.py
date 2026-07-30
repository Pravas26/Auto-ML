import os


def get_extension(filename):

    return os.path.splitext(filename)[1].lower()


def get_file_size(file):

    return round(file.size / 1024, 2)