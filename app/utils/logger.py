import logging
import logging.config as cf
from pathlib import Path

import yaml
from colorama import Fore, Style

COLORS = {
    "WARNING": Fore.YELLOW,
    "INFO": Fore.CYAN,
    "DEBUG": Fore.BLUE,
    "CRITICAL": Fore.YELLOW,
    "ERROR": Fore.RED,
}


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt=None, use_color=True):
        logging.Formatter.__init__(self, fmt)
        self.use_color = use_color

    def format(self, record):
        msg = super().format(record)
        if self.use_color and record.levelname in COLORS:
            return f"{COLORS[record.levelname]}{msg}{Style.RESET_ALL}"
        return msg


def load_logger(yaml_filename):
    # Get the directory of the current file (__file__)
    current_directory = Path(__file__).parent.absolute().parent.absolute()

    # Append the YAML file to this path
    yaml_file_path = current_directory / yaml_filename

    # Load and apply logging configuration
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)
        logging.config.dictConfig(config)