"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.
"""

from images import Image


def enlarge(image, factor):
    """Builds and returns a copy of the image which is larger
    by the factor."""
    width = image.getWidth()
    height = image.getHeight()
    new_image = Image(width * factor, height * factor)
    for y in range(height):
        for x in range(width):
            color = image.getPixel(x, y)
            new_image.setPixel(factor * x, factor * y, color)
            new_image.setPixel(factor * x + 1, factor * y, color)
            new_image.setPixel(factor * x, factor * y + 1, color)
            new_image.setPixel(factor * x + 1, factor * y + 1, color)

    return new_image


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    newimage = enlarge(image, 2)
    newimage.draw()


if __name__ == "__main__":
    main()
