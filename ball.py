from game_spr import GameSprite
from math import sin,cos

class Ball(GameSprite):
    angle: float = 0.3

    def update(self):
        #умножаем скорость на косинус угла
        self.rect.x += self.speed * cos(self.angle)
        self.rect.y += self.speed * sin(self.angle)
        