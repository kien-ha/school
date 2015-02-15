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
        
def solarize(img, threshold):
    """
    Solarize the specified image.
    """

    for x, y, col in img:

        # Invert the values of all RGB components less than 128,
        # leaving components with higher values unchanged.

        red, green, blue = col

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)


#--------------------------------------
# A filter that uses an if-else statement.

def black_and_white(img):
    """
    Convert the specified image to a black-and-white (two-tone) image.
    """

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on whether
    # its brightness is in the lower or upper half of this range.

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3
        if brightness < 128:
            set_color(img, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(img, x, y, white)


#--------------------------------------
# A filter that uses an if-elif-else statement.

def black_and_white_and_gray(img):
    """
    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, col in img:
        red, green, blue = col
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

def extreme_contrast(img):
    for x, y, col in img:
        red, green, blue = col

        if red <= 127:
            red = 0
        else:
            red = 255
        
        if green <= 127:
            green = 0
        else:
            green = 255
        
        if blue <= 127:
            blue = 0
        else:
            blue = 255
            
        col = create_color(red, green, blue)
        set_color(img, x, y, col)    
def sepia_tint(img):
    grayscale(img)

    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        
        if r < 63:
            dark_gray = create_color(r*1.1, g, b*0.9)
            set_color(img, x, y, dark_gray)
        
        elif r < 191:
            medium_gray = create_color(r*1.15, g, b*0.85)
            set_color(img, x, y, medium_gray)
        
        else:
            light_gray = create_color(r*1.08, g, b*0.93)
            set_color(img, x, y, light_gray)
        
def _adjust_component(amount):
    if amount <= 63:
        return 31
    elif amount <= 127:
        return 95
    elif amount <= 191:
        return 159
    else:
        return 233
    
def posterize(img):
    
    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        colour = create_color(r,g,b)
        set_color(img, x, y, colour)
        
def simplify(img):
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    green = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    
    for x, y, col in img:
        r, g, b = col

        
        if r >= 200 and g >= 200 and b >= 200:
            set_color(img, x, y, white)
        elif r <= 50 and g <= 50 and b <= 50:
            set_color(img, x, y, black)
            
        elif r > g and r > b:
            set_color(img, x, y, red)
        elif g > r and g > b:
            set_color(img, x, y, green)
        else:
            set_color(img, x, y, blue)