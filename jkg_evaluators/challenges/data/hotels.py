import shutil
import os
import json
import random
import pandas as pd
from .comparator_class import SolutionComparator


def _create_hotel_input(size):
    return [
        {
            "lat": random.normalvariate(0, 1) * 80,
            "lon": random.normalvariate(0, 1) * 180,
        }
        for _ in range(size)
    ]


class HotelSolutionComparator(SolutionComparator):

    @staticmethod
    def _get_input(size):
        return _create_hotel_input(size)

    @staticmethod
    def _dump_data(size, path):
        data_path = os.path.join("data", f"{size}.csv")
        shutil.copy(data_path, path)


def get_hotel_data(data_root="data"):
    os.makedirs(data_root, exist_ok=True)
    for data_size_k in [10, 20, 50, 100, 200, 500]:
        data_size = data_size_k * 1000
        dl_path = f"https://borza-hotelcom-data.s3.eu-central-1.amazonaws.com/challenge-{data_size}.csv"
        df = pd.read_csv(dl_path)
        write_path = os.path.join(data_root, f"data-{data_size}.csv")
        df.to_csv(write_path, index=False)


def dump_hotel_input(size, path="inputs.json"):
    obj = _create_hotel_input(size)
    with open(path, "w") as fp:
        json.dump(obj, fp)
