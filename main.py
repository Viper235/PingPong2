import pygame as pg
from setings import *
from player import Player
from ball import Ball 

class Game():

    def __init__(self):
        #Запускаем движок Pygame
        pg.init()
        self.window = pg.display.set_mode((W_WIDTH, W_HIGHT))
        self.new_game()

    def new_game(self):
        '''
        Метод отвечает за запуск новой игры
        '''
        #Переменная игрового цикла
        self.run_game = True
        self.clock = pg.time.Clock()
        self.bg = pg.transform.scale(pg.image.load('bg.jpg'), (W_WIDTH, W_HIGHT))
        
        self.playerL = Player(self,'left-block.png',[0,W_HIGHT // 2], (P_WIDTH, P_HIGHT),PLAYER_SPEED, DirButtons(pg.K_w, pg.K_s))
        self.playerR = Player(self,'right-block.png',[W_WIDTH - P_WIDTH, W_HIGHT // 2], (P_WIDTH, P_HIGHT),PLAYER_SPEED, DirButtons(pg.K_UP, pg.K_DOWN))

        self.ball = Ball(self, 'ball.png', (W_WIDTH // 2, W_HIGHT // 2), size=(50,50))

    def update(self):
        '''
        Меняем положение спрайтов
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run_game = False 
        self.playerL.update()
        self.playerR.update()
        pg.display.update()
        
    def draw(self):
        '''
        Отрисовываем спрайты в окне
        '''
        self.window.blit(self.bg, (0,0))
        self.playerL.draw()
        self.playerR.draw()
        


    def run(self):
        '''
        Запуск игрового цикла 
        '''
        while self.run_game:
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
    