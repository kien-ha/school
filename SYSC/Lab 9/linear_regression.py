"""
SYSC 1005 Fall 2014 Lab 9, Parts 2 and 3
"""
import math

def distance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def get_points():
    """ Return a set of (x, y) points, with each point stored in a tuple.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def fit_line_to_points(points):
    sumx = 0
    sumy = 0
    sumxy= 0
    sumxx = 0
    n = len(points)
    for point in points:
        x, y = point
        sumx = sumx + x
        sumy = sumy + y
        sumxy = sumxy + (x*y)
        sumxx = sumxx + x**2
        
        m = (sumx * sumy - n * sumxy) / (sumx * sumx - n * sumxx)
        b = (sumx * sumxy - sumxx * sumy) / (sumx * sumx - n * sumxx)
        
    return m, b

def read_and_print_lines():
    infile = open("data.txt", "r")
    for line in infile:
        print(line)
    infile.close()
    
def read_points(filename):
    point = set()
    infile = open(filename, "r")
    for line in infile:
        numbers = line.split()
        x = float(numbers[0])
        y = float(numbers[1])
        a = x, y
        point.add(a)
    infile.close()
    return point

if __name__ == "__main__":
    insert_text = input("Choose text file to open: ")
    points = read_points(insert_text)
    m, b = fit_line_to_points(points)
    print("The best-fit line is y =", m, "x+", b)
