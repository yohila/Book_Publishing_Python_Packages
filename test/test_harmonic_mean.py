import sys

import pytest

from imppkg.harmony import _calculate_result


# @pytest.mark.parametrize(
#     "inputs, expected",
#     [
#         (["3", "3", "3"], 3.0),
#         ([], 0.0),
#         (["foo", "bar"], 0.0),
#     ],
# )
# def test_harmony_parametrized(inputs, monkeypatch, capsys, expected):
#     monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)
#     main()
#     assert capsys.readouterr().out.strip() == colored(expected, "red", "on_cyan", attrs=["bold"])

my_list = [1.0]
def test_harmonic_mean():
    assert _calculate_result(my_list) == 1.0

FRUITS = ["apple"]


def test_len():
    assert len(FRUITS) == 1


def test_append():
    FRUITS.append("banana")
    assert FRUITS == ["apple", "banana"]
