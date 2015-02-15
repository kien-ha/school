""" SYSC 1005 A Fall 2014 Lab 4 - Parts 1 and 2
Image processing examples.

D.L.Bailey, SCE, Carleton University
"""

from Cimpl import *

#---------------------------------------------
#
# These two functions were presented in class:

# maximize_red is used in Part 1, Exercise 1

def maximize_red(img):
   """ Modify the photo bound to img to look like it was taken at 
   sunset, by maximizing the red component of every pixel.
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      new_color = create_color(255, g, b)
      set_color(img, x, y, new_color)
      
# make_sunset is used in Part 2, Exercise 3      

def make_sunset(img):
   """ Modify the photo bound to img to look like it was taken at 
   sunset, by reducing the green and blue components of every pixel.
   """
   for pixel in img:
      x, y, col = pixel  
      r, g, b = col

      g = g * 0.7 # decrease green by 30%
      b = b * 0.7 # decrease blue by 30%

      col = create_color(r, g, b)
      set_color(img, x, y, col)

def red_channel (img):
   """
   No colours of Green or Blue, only red
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      g = 0
      b = 0
      
      col = create_color (r, g, b)
      set_color (img, x, y, col)
      
def green_channel (img):
   """
   No colours of Red or Blue, only green
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      r = 0
      b = 0
      
      col = create_color (r, g, b)
      set_color (img, x, y, col)
      
def blue_channel (img):
   """
   No colours of Red or Green, only blue
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      r = 0
      g = 0 
      
      col = create_color (r, g, b)
      set_color (img, x, y, col)
      
def halve_brightness (img):
   """
   Reduce the brightness of the image by half
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      r = r * 0.5 #decrease red by half
      g = g * 0.5 #decrease green by half
      b = b * 0.5 #decrease blue by half
      
      col = create_color (r, g, b)
      set_color (img, x, y, col)
      
def swap_red_blue (img):
   """
   swaps red and blue components
   """
   for pixel in img:
      x, y, col = pixel
      r, g, b = col
      
      r1 = r
      r = b
      b = r1
      
      col = create_color (r, g, b)
      set_color (img, x, y, col)