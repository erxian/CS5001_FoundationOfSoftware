from exercise import check_temperature, check_workout_days


def test_check_temperature():
    assert(check_temperature(50) == 45)
    assert(check_temperature(20) == 30)


def test_check_workout_days():
    assert(check_workout_days("M", "Y") == True)
    assert(check_workout_days("Tu", "N") == False)
    assert(check_workout_days("Tu", "Y") == True)
    assert(check_workout_days("M", "N") == True)