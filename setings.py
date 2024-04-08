from dataclasses import dataclass

FPS = 60
W_WIDTH = 1200
W_HIGHT = 720

P_WIDTH = 20
P_HIGHT = 130

PLAYER_SPEED = 5
BALL_SPEED = 1

@dataclass
class DirButtons:
    up:int
    down:int

