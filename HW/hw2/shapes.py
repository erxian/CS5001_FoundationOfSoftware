'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from user about the information of a shape, \
and calculates the area of the shape.
'''


def main():
    valid_shape = {"triangle", "square", "rectangle"}
    shape = input("Select a shape (triangle, square, or rectangle): ").lower()

    if shape not in valid_shape:
        print("Unknown shape")
    else:
        valid_dimension = 0
        if shape == "square":
            width = float(input("Enter the width: "))
            # To be valid, a dimension must be greater than 0
            if width <= valid_dimension:
                print("Invalid width")
            else:
                square = width * width
                print("The area of the %s is %.2f" % (shape, square))
        else:
            # The shape is triangle or rectangle
            width = float(input("Enter the width: "))

            # To be valid, a dimension must be greater than 0
            if width <= valid_dimension:
                print("Invalid width")
            else:
                height = float(input("Enter the height: "))

                # To be valid, a dimension must be greater than 0
                if height <= valid_dimension:
                    print("Invalid height")
                else:
                    if shape == "triangle":
                        square = width * height / 2
                    else:
                        square = width * height  # The shape is rectangle
                    print("The area of the %s is %.2f" % (shape, square))


if __name__ == "__main__":
    main()
