from backend.routes import upload_dataset


class Backend:

    def save_dataset(self, uploaded_file):

        return upload_dataset(uploaded_file)