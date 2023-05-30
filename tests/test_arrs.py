from utils import arrs
import pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1) is None


def test_get_out_of_range():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
