import math

def radius_of_circle(radius):
    area= math.pi* radius **2
    circumference= 2 * math.pi * radius
    return area, circumference

a,c= radius_of_circle(3)
print('Area of circle:',round(a,2), 'and', 'Circumference of circle:',round(c,2))