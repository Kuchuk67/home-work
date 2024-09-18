import os
from functools import wraps
from typing import TypeVar, cast, Any, Callable


def log(filename: str = '') -> Any:
    """
    Декоратор позволяет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    @log(filename="mylog.txt") имя файла для логов
    Если filename не задан, логи выводятся в консоль.
    """

    def log_decorator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            def log_write(log_text_for_write: str) -> None:
                filename_no_space = filename.replace(' ', '')
                if filename_no_space > '':
                    # если есть имя файла пишем в файл
                    path_to_file = os.path.join(os.path.dirname(__file__), "log", filename_no_space)
                    #path_to_file = os.path.abspath("log/" + filename_no_space)
                    with open(path_to_file, "a") as file:
                        file.write(log_text)
                else:
                    # если нет имени файла пишем в консоль
                    print(log_text)
            try:
                result = func(*args, **kwargs)
            except Exception as name_error:
                # если функция выполняется с ошибкой
                log_text = (f"{func.__name__} error: {name_error}. Inputs: {args} {kwargs} \n")

                log_write(log_text)
                raise name_error
            else:
                # если функция выполняется правильно
                log_text = (f"{func.__name__} Ok\n")
                log_write(log_text)
                return result







        return wrapper

    return log_decorator



