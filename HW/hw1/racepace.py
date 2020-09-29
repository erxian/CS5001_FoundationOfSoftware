'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from the runners about the distance and time they run and 
calculate the racepace of them.

Examples:
11km, 0 hours, 58 minutes => 6.83 miles, 8:29 pace, 7.07 MPH 
8km, 0 hours, 51 minutes => 4.97 miles, 10:16 pace, 5.85 MPH 
32km, 2 hours, 46 minutes => 19.88 miles, 8:21 pace, 7.18 MPH 
'''


def main():
    kilometers = float(input("How many kilometers did you run? "))
    hour = int(input("What was your finish time? Enter hours: "))
    minutes = int(input("Enter minutes: "))

    miles = kilometers/1.61
    miles_with_unit = str(round(miles, 2)) + " miles,"

    total_minutes = hour * 60 + minutes
    pace_in_minute = int(total_minutes // miles)
    pace_in_second = ((total_minutes / miles - pace_in_minute) * 60)
    pace_in_second = round(pace_in_second)
    mile_in_hour = round(miles / (hour + minutes / 60), 2)

    average_time_per_mile = str(pace_in_minute) + ":" + str(pace_in_second) + " pace,"
    average_miles_per_hour = str(mile_in_hour) + " MPH"
    
    print(miles_with_unit, average_time_per_mile, average_miles_per_hour)


if __name__ == "__main__":
    main()
