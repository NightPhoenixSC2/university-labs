import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


vertices = [
    (2, 1, -0.5),
    (2, -1, -0.5),
    (-2, -1, -0.5),
    (-2, 1, -0.5),
    (2, 1, 0.5),
    (2, -1, 0.5),
    (-2, -1, 0.5),
    (-2, 1, 0.5)
]

edges = [
    (3, 0),
    (7, 4),
    (0, 4),
    (3, 7)
]


def draw_edges():
    for edge in edges:
        glBegin(GL_LINES)
        for vertex in edge:
            glVertex3fv(vertices[vertex])
        glEnd()


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)


angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glRotatef(angle, 1, 0, 0)

    draw_edges()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
    angle += 1