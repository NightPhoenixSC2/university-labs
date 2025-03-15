import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

    A = (20, 300)
    B = (400, 75)
    C = (770, 300)
    D = (400, 570)
    path = [A, B, C, D]

    current_index = 0
    next_index = 1
    t = 0
    speed = 0.007

    clvis = random_color()
    clunvis = random_color()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current_pos = path[current_index]
        next_pos = path[next_index]

        x0 = (1 - t) * current_pos[0] + t * next_pos[0]
        y0 = (1 - t) * current_pos[1] + t * next_pos[1]

        if current_pos == A and next_pos == B:
            m = 100 + t * 100   # A(100) -> B(200)
        elif current_pos == B and next_pos == C:
            m = 200 - t * 100   # B(200) -> C(100)
        elif current_pos == C and next_pos == D:
            m = 100 - t * 50    # C(100) -> D(50)
        elif current_pos == D and next_pos == A:
            m = 50 + t * 50     # D(50) -> A(100)
        else:
            m = 100

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_figure(x0, y0, m, clvis, clunvis, visible, hidden)
        draw_center_point()
        pygame.display.flip()
        pygame.time.wait(10)

        t += speed
        if t >= 1:
            t = 0
            current_index = next_index
            next_index = (next_index + 1) % len(path)

if __name__ == "__main__":
    main()
