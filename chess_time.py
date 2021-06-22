import time
import threading

def TimeTikTok(sec):
    sec=60
    while(sec!=0):
        sec=sec-1
        time.sleep(1)
        #1초에 한번씩 sec-1이 되도록 하는 함수 time.sleep(1)
        blinkSec(sec)

def blinkSec(sec):
    if sec>10:      
            threading.Timer(1,print(sec)).start()
            #sec를 60초에서부터 11초까지 표시하도록 반복
    elif sec<=10:
       print('\033[5m'+str(sec)+'\033[0m')
        #sec가 10초가 되면 0까지 깜빡거리도록 함
def TurnSwitch(user):
    if user=="white":
        user="black"
    else:
        user="white"
        
while True:
    global user,sec
    sec=0
    user="white"
    #user의 기본값으로 0 설정
    TimeTikTok(sec)
    if user=="white":
        if sec==0:
            TurnSwitch(user)
            user="black"
        elif chessmove:
            #체스 말이 움직이면
            TurnSwitch(user)
            user=="black"
        
    else:
        if sec==0:
            TurnSwitch(user)
            user="white"
        elif chessmove:
            TurnSwitch(user)
            user="white"
       
        




