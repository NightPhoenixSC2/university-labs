import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import cv2
from flask import Flask, Response

# Фігура
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

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Функція малювання граней
def draw_faces():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i % len(colors)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# Функція малювання ребер
def draw_edges():
    glColor3f(0, 0, 0)  # Чорні ребра
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Налаштування Pygame та OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)

glEnable(GL_DEPTH_TEST)

# Flask додаток
app = Flask(__name__)

# Відео потік для Flask
def generate_frames():
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Очищення екрану
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Обертання та малювання фігури
        glPushMatrix()
        glRotatef(angle, 1, 0, 0)  # обертання по осі X
        draw_faces()
        draw_edges()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
        angle += 1

        # Захоплення кадру
        pixels = glReadPixels(0, 0, display[0], display[1], GL_RGB, GL_UNSIGNED_BYTE)
        frame = np.frombuffer(pixels, dtype=np.uint8).reshape(display[1], display[0], 3)
        frame = cv2.flip(frame, 0)  # Виправлення орієнтації

        # Перетворення у формат MJPEG
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n\r\n')

# Маршрут для відео потоку
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Запуск Flask серверу
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
