import pygame as pg
import os
pg.init()

os.environ["SDL_VIDEO_CENTERED"] = '1'
screen_info = pg.display.Info()

# WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
WIDTH, HEIGHT = 500,600
FPS = 60