a = 7
b = 2
c = 8


def triangle_perimeter(z=a, x=b, v=c):
    return z+x+v


def triangle_area(z=a, x=b, v=c):
    p = triangle_perimeter(z, x, v)/2
    return (p*(p-z)*(p-x)*(p-c))**0.5
