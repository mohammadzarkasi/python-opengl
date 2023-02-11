import pygame as pg
# from OpenGL.GL import * as gl
from OpenGL import GL as gl
from OpenGL.GL import shaders as shd
import numpy as np
import ctypes

class App:
    def __init__(self) -> None:

        # init pygame
        pg.init()
        pg.display.set_mode((640,480), pg.OPENGL | pg.DOUBLEBUF)

        self.clock = pg.time.Clock()

        # init open cl
        gl.glClearColor(0.1, 0.2, 0.2, 1)

        # aktifkan konfigurasi shader
        self.shader = self.create_shader()
        gl.glUseProgram(self.shader)

        # buat objek yg akan digambar
        self.tr1 = Triangle()

        self.mainLoop();

    def create_shader(self):
        vs = []
        fs = []
        with open('shaders/vertex.txt', 'r') as f:
            vs = f.readlines()
        with open('shaders/fragment.txt', 'r') as f:
            fs = f.readlines()
        
        shader = shd.compileProgram(
            shd.compileShader(vs, gl.GL_VERTEX_SHADER),
            shd.compileShader(fs, gl.GL_FRAGMENT_SHADER)
        )

        return shader

    def mainLoop(self):
        running = True
        while running == True:
            for ev in pg.event.get():
                # print('ev type', ev.type)
                if ev.type == pg.QUIT:
                    running = False
            
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            # menggambar
            gl.glUseProgram(self.shader)
            gl.glBindVertexArray(self.tr1.vao)
            gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.tr1.vertex_count)

            # 
            pg.display.flip()

            self.clock.tick(60)

        self._quit();

    def _quit(self):
        self.tr1.destroy()
        gl.glDeleteProgram(self.shader)
        pg.quit()


class Triangle:
    def __init__(self) -> None:
        # x y z, r g b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
             0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
             0.0,  0.5, 0.0, 0.0, 0.0, 1.0
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3

        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)

        self.vbo = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(1)
        gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        gl.glDeleteVertexArrays(1, (self.vao,))
        gl.glDeleteBuffers(1, (self.vbo,))

if __name__ == '__main__':
    app = App()
    

