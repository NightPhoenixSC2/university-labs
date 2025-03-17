import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(0, 800, 0, 600)

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)


def random_color():
    return random.random(), random.random(), random.random()


def draw_figure(x0, y0, m, clvis, clunvis, visible, hidden, line_width=2.0):
    glLineWidth(line_width)
    glBegin(GL_LINES)

    glColor3fv(clunvis)
    for edge in hidden:
        glVertex2f(x0 + edge[0][0] * m, y0 + edge[0][1] * m)
        glVertex2f(x0 + edge[1][0] * m, y0 + edge[1][1] * m)

    glColor3fv(clvis)
    for edge in visible:
        glVertex2f(x0 + edge[0][0] * m, y0 + edge[0][1] * m)
        glVertex2f(x0 + edge[1][0] * m, y0 + edge[1][1] * m)

    glEnd()


def draw_center_point():
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(400, 300)
    glEnd()


def main():
    visible = [([-0.3, 0.4], [-0.3, 0.6]), ([0.3, 0.4], [0.3, 0.6]), ([-0.3, 0.6], [0.3, 0.6]),
               ([-0.3, 0.4], [0.3, 0.4]),
               ([-0.3, 0.6], [-0.2, 0.7]), ([-0.2, 0.7], [0.4, 0.7]), ([0.4, 0.7], [0.3, 0.6]),
               ([0.4, 0.7], [0.4, 0.5]),
               ([0.4, 0.5], [0.3, 0.4]), ([0.2, 0.4], [0.2, -0.1]), ([0.1, 0.4], [0.1, -0.2]),
               ([-0.1, 0.4], [-0.1, -0.2]),
               ([-0.3, -0.2], [0.3, -0.2]), ([0.3, -0.2], [0.3, -0.4]), ([0.3, -0.4], [-0.3, -0.4]),
               ([-0.3, -0.4], [-0.3, -0.2]),
               ([-0.3, -0.2], [-0.2, -0.1]), ([-0.2, -0.1], [-0.1, -0.1]), ([0.2, -0.1], [0.4, -0.1]),
               ([0.4, -0.1], [0.4, -0.3]),
               ([0.4, -0.1], [0.3, -0.2]), ([0.4, -0.3], [0.3, -0.4]), ([0.2, -0.1], [0.1, -0.2])]

    hidden = [([-0.3, 0.4], [-0.2, 0.5]), ([-0.2, 0.5], [-0.2, 0.7]), ([-0.2, 0.5], [0.4, 0.5]),
              ([0.0, 0.5], [-0.1, 0.4]),
              ([0.2, 0.5], [0.1, 0.4]), ([0.0, 0.5], [0.0, -0.1]), ([0.2, 0.5], [0.2, 0.4]),
              ([-0.1, -0.1], [0.2, -0.1]),
              ([0.0, -0.1], [-0.1, -0.2]), ([-0.2, -0.1], [-0.2, -0.3]), ([-0.2, -0.3], [-0.3, -0.4]),
              ([-0.2, -0.3], [0.4, -0.3])]

    clvis = random_color()
    clunvis = random_color()

    h, k = 400, 300
    a, b = 300, 200

    # Розміри
    min_size = 50
    max_size = 200

    t = math.pi
    dt = 0.01

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        x0 = h + a * math.cos(t)
        y0 = k + b * math.sin(t)

        m = max_size - (max_size - min_size) * ((y0 - (k - b)) / (2 * b))


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_figure(x0, y0, m, clvis, clunvis, visible, hidden)
        draw_center_point()
        pygame.display.flip()
        pygame.time.wait(10)

        t += dt
        if t > 2 * math.pi:
            t -= 2 * math.pi


if __name__ == "__main__":
    main()
