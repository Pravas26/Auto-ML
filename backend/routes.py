import os
from backend.config import SUPPORTED_FILES
from utils.file_loader import save_uploaded_file
from utils.helpers import get_extension


def upload_dataset(uploaded_file):
    extension = get_extension(uploaded_file.name)
    if extension not in SUPPORTED_FILES:

        return {
            "success": False,
            "message": "Unsupported File Type"
        }

    path = save_uploaded_file(uploaded_file)
    return {
        "success": True,
        "filename": uploaded_file.name,
        "path": path,
        "size": round(uploaded_file.size / 1024,2),
        "extension": extension
    }