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

def generate_vertices(R1, R2, height, slices, stacks):
    vertices = []
    for i in range(stacks + 1):
        z = i * (height / stacks)
        r = R1 + (R2 - R1) * (i / stacks)
        ring = []
        for j in range(slices):
            angle = 2 * np.pi * j / slices
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            ring.append((x, y, z))
        vertices.append(ring)
    return vertices

def draw_spokes(r, z):
    angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]  # 0°, 120°, 240°
    glBegin(GL_LINES)
    for angle in angles:
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        glVertex3f(0, 0, z)
        glVertex3f(x, y, z)
    glEnd()

def draw_circle(center, radius, slices, z):
    glBegin(GL_LINE_LOOP)
    for i in range(slices):
        angle = 2 * np.pi * i / slices
        x = radius * np.cos(angle) + center[0]
        y = radius * np.sin(angle) + center[1]
        glVertex3f(x, y, z)
    glEnd()

def draw_grid_on_circle(r, z, slices):
    center = (0, 0)
    draw_circle(center, r, slices, z)
    draw_spokes(r, z)

def draw(vertices):
    stacks = len(vertices)
    slices = len(vertices[0])

    for ring in vertices:
        glBegin(GL_LINE_LOOP)
        for v in ring:
            glVertex3fv(v)
        glEnd()

    for i in range(slices):
        glBegin(GL_LINE_STRIP)
        for j in range(stacks):
            glVertex3fv(vertices[j][i])
        glEnd()

    r_bottom = np.linalg.norm(vertices[0][0][:2])
    draw_grid_on_circle(r_bottom, vertices[0][0][2], slices)

    r_top = np.linalg.norm(vertices[-1][0][:2])
    draw_grid_on_circle(r_top, vertices[-1][0][2], slices)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    glEnable(GL_DEPTH_TEST)
    glLineWidth(2.0)

    vertices = generate_vertices(R1, R2, height, slices, stacks)

    clock = pygame.time.Clock()
    angle = 0

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(angle, 1, 0, 1)
        draw(vertices)
        glPopMatrix()

        angle += 0.5

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()