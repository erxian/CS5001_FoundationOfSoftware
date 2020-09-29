'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from students about the courses they \
want to register for, and gives feedback to the students about \
their registration result.
'''


def main():
    valid_x_course = {"X101", "X102"}
    valid_b_course = {"B500", "B525", "B701"}
    course_number = input("Enter a course number: ").upper().replace(' ', '')

    if course_number in valid_x_course:
        print("You have successfully registered for", course_number)
    elif course_number in valid_b_course:
        x101_grade = input("What grade did you get for X101? ").upper()
        x102_grade = input("What grade did you get for X102? ").upper()

        valid_x101_grade = {"A", "B"}
        valid_x102_grade = {"A", "B", "C"}

        if x101_grade in valid_x101_grade and x102_grade in valid_x102_grade:
            print("You meet all the prerequisites and have successfully \
registered for", course_number)
        else:
            print("You do not meet the prerequisites for", course_number)
    else:
        print("Invalid course number")


if __name__ == "__main__":
    main()
