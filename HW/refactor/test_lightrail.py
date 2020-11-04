from lightrail import is_valid_station, get_direction, get_num_stops
from lightrail import get_station_index


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))


def test_get_direction():
    assert(get_direction("University of Washington", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "University of Washington")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_num_stops():
    assert(get_num_stops("University of Washington", "Angle Lake") == 15)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University Street", "Tacoma") == 0)


def test_get_station_index():
    assert(
       get_station_index("University of Washington", "Angle Lake") ==
       (0, 15))
    assert(
       get_station_index("Angle Lake", "University of Washington") ==
       (15, 0))
    assert(
       get_station_index("University Street", "University Street") ==
       (0, 0))
    assert(get_station_index("University Street", "Tacoma") == (0, 0))
