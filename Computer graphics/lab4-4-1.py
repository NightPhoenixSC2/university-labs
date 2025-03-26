import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def scale_vertices(vertices, scale_factor):
    return [(x * scale_factor, y * scale_factor, z * scale_factor) for x, y, z in vertices]


scale_factor = 0.2  # Масштабний коефіцієнт
translation_coefficient = (0, 0, -2.0)  # Коефіцієнт зміщення (x, y, z)
rotation_angle = 0  # Кут обертання

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

vertices = scale_vertices(vertices, scale_factor)

faces = [
    (0, 1, 2, 3),  # Задня
    (4, 5, 6, 7),  # Передня
    (0, 4, 5, 1),  # Права
    (3, 7, 6, 2),  # Ліва
    (0, 4, 7, 3),  # Верхня
    (1, 5, 6, 2)  # Нижня
]

colors = [
    (1, 0, 0),  # Червоний
    (0, 1, 0),  # Зелений
    (0, 0, 1),  # Синій
    (1, 1, 0),  # Жовтий
    (1, 0, 1),  # Фіолетовий
    (0, 1, 1),  # Блакитний
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
    global rotation_angle
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(*translation_coefficient)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(rotation_angle, 0, 1, 0)  # Обертання навколо осі Y
        draw_faces()
        draw_edges()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
        rotation_angle += 1  # Збільшення кута обертання


if __name__ == "__main__":
    main()