import math

from OpenGL import GL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500
def square():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def mapear(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


def draw_esfera(raio, vertices):
    GL.glBegin(GL.GL_POINTS)
    n_vertices = vertices
    for i in range(0, n_vertices):
        lon = mapear(i, 0, n_vertices, -math.pi, math.pi)
        for j in range(0, n_vertices):
            lat = mapear(j, 0, n_vertices, -math.pi / 2, math.pi / 2)
            x = raio * math.sin(lon) * math.cos(lat)
            y = raio * math.sin(lon) * math.sin(lat)
            z = raio * math.cos(lon)
            GL.glVertex3f(x, y, z)
    GL.glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()