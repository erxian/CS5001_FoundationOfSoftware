from score import get_max, get_min
from score import get_median, get_average


def test_get_max():
    assert(get_max([68, 78, 88, 98]) == 98.0)
    assert(get_max([77, 78, 79, 80, 81]) == 81.0)
    assert(get_max([69, 72, 79, 83, 94]) == 94.0)


def test_get_min():
    assert(get_min([68, 78, 88, 98]) == 68.0)
    assert(get_min([77, 78, 79, 80, 81]) == 77.0)
    assert(get_min([69, 72, 79, 83, 94]) == 69.0)


def test_get_median():
    assert(get_median([68, 78, 88, 98]) == 83.0)
    assert(get_median([77, 78, 79, 80, 81]) == 79.0)
    assert(get_median([69, 72, 79, 83, 94]) == 79.0)


def test_get_average():
    assert(get_average([68, 78, 88, 98]) == 83.0)
    assert(get_average([77, 78, 79, 80, 81]) == 79.0)
    assert(get_average([69, 72, 79, 83, 94]) == 79.0)