'''
Zengping Xu
CS 5001 Fall 2020

This program get inputs from user about the width and height
of a rectangle, and a character will use to draw the rectangle.
Then draw a rectangle as the user wished
'''


def main():
    width = int(input("Enter a desired width in columns: "))
    height = int(input("Enter a desired height in rows: "))
    character = input("Enter a character that you will use \
to draw the rectangle: ")
    count = 0
    space = " "
    if height > 2:
        print(character*width)
        while count < height - 2:
            print(character + space*(width - 2) + character)
            count += 1
        print(character*width)
    else:
        print("Height is too low to draw a rectangle")


if __name__ == "__main__":
    main()
