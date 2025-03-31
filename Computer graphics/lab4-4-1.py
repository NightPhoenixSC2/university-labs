import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

scale = [0.2, 0.2, 0.2]  # Масштабні коефіцієнти [X, Y, Z]
translation_coefficient = (0.25, 0.25, -2.0)  # Коефіцієнт зміщення (x, y, z)
rotation_angle = 20  # кут обертання
rotation_axis = [1, 1, 1]  # Вісь обертання (X, Y, Z)

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

faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 4, 5, 1),
    (3, 7, 6, 2),
    (0, 4, 7, 3),
    (1, 5, 6, 2)
]

colors = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


def draw_faces():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i % len(colors)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_edges():
    glColor3f(0, 0, 0)  # чорні ребра
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Задання матриці проєкції

    glTranslatef(*translation_coefficient)  # Використання матриці перенесення (зсуву)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()  # Збереження поточної матриці перетворень
        glScalef(*scale)  # Використання матриці масштабування
        glRotatef(rotation_angle, *rotation_axis)  # Фіксований кут обертання
        draw_faces()
        draw_edges()
        glPopMatrix()  # Відновлення матриці після перетворень

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
