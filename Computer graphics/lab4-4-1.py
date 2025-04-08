import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

scale = [0.2, 0.2, 0.2]
base_translation = [0.25, 0.25, -2.0]
rotation_angle = 20
rotation_axis = [1, 1, 1]

direction_mask = (1, 1, 0)

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


def apply_directional_translation(base, mask):
    return [(-base[i] if mask[i] else base[i]) for i in range(3)]


def draw_faces():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i % len(colors)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_edges():
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    translation = apply_directional_translation(base_translation, direction_mask)
    glTranslatef(*translation)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glScalef(*scale)
        glRotatef(rotation_angle, *rotation_axis)
        draw_faces()
        draw_edges()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()