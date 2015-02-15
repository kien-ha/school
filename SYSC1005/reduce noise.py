from Cimpl import *

def reduce_noise(img):
    height = get_height(img)
    width = get_width(img)
    
    for x in range(width - 1):
        for y in range(height - 1):
            r, g, b = get_color(img, x, y)
            number_1 = r, g, b
        
            r, g, b = get_color(img, x + 1, y)
            number_2 = r, g, b
            
            r, g, b = get_color(img, x, y + 1)
            number_3 = r, g, b
            
            r, g, b = get_color(img, x - 1, y)
            number_4 = r, g, b
            
            r, g, b = get_color(img, x, y - 1)
            number_5 = r, g, b
            
            lst = sort[number_1, number_2, number_3, number_4, number_5]
            r, g, b = (lst[2])
            color = create_color(r, g, b)
            set_color(img, x, y, color)