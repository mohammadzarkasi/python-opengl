import pygame as pg
# from OpenGL.GL import * as gl
from OpenGL import GL as gl


class App:
    def __init__(self) -> None:

        # init pygame
        pg.init()
        pg.display.set_mode((640,480), pg.OPENGL | pg.DOUBLEBUF)

        self.clock = pg.time.Clock()

        # init open cl
        gl.glClearColor(0.1, 0.2, 0.2, 1)

        self.mainLoop();

    def mainLoop(self):
        running = True
        while running == True:
            for ev in pg.event.get():
                # print('ev type', ev.type)
                if ev.type == pg.QUIT:
                    running = False
            
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            self.clock.tick(60)

        self._quit();

    def _quit(self):
        pg.quit()



if __name__ == '__main__':
    app = App()

