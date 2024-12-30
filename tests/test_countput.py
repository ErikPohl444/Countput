import pytest
from src.Countput import Countput


def test_topn_as_string(capsys):
    x = Countput([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    x.formatted_topn_output(n=2)
    captured = capsys.readouterr()
    assert captured.out == "4 4\n3 3\n"

def test_topn_as_string_with_header(capsys):
    x = Countput([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    x.formatted_topn_output(n=2, header="test")
    captured = capsys.readouterr()
    assert captured.out == "test\n4 4\n3 3\n"


def test_topn_as_dict():
    x = Countput([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    d = x.return_as_dict()
    print(d)
    assert d == {1: 1, 2: 2, 3: 3, 4: 4}


def test_topn_as_list_of_strings():
    x = Countput([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    d = x.return_topn_as_list_of_strings()
    print(d)
    assert d == ['4 4', '3 3', '2 2', '1 1']
