""" SYSC 1005 A Fall 2014 Lab 4 - Part 3.
"""

from Cimpl import *

#--------------------------------------
# This function was presented in class:

def grayscale(img):
    """
    Convert the specified picture into a grayscale image.
    """

    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        
        set_color(img, x, y, gray)

def negative(img):
    """
    Creates a negative image by changing red, green and blue components to their opposite
    """
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        rv = 255 - r
        gv = 255 - g
        bv = 255 - b
        
        col = create_color (rv, gv, bv)
        set_color (img, x, y, col)
        
def weighted_grayscale(img):
    """
    Makes image grayscaled but takes human eye perception into account
    """
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        brightness = ( (r * 0.299) + (g * 0.587) + (b * 0.114) )
        
        gray = create_color (brightness, brightness, brightness)
        
        set_color(img, x, y, gray)
        
        