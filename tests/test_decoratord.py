import pytest
from src.decorators import log

def test_log(capsys):
    @log(filename = '')
    def add_numbers(a):
        return 10 / a

    result = add_numbers(5)

    captured = capsys.readouterr()
    assert captured.out == 'add_numbers Ok\n\n'
    assert result == 2

