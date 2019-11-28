from models.matrix import Matrix
import math


def transladar(tx,ty,tz, points = []):

    print(points)


def translate(d, x, y, z, points = []):
    # to translate:
    # p' = t * p;

    if type(points) is not tuple:
        return str(type(list))

    if d == 2:
        T = Matrix(3, 3, [1, 0, x, 0, 1, y, 0, 0, 1])
    elif d == 3:
        T = Matrix(4, 4, [1, 0, 0, x, 0, 1, 0, y, 0, 0, 1, z, 0, 0, 0, 1])

    newpoints = [];

    if T:
        for point in points:
            P = Matrix(3,1, list(point))
            # print(P)
            newpoint = T.dot(P)
            newpoints.append(newpoint)

    return newpoints

# eixo 1 = x, 2 = y, 3 = z
# points are the same that vertices
def rotate(graus, eixo, points = ()):
    if type(points) is not tuple:
        return str(type(points))

    if eixo == 1:
        R = Matrix(3, 3, [math.cos(graus),0,math.sin(graus),0,1,0,-math.sin(graus),math.cos(graus)])
    elif eixo == 2:
        R = Matrix(3, 3, [1,0,0,0,math.cos(graus),-math.sin(graus),0,math.sin(graus),math.cos(graus)])
    else:
        R = Matrix(3, 3, [math.cos(graus),-math.sin(graus),0,math.sin(graus),math.cos(graus),0,0,0,1])

    print("graus: ")
    for point in points:
        P = Matrix(1,3,[point[0],point[1],point[2]])
        print(P)
