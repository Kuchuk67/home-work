import logging
import os

from config import PATH_HOME

if not os.path.exists(os.path.join(PATH_HOME, "logs")):
    os.mkdir(os.path.join(PATH_HOME, "logs"))


def logger_init(name_module: str) -> logging.Logger:
    # Настройка логирования
    named_logger = logging.getLogger(name_module)

    path_to_log_file = os.path.join(PATH_HOME, "logs", f"{name_module}.log")
    file_handler = logging.FileHandler(filename=path_to_log_file,
                                       mode='w',
                                       encoding='utf8')
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(name)s %(message)s')
    file_handler.setFormatter(file_formatter)
    named_logger.addHandler(file_handler)

    named_logger.setLevel(logging.INFO)
    return named_logger
