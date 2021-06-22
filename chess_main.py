
import pygame
from pygame import freetype

pygame.init()

BACKGROUND_COLOR = (192, 192, 192)
BOARD1 =  (255, 206, 158)# 밝은 색
BOARD2 = (209, 139, 71) # 어두운 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
score_white, score_black = 0, 0
game_count, game_count_temp = 0, 0

# 폰트 지정
freetype.init()
chess_font = freetype.Font(None, 50)
score_font = pygame.font.Font(None, 100)
turn_font = pygame.font.Font(None, 80)

# 보드판 그리기 (중심 좌표 : 30 + a) # pygame.draw.circle(screen, BLACK, (90, 90), 5)
def show_board(screen, font, flipped):
    select_color = {True: BOARD1, False: BOARD2}
    cur_color = True
    for row in range(8):
        for square in range(8):
            pygame.draw.rect(screen, select_color[cur_color], ((60 + (square * 60)), 60 + (row * 60), 60, 60))
            cur_color = not cur_color
        cur_color = not cur_color

    pygame.draw.rect(screen, BLACK, (560, 60, 320, 160), 4)
    pygame.draw.rect(screen, GRAY, (560, 240, 320, 120), 4)
    pygame.draw.rect(screen, WHITE, (560, 380, 320, 160), 4)

    for row in range(8):
        if flipped:
            font.render_to(screen, (15, 70 + (row * 60)), chr(49 + row))
        else:
            font.render_to(screen, (15, 70 + (row * 60)), chr(56 - row))
    for col in range(8):
        if flipped:
            font.render_to(screen, (72 + (col * 60), 550), chr(72 - col))
        else:
            font.render_to(screen, (72 + (col * 60), 550), chr(65 + col))

    font.render_to(screen, (145, 12), "Chess Board")

# 점수 명시
def show_score(screen, font, turn=""):
    global score_white, score_black, game_count, game_count_temp

    if game_count != game_count_temp:
        score_show_black = score_font.render(str(score_black), True, BLACK)
        score_show_white = score_font.render(str(score_white), True, WHITE)
        score_show_colon = score_font.render(':', True, GRAY)
        screen.blit(score_show_black, (650, 270))
        screen.blit(score_show_white, (750, 270))
        screen.blit(score_show_colon, (710, 265))
    else: # 제대로 구현하려면 checkmate 함수 필요
        if turn == "White":
            score_white += 1
            score_show_black = score_font.render(str(score_black), True, BLACK)
            score_show_white = score_font.render(str(score_white), True, WHITE)
            score_show_colon = score_font.render(':', True, GRAY)
            screen.blit(score_show_black, (650, 270))
            screen.blit(score_show_white, (750, 270))
            screen.blit(score_show_colon, (710, 265))
            game_count_temp += 1
        elif turn == "Black":
            score_show_black = score_font.render(str(score_black), True, BLACK)
            score_show_white = score_font.render(str(score_white), True, WHITE)
            score_show_colon = score_font.render(':', True, GRAY)
            screen.blit(score_show_black, (650, 270))
            screen.blit(score_show_white, (750, 270))
            screen.blit(score_show_colon, (710, 265))
            game_count_temp += 1
        else:
            score_show_black = score_font.render(str(score_black), True, BLACK)
            score_show_white = score_font.render(str(score_white), True, WHITE)
            score_show_colon = score_font.render(':', True, GRAY)
            screen.blit(score_show_black, (650, 270))
            screen.blit(score_show_white, (750, 270))
            screen.blit(score_show_colon, (710, 265))

# 누구의 턴인지 명시
def show_turn(screen, font, turn="White"):
    if turn == "Black": # 검은색 턴
        score_turn = turn_font.render("Your turn!", True, BLACK)
        screen.blit(score_turn, (587, 120))
    elif turn == "White":
        score_turn = turn_font.render("Your turn!", True, WHITE)
        screen.blit(score_turn, (587, 440))

# 체크메이트
def checkmate(screen, font, turn, ):
    pass

def main():
    flipped = False

    # 화면 설정
    screen_width = 900
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 게임 이름
    pygame.display.set_caption("체스게임")

    # 게임 시작
    running = True 
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # 스페이스 바 누르면 뒤집음
                    flipped = not flipped
        
        # 기본적인 정보 표시
        screen.fill(BACKGROUND_COLOR)
        show_board(screen, chess_font, flipped)
        show_score(screen, score_font)
        show_turn(screen, score_font)

        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()
    
    
    
    