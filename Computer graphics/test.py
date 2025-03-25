import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import cv2
from flask import Flask, Response

app = Flask(__name__)

# Визначення вершин, граней та кольорів
vertices = [
    (2, 1, -0.5), (2, -1, -0.5), (-2, -1, -0.5), (-2, 1, -0.5),
    (2, 1, 0.5), (2, -1, 0.5), (-2, -1, 0.5), (-2, 1, 0.5)
]

faces = [
    (0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1),
    (3, 7, 6, 2), (0, 4, 7, 3), (1, 5, 6, 2)
]

colors = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (1, 1, 0), (1, 0, 1), (0, 1, 1)
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
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def render_frame(angle):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(angle, 1, 0, 0)
    draw_faces()
    draw_edges()
    glPopMatrix()
    
    pygame.display.flip()
    
    buffer = glReadPixels(0, 0, 800, 600, GL_RGB, GL_UNSIGNED_BYTE)
    img = np.frombuffer(buffer, dtype=np.uint8).reshape(600, 800, 3)
    img = np.flipud(img)
    return cv2.imencode('.jpg', img)[1].tobytes()

def generate_frames():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)
    glEnable(GL_DEPTH_TEST)
    angle = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        frame = render_frame(angle)
        angle += 1
        
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)