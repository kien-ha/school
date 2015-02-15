# SYSC 1005 A Fall 2014 Lab 7
# Revised: November 3, 2014.

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

if __name__ == "__main__":

    # A bit of code to demonstrate how to use get_image().
    terminate = False
    imgLoaded = False
    
    while not terminate:
        print("""
        L)oad image
        N)egative G)rayscale P)osterize S)epia tint E)dge detect 
        Q)uit""")
        Command = input(": ")
        
        if Command == "L":
            img = get_image()
            imgLoaded = True
            show(img)
            
        elif Command == "N":
            negative(img)
            show(img)
        
        elif Command == "G":          
            grayscale(img)
            show(img)
            
        elif Command == "P":
            posterize(img)
            show(img)
            
        elif Command == "S":
            sepia_tint(img)
            show(img)
            
        elif Command == "E":
            threshold = input("threshold: ")
            detect_edges_better(img, int(threshold))
            show(img)
            
        elif Command == "Q":
            terminate = True
            
        elif imgLoaded == False and Command != "Q":
            print ("No image loaded")
            
        else:
            print ("No such command")