import json
import csv
import logging
from typing import TextIO, List


class Saver:
    """
    Provides functionality for saving an object to a file with
    the selected extension and at a given path.
    """
    def __init__(self):
        self.__savers = {
            "json": self.__array_save_to_json,
            "csv": self.__array_save_to_csv
        }

    def __array_save_to_json(self, fh: TextIO, array: List):
        """
        Convert to string type and save json
        object to file with .json extension.
        """
        json.dump(array, fh)

    def __array_save_to_csv(self, fh: TextIO, array: List):
        """
        Save json object to file with .csv extension.
        """
        csv_writer = csv.writer(fh)
        csv_writer.writerows(array)

    def array_save(self, path: str, array: List) -> bool:
        try:
            file_type: str = path.split('.')[-1]
            saver = self.__savers[file_type]

            with open(path, mode='x') as fh:
                saver(fh, array)

            return True

        except KeyError:
            logging.error(
                f"You should choose an file extension from follows:\n"
                f"{' '.join([exten for exten in self.__savers])}"
            )
        except FileExistsError:
            logging.error("File with same name already exists.")

        return False
