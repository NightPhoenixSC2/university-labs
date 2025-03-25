import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import cv2
from flask import Flask, Response

# Ініціалізація Pygame та OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)
glEnable(GL_DEPTH_TEST)

# Куб
vertices = [
    (2, 1, -0.5), (2, -1, -0.5), (-2, -1, -0.5), (-2, 1, -0.5),
    (2, 1, 0.5), (2, -1, 0.5), (-2, -1, 0.5), (-2, 1, 0.5)
]
faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (3, 7, 6, 2), (0, 4, 7, 3), (1, 5, 6, 2)]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(pygame.time.get_ticks() / 10 % 360, 1, 1, 0)
    
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glPopMatrix()
    pygame.display.flip()

# Flask сервер для стрімінгу відео
app = Flask(__name__)

def generate_frames():
    while True:
        draw()
        width, height = display
        pixels = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
        frame = np.frombuffer(pixels, dtype=np.uint8).reshape(height, width, 3)
        frame = cv2.flip(frame, 0)  # Віддзеркалення OpenGL
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
