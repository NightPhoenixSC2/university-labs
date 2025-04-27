import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

R1 = 2.5
R2 = 0.5
height = 3.0
slices = 20
stacks = 5

def generate_grid_points(R1, R2, height, slices, stacks):
    points = []
    for i in range(stacks + 1):
        z = i * (height / stacks)
        r = R1 + (R2 - R1) * (i / stacks)
        for j in range(slices):
            angle = 2 * np.pi * j / slices
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            points.append((x, y, z))
    return points

def draw_circle(r, z, slices):
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    for i in range(slices):
        angle = 2 * np.pi * i / slices
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        glVertex3f(x, y, z)
    glEnd()

def draw_lines_between_circles(r1, z1, r2, z2, count):
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for i in range(count):
        angle = 2 * np.pi * i / count
        x1 = r1 * np.cos(angle);  y1 = r1 * np.sin(angle)
        x2 = r2 * np.cos(angle);  y2 = r2 * np.sin(angle)
        glVertex3f(x1, y1, z1)
        glVertex3f(x2, y2, z2)
    glEnd()

def draw(R1, R2, height, slices, stacks):
    # фігура
    draw_circle(R1, 0.0, slices)
    draw_circle(R2, height, slices)
    draw_lines_between_circles(R1, 0.0, R2, height, 4)

    # точки по периметру
    points = generate_grid_points(R1, R2, height, slices, stacks)
    glColor3f(1, 0, 0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    for x, y, z in points:
        glVertex3f(x, y, z)
    # центри кілець
    glVertex3f(0.0, 0.0, 0.0)    # центр нижнього кола
    glVertex3f(0.0, 0.0, height)    # центр верхнього кола
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    angle = 0.0

    running = True
    while running:
        clock.tick(60)
        for evt in pygame.event.get():
            if evt.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 1, 0, 1)
        draw(R1, R2, height, slices, stacks)
        glPopMatrix()

        angle += 0.5
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()