import argparse
from pathlib import Path


class BaseConfig:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def add_arguments(self):
        self.parser.add_argument("--data_dir", type=str, help="",
                                 default=Path(__file__).parents[2].__str__() + "/data/")

        self.parser.add_argument("--data_file", type=str, help="",
                                 default="Data_DCDC_Converter.xlsx")

    def get_config(self):
        return self.parser.parse_args()
