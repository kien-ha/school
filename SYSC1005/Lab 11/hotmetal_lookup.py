from Cimpl import *

def build_hot_metal_lookup_table():
    lookup = {}
    
    for c in range(256):
        if c <= 170:
            new_red = (255/170) * c
            new_green = 0
        else:
            new_red = 255
            new_green = (255/(255-170)) * (c-170)
        col = create_color(new_red, new_green, 0)
        lookup[c] = col
    return lookup

hot_metal_table = build_hot_metal_lookup_table()

def hot_metal(img, table):
    for x, y, col in img:
        r, g, b = col
        weighted_brightness = int(0.3 * r + 0.59 * g + 0.11 * b)
        new_col = table[weighted_brightness]
        set_color(img, x, y, new_col)
    return img