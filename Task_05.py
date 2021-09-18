import math 
def area_of_triangle(x,y,z):
    s_length = (x+y+z)/2
    area_t = (s_length-x)*(s_length-y)*(s_length-z)
    area_t = area_t*s_length
    area_t = math.sqrt(area_t)
    return area_t


area_of_t = area_of_triangle(4,5,6)
print(str(area_of_t))

