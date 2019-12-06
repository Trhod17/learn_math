"""Methods for computing arithmetic calculations"""
from typing import List, SupportsFloat
from ruamel.yaml import YAML
import argparse
from pathlib import Path
import logging


def main(datafile):
    yaml = YAML(typ="safe")
    path = Path(datafile)
    with open(path, "r") as stream:
        try:
            my_data = yaml.load(stream)
            logging.info(f"Loading {path} file.")
            logging.info(f"Running data against addition() method.")
            print(f"Addition test result: {addition(x=my_data['addition_list'])}")
            print(f"Subtraction test result: {subtraction(x=my_data['addition_list'])}")
            print(f"Multiplication test result: {multiplication(x=my_data['addition_list'])}")
            print(f"Division test result: {division(x=my_data['addition_list'])}")

        except OSError as e:
            logging.error(f"An error has occurred trying to open {path}. -- {e}")
            exit(1)


def addition(x: List[SupportsFloat]):
    return sum(x)


def subtraction(x: List[SupportsFloat]):
    value: SupportsFloat = x[0]
    for num in x[1:]:
        value -= num
    return value


def multiplication(x: List[SupportsFloat]):
    value: SupportsFloat = x[0]
    for num in x[1:]:
        value *= num
    return value


def division(x: List[SupportsFloat]):
    value: SupportsFloat = x[0]
    for num in x[1:]:
        value /= num
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Specify arguments to modify program.")
    parser.add_argument(
        "-d",
        "--datafile",
        action="store",
        dest="datafile",
        type=str,
        help="Path and filename to YAML file containing data.",
        default="datafile.yml",
    )
    args = parser.parse_args()
    main(datafile=args.datafile)
