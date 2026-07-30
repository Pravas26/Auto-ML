from backend.routes import upload_dataset


class Backend:

    def save_dataset(self, uploaded_file):

        result = upload_dataset(uploaded_file)

        return result