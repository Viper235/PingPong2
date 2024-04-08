import pygame as pg
from setings import *

class GameSprite(pg.sprite.Sprite):
    def __init__(
            self,
            game,
            image_path: str,
            pos: tuple[int,int],#можно не писать tuple
            size: tuple[int,int],
            speed: float
            ) -> None:
        super().__init__()
        self.game = game
        self.image = pg.transform.scale(pg.image.load(image_path), size=size).convert_alpha()
        self.size = size
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


    def draw(self):
        self.game.window.blit(self.image, (self.rect.x, self.rect.y))