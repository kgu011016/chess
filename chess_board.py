# -*- coding: utf-8 -*-
"""

team: sammaru team 4
project: Chess Game
writer: Chaerin Jung

<Chess Board Module>

"""

import pygame

pygame.init()
w = 600
h = 600
size = [600, 600]
# 실행 창의 전체 크기를 고려하지 않고 체스판의 크기만을 고려
# 8X8 체스판 이므로 한 칸의 크기는 (75,75)
WHITE = (255, 255, 255)


def Back(x, y):
    global screen, background
    screen.blit(background, (x,y))

def ChessBoard():
    
    global screen, back, background

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('ChessPlay') #게임판 타이틀 지정
    background = pygame.image.load('C:/체스판 이미지가 저장된 경로를 입력/chess_board.png')
    # 갈색/베이지로 이루어진 체스판이 체스말을 흰/검으로 구현하기 쉬울 것 같아서 해당 색으로 이미지 제작
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True # 마우스로 창을 닫으면 종료
        screen.fill(WHITE)
        Back(0, 0)
        pygame.display.update()
    
    pygame.quit() # 이 부분은 다른 함수와 합친 후엔 삭제해야될 듯

ChessBoard()