from expenses import calculate_mileage, get_reimbursement_amount
from expenses import get_actual_mileage_rate, get_actual_trip_cost


def test_calculate_mileage():
    assert(calculate_mileage(1000, 1010) == 10)
    assert(calculate_mileage(100, 80) == 0)
    assert(calculate_mileage(-10, 10) == 0)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(10) == 5.75)
    assert(get_reimbursement_amount(21) == 12.07)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(36, 3.09) == 0.0858)
    assert(get_actual_mileage_rate(0, 3.09) == 0.0)
    assert(get_actual_mileage_rate(36, -3.09) == 0.0)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(1000, 1010, 36, 3.09) == 0.86)
    assert(get_actual_trip_cost(100, 123, 26, 4.79) == 4.24)
