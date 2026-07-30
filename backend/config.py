import os

BASE_DIR = os.getcwd()

DATASET_FOLDER = os.path.join(BASE_DIR, "storage", "datasets")
MODEL_FOLDER = os.path.join(BASE_DIR, "storage", "models")
REPORT_FOLDER = os.path.join(BASE_DIR, "storage", "reports")
TEMP_FOLDER = os.path.join(BASE_DIR, "storage", "temp")

SUPPORTED_FILES = [
    ".csv",
    ".xlsx",
    ".txt",
    ".zip"
]

os.makedirs(DATASET_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)