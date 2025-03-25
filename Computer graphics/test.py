import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from flask import Flask, send_file
from io import BytesIO

app = Flask(__name__)

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
    (0, 1, 2, 3),  # Задня
    (4, 5, 6, 7),  # Передня
    (0, 4, 5, 1),  # Права
    (3, 7, 6, 2),  # Ліва
    (0, 4, 7, 3),  # Верхня
    (1, 5, 6, 2)   # Нижня
]

colors = [
    (1, 0, 0),  # Червоний
    (0, 1, 0),  # Зелений
    (0, 0, 1),  # Синій
    (1, 1, 0),  # Жовтий
    (1, 0, 1),  # Фіолетовий
    (0, 1, 1),  # Блакитний
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
    for edge in [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def capture_screen():
    # Отримуємо поточний кадр в буфер
    width, height = 800, 600
    glReadBuffer(GL_FRONT)
    raw_data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    
    # Перетворюємо дані в зображення
    image = np.frombuffer(raw_data, dtype=np.uint8).reshape((height, width, 3))
    image = np.flipud(image)  # Перевертаємо по вертикалі, бо OpenGL зчитує знизу вгору
    
    return image

@app.route('/')
def render_cube():
    # Ініціалізація Pygame і OpenGL
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    glEnable(GL_DEPTH_TEST)

    # Очищаємо екран і рендеримо куб
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_faces()
    draw_edges()

    # Захоплюємо екран у вигляді зображення
    image = capture_screen()

    # Перетворюємо в зображення у форматі PNG
    buffer = BytesIO()
    pygame.image.save(pygame.surfarray.make_surface(image), buffer)
    buffer.seek(0)

    # Повертаємо зображення через Flask
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
