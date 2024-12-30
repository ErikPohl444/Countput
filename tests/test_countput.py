import pytest
from src.Countput import Countput


def test_powerset(capsys):
    x = Countput([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    x.formatted_topn_output(n=2)
    captured = capsys.readouterr()
    assert captured.out == "4 4\n3 3\n"
