import os
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Any:
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
                filename_no_space = filename.replace(" ", "")
                if filename_no_space > "":
                    # если есть имя файла пишем в файл
                    if not os.path.exists(os.path.join(os.path.dirname(__file__), "log")):
                        os.mkdir("log")
                    path_to_file = os.path.join(os.path.dirname(__file__), "log", filename_no_space)
                    # path_to_file = os.path.abspath("log/" + filename_no_space)
                    with open(path_to_file, "a") as file:
                        file.write(log_text_for_write + "\n")
                else:
                    # если нет имени файла пишем в консоль
                    print(log_text_for_write)

            try:
                result = func(*args, **kwargs)
            except Exception as name_error:
                # если функция выполняется с ошибкой
                log_text = f"{func.__name__} error: {name_error}. Inputs: {args} {kwargs}"

                log_write(log_text)
                raise name_error
            else:
                # если функция выполняется правильно
                log_text = f"{func.__name__} Ok"
                log_write(log_text)
                return result

        return wrapper

    return log_decorator


@log(filename="")
def add_numbers(a: int) -> float:
    return 10 / a


current_directory = os.getcwd()
print(current_directory)

print(add_numbers(2))
