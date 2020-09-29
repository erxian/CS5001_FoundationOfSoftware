'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from user about the day of the week and \
the weather, and create an exercise plan.
'''


def check_temperature(t):
    normal_exercise_duration = 45
    abnormal_exercise_duration = 30
    if 35 < t < 75:
        exercise_duration = normal_exercise_duration
    else:
        exercise_duration = abnormal_exercise_duration

    return exercise_duration


def check_workout_days(d, h):
    workout_days = {"M", "W", "F", "Sa"}
    if d in workout_days or h == "Y":
        return True
    else:
        return False


def main():
    days_of_week = {"M", "Tu", "W", "Th", "F", "Sa", "Su"}
    valid_answer = {"Y", "N"}

    day = input("What day is it? ").capitalize()
    is_holiday = input("Is it a holiday? ").upper()
    is_raining = input("Is it raining? ").upper()
    temperature = float(input("What is the temperature? "))

    if day not in days_of_week or is_holiday not in valid_answer or \
            is_raining not in valid_answer:
        print("Swim for 35 minutes")
    else:
        is_workout_days = check_workout_days(day, is_holiday)
        running_days = {"M", "W", "F"}
        normal_exercise_duration = 45
        if day in running_days and is_holiday == "N":
            exercise_duration = check_temperature(temperature)
            print("Run for %d minutes" % exercise_duration)
        elif (day == "Sa" or is_holiday == "Y") and is_raining == "N":
            print("Hike for %d minutes" % normal_exercise_duration)
        elif is_raining == "Y" and is_workout_days is True:
            print("Swim for %d minutes" % normal_exercise_duration)
        else:
            print("Take a rest day")


if __name__ == "__main__":
    main()
