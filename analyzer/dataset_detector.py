import pandas as pd


class DatasetDetector:

    def analyze(self, path):

        df = pd.read_csv(path)

        return {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "preview": df.head(),

            "statistics": df.describe(),

            "missing": df.isnull().sum().reset_index().rename(
                columns={
                    "index":"Column",
                    0:"Missing Values"
                }
            )

        }