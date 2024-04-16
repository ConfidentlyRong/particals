import pygame as pg
import sys
from sprites import RedPartical, Tile
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.load_data()
        self.dt = 1
        self.red_particals = {}
        self.tiles = {}
        self.p_num = -1
        self.tile_num = -1
        self.red_spawn = False
        self.windy = False

    def load_data(self):
        self.game_folder = os.path.dirname(__file__)
        self.map_data = []
        with open(os.path.join(self.game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line.strip())

    def new(self):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.tile_num += 1
                    tile = Tile(self, (col,row))
                    self.tiles.update({'i' + str(self.tile_num): tile})
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
        print(self.tiles)
        self.mpos = pg.mouse.get_pos()
        if self.red_spawn:
            self.p_num += 1
            partical = RedPartical(self, self.mpos)
            self.red_particals.update({'i' + str(self.p_num): partical})
        for partical in self.red_particals.values():
            partical.update()
        

    def draw(self):
        self.screen.fill(('black'))
        for tile in self.tiles.values():
            tile.render(self.screen)
        for partical in self.red_particals.values():
            partical.render(self.screen)
        pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.new()
