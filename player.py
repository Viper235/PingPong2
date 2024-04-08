import pygame as pg
from game_spr import GameSprite
from setings import *

class Player(GameSprite):
    '''Класс игрока-платформы'''
    def __init__(self, game, image_path: str, pos: tuple[int, int], size: tuple[int, int], speed: float, buttons: DirButtons) -> None:
        super().__init__(game, image_path, pos, size, speed)
        self.buttons = buttons

    def update(self) -> None:
        keys = pg.key.get_pressed()
        #Верхний обработчик
        if keys[self.buttons.up] and self.rect.y > 0:
            self.rect.y -= self.speed
        #Нижний обработчик 
        if keys[self.buttons.down] and self.rect.bottom < W_HIGHT:
            self.rect.y += self.speed