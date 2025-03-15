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

def main():
    visible = [([-0.3, 0.4], [-0.3, 0.6]), ([0.3, 0.4], [0.3, 0.6]), ([-0.3, 0.6], [0.3, 0.6]), ([-0.3, 0.4], [0.3, 0.4]),
               ([-0.3, 0.6], [-0.2, 0.7]), ([-0.2, 0.7], [0.4, 0.7]), ([0.4, 0.7], [0.3, 0.6]), ([0.4, 0.7], [0.4, 0.5]),
               ([0.4, 0.5], [0.3, 0.4]), ([0.2, 0.4], [0.2, -0.1]), ([0.1, 0.4], [0.1, -0.2]), ([-0.1, 0.4], [-0.1, -0.2]),
               ([-0.3, -0.2], [0.3, -0.2]), ([0.3, -0.2], [0.3, -0.4]), ([0.3, -0.4], [-0.3, -0.4]), ([-0.3, -0.4], [-0.3, -0.2]),
               ([-0.3, -0.2], [-0.2, -0.1]), ([-0.2, -0.1], [-0.1, -0.1]), ([0.2, -0.1], [0.4, -0.1]), ([0.4, -0.1], [0.4, -0.3]),
               ([0.4, -0.1], [0.3, -0.2]), ([0.4, -0.3], [0.3, -0.4]), ([0.2, -0.1], [0.1, -0.2])]

    hidden = [([-0.3, 0.4], [-0.2, 0.5]), ([-0.2, 0.5], [-0.2, 0.7]), ([-0.2, 0.5], [0.4, 0.5]), ([0.0, 0.5], [-0.1, 0.4]),
              ([0.2, 0.5], [0.1, 0.4]), ([0.0, 0.5], [0.0, -0.1]), ([0.2, 0.5], [0.2, 0.4]), ([-0.1, -0.1], [0.2, -0.1]),
              ([0.0, -0.1], [-0.1, -0.2]), ([-0.2, -0.1], [-0.2, -0.3]), ([-0.2, -0.3], [-0.3, -0.4]), ([-0.2, -0.3], [0.4, -0.3])]

    x0, y0 = 100, 250  # start position
    m = 400  # size of the figure
    clvis = (1, 1, 0)
    clunvis = (0, 0, 1)
    direction = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_figure(x0, y0, m, clvis, clunvis, visible, hidden, line_width=2.0)
        pygame.display.flip()

        x0 = x0 + 0.2 * direction  # move to the right
        if x0 > 650 or x0 < 100:  # return figure to the left side of the screen
            direction *= -1

if __name__ == "__main__":
    main()
