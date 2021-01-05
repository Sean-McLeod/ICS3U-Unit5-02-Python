#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program can calculate the area of a triangle


def triangle_area(base, height):
    # this function calculates the area

    # process
    area = (base * height) / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets base(cm) and height(cm)

    # input
    base_string = input("Enter the base of a triangle (cm): ")
    height_string = input("Enter the height of a triangle (cm): ")
    print("\n")

    try:
        base_integer = int(base_string)
        height_integer = int(height_string)

        if base_integer > 0 and height_integer > 0:
            # call functions
            triangle_area(base_integer, height_integer)

        else:
            print("The values should be positive")

    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
