from typing import Any

import pytest

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log(filename="")
    def add_numbers(a: int) -> float:
        return 10 / a

    result = add_numbers(5)

    captured = capsys.readouterr()
    assert captured.out == "add_numbers Ok\n"
    assert result == 2

    with pytest.raises(ZeroDivisionError) as excinfo:
        add_numbers(0)

    assert str(excinfo.value) == 'division by zero'
    captured2 = capsys.readouterr()
    assert captured2.out == "add_numbers error: division by zero. Inputs: (0,) {}\n"
