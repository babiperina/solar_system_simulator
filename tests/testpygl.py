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


def draw_esfera(raio, n_stacks, n_setores, distanciadosol):
    angulo_setores = 2 * math.pi / n_stacks
    angulo_stacks = math.pi / n_setores
    # cores = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(0, n_stacks):
        for j in range(0, n_setores + 1):
            if j % 2 == 0:
                glColor3f(0, 0, 0)
            else:
                glColor3f(255,255,255)
            # x = (raio * math.cos(angulo_stacks)) * math.cos(angulo_setores)
            z = math.cos(math.pi - (angulo_stacks * j)) * raio
            y = math.sin(math.pi - (angulo_stacks * j)) * math.sin(angulo_setores * i) * raio
            x = math.sin(math.pi - (angulo_stacks * j)) * math.cos(angulo_setores * i) * raio
            glVertex3f(x+distanciadosol, y, z)

            z = math.cos(math.pi - (angulo_stacks * j)) * raio
            y = math.sin(math.pi - (angulo_stacks * j)) * math.sin(angulo_setores * (i + 1)) * raio
            x = math.sin(math.pi - (angulo_stacks * j)) * math.cos(angulo_setores * (i + 1)) * raio
            glVertex3f(x+distanciadosol, y, z)

    glEnd()

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glScalef(1.2,1.2,1.2)
            if event.button == 5:
                glScalef(0.8,0.8,0.8)


def main():
    sistema_solar = SistemaSolar()

    pygame.init()
    display = (1400, 850)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(150, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            camera(event)


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for planeta in sistema_solar.get_sistema_solar():
            draw_esfera(planeta[0], planeta[1], planeta[1], planeta[2])
        # sistema_solar.get_satelites()
        # for satelite in sistema_solar.get_satelites():
        #     draw_esfera(satelite[0], satelite[1], satelite[1], satelite[2])

        # glRotatef(1, 0, 1, 0)
        pygame.display.flip()
        pygame.time.wait(100)


main()
