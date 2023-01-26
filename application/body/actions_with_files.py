from application.config.paths import FILES_INPUT_PATH
from application.logging.loggers import get_core_logger
from application.body.requesttoapi import get_csv_file_data_and_calculate
from faker import Faker

fake = Faker()


def to_create_file(file_name: str = None) -> None:
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath(f"{file_name}.txt")
    with open(path_to_file, mode="w") as file:
        file.write(f"{fake.text()}")
    logger.info(f"Path to file: {path_to_file}")


def to_read_file(file_name: str = None):
    path_to_file = FILES_INPUT_PATH.joinpath(f"{file_name}.txt")
    file_contents = path_to_file.read_text()
    return file_contents


def return_data_from_csv_average_function(link: str = None) -> str:
    result = get_csv_file_data_and_calculate(link)
    return f" Average height is {result['average_height']} sm, Average width is {result['average_weight']} kg\n"
