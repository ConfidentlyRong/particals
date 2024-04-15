import pygame as pg
import random
from settings import *
vec = pg.math.Vector2

class RedPartical:
    def __init__(self, game, pos):
        self.game = game
        self.mass = random.choice([8,7,5, 3, 4, 2])
        self.image = pg.Surface(((10 * self.mass),(10 * self.mass)))
        self.image.fill(('red'))
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.rect.center = self.pos
        self.gravity = vec(0,0.009)
        self.wind = vec(0.009, 0)
        self.c = 0.0001

    def kinetic_friction(self):
        friction = self.vel.copy()
        friction *= -1
        if friction[0] != 0 and friction[1] != 0:
            friction.normalize()
        friction *= self.c
        return friction

    def apply_force(self, vec_force):
        f = vec_force.copy()
        f = (f / self.mass)
        self.acc += f

    def update(self):
        if self.game.windy:
            self.apply_force(self.wind)
        self.apply_force(self.gravity)
        self.apply_force(self.kinetic_friction())
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if self.pos[0] > WIDTH:
            self.vel[0] *= -1
        if self.pos[0] < 0:
            self.vel[0] *= -1
        if self.pos[1] > HEIGHT:
            self.vel[1] *= -1
        if self.pos[1] < 0:
            self.vel[1] *= -1
        self.acc *= 0


    def render(self, surf):
        surf.blit(self.image, (self.rect.x, self.rect.y))