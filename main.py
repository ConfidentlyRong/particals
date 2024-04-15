import pygame as pg
import sys
from sprites import RedPartical
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.dt = 1
        self.red_particals = {}
        self.p_num = -1
        self.red_spawn = False
        self.windy = False

    def new(self):
        self.run()

    def run(self):
        while True:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                if event.key == pg.K_w:
                    self.windy = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.windy = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.red_spawn = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.red_spawn = False
    
    def update(self):
        self.mpos = pg.mouse.get_pos()
        if self.red_spawn:
            self.p_num += 1
            partical = RedPartical(self, self.mpos)
            self.red_particals.update({'i' + str(self.p_num): partical})
        for partical in self.red_particals.values():
            partical.update()
        

    def draw(self):
        self.screen.fill(('black'))
        for partical in self.red_particals.values():
            partical.render(self.screen)
        pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.new()
