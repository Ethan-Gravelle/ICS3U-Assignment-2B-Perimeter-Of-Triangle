#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: April 29 2021
# This program calculates the perimeter of a triangle
#    with the sides inputted by the user


def main():
    "#main function"
    print("We will be calculating the perimeter of a triangle.")
    "#input"
    side_1 = int(input("Enter side 1 of triangle (mm):"))
    side_2 = int(input("Enter side 2 of triangle (mm):"))
    side_3 = int(input("Enter side 3 of triangle (mm):"))
    "#process"
    perimeter = side_1 + side_2 + side_3
    "#output"
    print("")
    print("Perimeter is {0}mm".format(perimeter))
    print("Done.")


if __name__ == "__main__":
    main()
