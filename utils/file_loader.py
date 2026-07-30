import os
import shutil

from backend.config import DATASET_FOLDER


def save_uploaded_file(uploaded_file):

    save_path = os.path.join(
        DATASET_FOLDER,
        uploaded_file.name
    )

    with open(save_path, "wb") as f:

        f.write(uploaded_file.getbuffer())

    return save_path