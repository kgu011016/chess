import pygame as p

# chess 말 파일 불러오기 >> 게임이 시작되기 전 한번만
def loadImages():
    #[ 폰 룩 나이트 비숑 킹 퀸 ] white, black 순
    pieces=['wP','wR','wN','wB','wK','wQ','bP','bR','bN','bB','bK','bQ'] 
    for piece in pieces:    
        Images[piece]=p.image.load(piece+".png") #파일경로
        #파일경로 & 사진 사이즈 설정
        #Images[piece]=p.fransform.sclae(p.image.load("파일경로/"+piece+".png"),(가로, 세로)) 

# #2차원 배열로 구현한 board     
# board=[
#        ['bR','bN','bB','bQ','bK','bB','bN','bR'],
#        ['bP','bP','bP','bP','bP','bP','bP','bP'],
#        ['--','--','--','--','--','--','--','--'],
#        ['--','--','--','--','--','--','--','--'],
#        ['--','--','--','--','--','--','--','--'],
#        ['--','--','--','--','--','--','--','--'],
#        ['wP','wP','wP','wP','wP','wP','wP','wP'],
#        ['wR','wN','wB','wQ','wK','wB','wN','wR']]

        
class Piece: 
    def __init__(self, color, name):    #color: w/b   name: R N B Q K P (대문자)
        self.color = color
        self.name = name
        self.image = loadImages().Images[color+name]
        self.direction =direction        
        
class King(Piece):
    def __init__(self, color):
        self.direction = -1 if color == 'w' else 1
        #self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}
        super().__init__(color, 'K', unbounded=False)
    
    # #움직일 수 있는 반경 : 주위 1칸 & king은 공격 할 수 있는 칸으로 이동 불가
    # def can_move(x,y):   #현재 위치 x y  
    #    (x-1,y-1), (x,y-1), (x+1,y-1)
    #    (x-1,y),            (x+1,y)
    #    (x-1,y+1), (x,y+1), (x+1,y+1)
           
    def can_kill():
        pass
        
        
    #체크메이트 구현
    def check_mate():
        pass
        

class Queen(Piece):
    def __init__(self, color):
        self.direction = -1 if color == 'w' else 1
        #self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}
        super().__init__(color, 'Q')
        
    #움직일 수 있는 반경 & 기물 뛰어넘기 안됨
    def can_move():
        cross = [[[x + i, y] for i in range(1, 8 - x)],  #직선방향 오른쪽
             [[x - i, y] for i in range(1, x + 1)],      #직선방향 왼쪽
             [[x, y + i] for i in range(1, 8 - y)],      #직선방향 아래쪽
             [[x, y - i] for i in range(1, y + 1)]]      #직선방향 위쪽
        diagonals = [[[x + i, y + i] for i in range(1, 8-y)],   #오른쪽 아래 대각선 방향
             [[x + i, y - i] for i in range(1, y+1)],           #오른쪽 위 대각선 방향
             [[x - i, y + i] for i in range(1, x+1)],            #왼쪽 아래 대각선 방향
             [[x - i, y - i] for i in range(1, x+1)]]           #왼쪽 위 대각선 방향
        
    def can_kill():
        pass


class Rook(Piece):
    def __init__(self, color):
        self.direction = -1 if colour == 'w' else 1
        #self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x == 0 or y == 0) and (x != 0 or y != 0)}
        super().__init__(color, 'R')

    #움직일 수 있는 반경 & 기물 뛰어넘기 안됨
    def can_move():    
        cross = [[[x + i, y] for i in range(1, 8 - x)],  #직선방향 오른쪽
             [[x - i, y] for i in range(1, x + 1)],      #직선방향 왼쪽
             [[x, y + i] for i in range(1, 8 - y)],      #직선방향 아래쪽
             [[x, y - i] for i in range(1, y + 1)]]      #직선방향 위쪽
        
    def can_kill():
        pass

class Bishop(Piece):
    def __init__(self, color):
        self.direction = -1 if colour == 'w' else 1
        #self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 and y != 0}
        super().__init__(color, 'B')

    #움직일 수 있는 반경 & 기물 뛰어넘기 안됨
    def can_move(): 
        diagonals = [[[x + i, y + i] for i in range(1, 8-y)],    #오른쪽 아래 대각선 방향
             [[x + i, y - i] for i in range(1, y+1)],           #오른쪽 위 대각선 방향
             [[x - i, y + i] for i in range(1, x+1)],            #왼쪽 아래 대각선 방향
             [[x - i, y - i] for i in range(1, x+1)]]           #왼쪽 위 대각선 방향
        
    def can_kill():
        pass

class Knight(Piece):
    def __init__(self, color):
        self.direction = -1 if colour == 'w' else 1
        #self.moveset = {(x, y) for x in range(-2, 3) for y in range(-2, 3) if x != 0 and y != 0 and abs(x) != abs(y)}
        super().__init__(colour, 'N')
    
    #움직일 수 있는 반경
    def can_move():    
        # for i in [-2,-1,1,2]:
        #     for j in [-2,-1,1,2]:
        #         [[x+i],[y+j]]
        pass
        
    def can_kill():
        pass

class Pawn(Piece):
    def __init__(self, color):
        self.direction = -1 if colour == 'w' else 1
        #self.moveset = {(0, y * self.direction) for y in range(1, 2)}
        self.double_move =1  #폰이 처음 움직일 때 2칸 이동 가능 > 움직이고 나서 0
        super().__init__(color, 'P')
        
    #움직일 수 있는 반경 & 기물 뛰어넘기 안됨
    def can_move():  
        # if self.double_move==1:
        #     (x+1,y) || (x+2,y)
        #     double_move=0   #처음으로 움직인 후 0
        #else: 
         #   (x+1,y)
        pass
        
    #앞 방향 대각선으로만 공격가능
    def can_kill():
        pass
    #def promotion()    폰이 맨 끝 칸까지 간다면 승진 가능 >> 퀸, 룩, 비숍, 나이트
    #def ep()    앙파상 적의 폰이 2칸 이동하는 도중 1칸 밖에 움직이지 않은 것처럼 잡는 폰의 이동
        

    
