import os

from utils.file_loader import save_uploaded_file
from analyzer.dataset_detector import DatasetDetector


detector = DatasetDetector()


def upload_dataset(uploaded_file):

    path = save_uploaded_file(uploaded_file)

    analysis = detector.analyze(path)

    return {

        "success": True,

        "filename": uploaded_file.name,

        "extension": os.path.splitext(uploaded_file.name)[1],

        "size": round(uploaded_file.size/1024,2),

        **analysis
    }