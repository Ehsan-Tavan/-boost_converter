import argparse
from pathlib import Path


class BaseConfig:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument("--data_dir", type=str, help="",
                                 default=Path(__file__).parents[2].__str__() + "/data/")

        self.parser.add_argument("--data_file", type=str, help="",
                                 default="Data_DCDC_Converter.xlsx")

        self.parser.add_argument("--data_headers", type=list, help="",
                                 default=["VO", "DVO",	"IL", "DIL", "E", "DE",	"U=Target"])

        self.parser.add_argument("--normalizer_type", type=str, help="StandardScaler, MinMaxScaler",
                                 default="StandardScaler")

    def get_config(self):
        return self.parser.parse_args()
