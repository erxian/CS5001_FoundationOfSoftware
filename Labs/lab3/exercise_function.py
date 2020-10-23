'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from user about the day of the week and 
the weather, and create an exercise plan.
'''


normal_exercise_duration = 45
abnormal_exercise_duration = 30

def check_temperature(temp):
    '''
    Function -- check_temperature
        check the value of termperature with the lowest running temprature
        and the highest running temperature, then determine the exercise duration.
    Parameters:
        temp -- the value of temperature, will not be modified
    Return a number of exercise duration
    '''    
    lowest_running_temp = 35
    highest_running_temp = 75
    if lowest_running_temp < temp < highest_running_temp:
        exercise_duration = normal_exercise_duration
    else:
        exercise_duration = abnormal_exercise_duration

    return exercise_duration


def check_workout_days(day, holiday):
    '''
    Function --  check_workout_days
        check if one day is a workout day, workout days are Monday, Wednesday,
        Friday, Saturday or Holiday.
    Parameters:
        day -- the day in week
        holiday -- if the day is a holiday, the value of holiday is Y or N
    Return a boolean value represents if a day is a workout day, True means the day
        is workout day while False means the day is not.
    '''
    workout_days = {"M", "W", "F", "Sa"}
    if day in workout_days or holiday == "Y":
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
