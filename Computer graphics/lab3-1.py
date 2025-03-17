import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(0, 800, 0, 600)

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)


def random_color():
    return (random.random(), random.random(), random.random())


def draw_figure(x0, y0, m, clvis, clunvis, visible, hidden, line_width=2.0):
    glLineWidth(line_width)
    glBegin(GL_LINES)

    # Draw hidden lines
    glColor3fv(clunvis)
    for edge in hidden:
        glVertex2f(x0 + edge[0][0] * m, y0 + edge[0][1] * m)
        glVertex2f(x0 + edge[1][0] * m, y0 + edge[1][1] * m)

    # Draw visible lines
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

    x0, y0 = 0, 600
    m = 3
    clvis = random_color()
    clunvis = random_color()
    speed_x, speed_y = 3, -2.3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_figure(x0, y0, m, clvis, clunvis, visible, hidden, line_width=2.0)
        draw_center_point()
        pygame.display.flip()
        pygame.time.wait(30)

        x0 += speed_x
        y0 += speed_y

        center_x, center_y = display[0] / 2, display[1] / 2
        distance = ((x0 - center_x) ** 2 + (y0 - center_y) ** 2) ** 0.5
        m += 2

        if x0 > 580 or y0 < 0:
            x0, y0 = 0, 600
            m = 3


if __name__ == "__main__":
    main()
