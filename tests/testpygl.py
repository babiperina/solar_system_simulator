import pygame
from OpenGL import GL
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from models.sistema_solar import SistemaSolar
from utils.transformacoes import *
import math

from models.geometrics import Triangle


def drawTriangle(triangle):
    glBegin(GL_LINES)
    for aresta in triangle.arestas:
        for vertex in aresta:
            glVertex3fv(triangle.edges[vertex])
    glEnd()

def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(100, 100) # Coordinates for the bottom left point
    glVertex2f(200, 100) # Coordinates for the bottom right point
    glVertex2f(200, 200) # Coordinates for the top right point
    glVertex2f(100, 200) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

def mapear(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


def draw_esfera(raio, vertices, distancia, rgb):
    GL.glBegin(GL.GL_POINTS)
    n_vertices = vertices
    for i in range(0, n_vertices):
        lon = mapear(i, 0, n_vertices, -math.pi, math.pi)
        for j in range(0, n_vertices):
            lat = mapear(j, 0, n_vertices, -math.pi / 2, math.pi / 2)
            x = raio * math.sin(lon) * math.cos(lat)
            y = raio * math.sin(lon) * math.sin(lat)
            z = raio * math.cos(lon)
            GL.glColor3f(rgb[0],rgb[1],rgb[2])
            GL.glVertex3f(x+distancia, y+distancia, z+distancia)
    GL.glEnd()


def camera(event):
    if event:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("CIMA")
                # glTranslatef(0, 1, 0)
                glRotatef(-10,1,0,0)
            elif event.key == pygame.K_DOWN:
                print("BAIXO")
                # glTranslatef(0, -1, 0)
                glRotatef(10,1,0,0)
            elif event.key == pygame.K_LEFT:
                print("ESQUERDA")
                # glTranslatef(-1, 0, 0)
                glRotatef(-10,0,1,0)
            elif event.key == pygame.K_RIGHT:
                print("DIREITA")
                # glTranslatef(1, 0, 0)
                glRotatef(10,0,1,0)
            elif event.key == pygame.K_q:
                print("ZOOM IN")
                # glTranslatef(0, 0, 1)
                glScalef(1.2,1.2,1.2)
            elif event.key == pygame.K_w:
                print("ZOOM out")
                # glTranslatef(0, 0, -1)
                glScalef(0.8,0.8,0.8)
            else:
                print(event.key)

def main():
    edges = (
        (2, 0, 0),
        (1, 2, 0),
        (0, 1, 0)
    )

    triangle = Triangle(edges)

    sistema_solar = SistemaSolar()

    pygame.init()
    display = (700, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(150, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            camera(event)


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # drawTriangle(triangle)
        # gluSphere(gluNewQuadric(),4,25,25)
        # sphere(200,100)
        # draw_point(7.68962087583727e-16, 12.558103905862627, -199.6053456856543)
        # draw_point(1,1,1)
        for planeta in sistema_solar.get_planetas():
            rgb = planeta[3], planeta[4], planeta[5]
            draw_esfera(planeta[0], planeta[1], planeta[2], rgb)
        # draw_esfera(800,50,0)
        # rotate(90,1,triangle.edges)
        # glRotatef(1, 0, 1, 0)
        pygame.display.flip()
        pygame.time.wait(100)


main()
