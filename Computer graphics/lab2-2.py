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


def generate_figures(n):
    figures = []
    x0, y0 = 400, 300  # center of the screen
    m = 400  # size of the first figure
    for _ in range(n):
        clvis = random_color()
        clunvis = random_color()
        figures.append((x0, y0, m, clvis, clunvis))
        m *= 0.8  # decrease the size of the next figure
    return figures


def main(n):
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

    figures = generate_figures(n)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for x0, y0, m, clvis, clunvis in figures:
            draw_figure(x0, y0, m, clvis, clunvis, visible, hidden, line_width=2.0)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main(4)