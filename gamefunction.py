import pygame
import random
import sys
from fish import *
import time
import threading
from Hook import Hook

result=0 # 지금까지 잡은 물고기의 총무게를 저장할 전역변수
"""이벤트를 감지할 함수"""
def check_event(ship,line,fishes,hook,t):
    global result # 전역변수 사용
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창닫기 눌렀을때
            pygame.quit()
            sys.exit()
            
        elif event.type==pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key == pygame.K_LEFT:
                ship.moving_left=True
            elif event.key ==pygame.K_SPACE:
                line.moving=True
                
        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key == pygame.K_LEFT:
                ship.moving_left=False
            elif event.key ==pygame.K_SPACE: #스페이스를 눌렀을 때
                line.moving=False
                if pygame.sprite.spritecollideany(hook,fishes): #hook이랑 fishes라는 그룹이 충돌했다면
                    a=pygame.sprite.spritecollideany(hook,fishes) #충돌한 fishes그룹중 무슨 fish멤버가 충돌했는지 반환
                    fishes.remove(a) #그 잡힌 fish멤버를 없애준다.
                    a.nameing() #잡힌 fish멤버의 설명 띄어주는 함수
                    result+=a.weight #잡힌 물고기 무게를 더한다.
                    print("남은 시간은 ",40-t,"초")
                    print("현재까지 잡은 물고기의 총무게 : ",result,"kg") #총무게 띄어주기
                    if(result>=20): #총무게 20이상이면
                        print("승리!!!!!")
                        pygame.quit() #게임 끝내기
                        sys.exit()
                    elif(result>10): #10kg이상으로 잡으면
                        line.speed=10 #낚시줄의 속도를 빠르게 해서 타이밍 힘들게!
                line.up() #스페이스떼면 낚시줄 올리기

"""물고기를 랜덤하게 만들어낸 함수들"""
def makefish1(screen,fishes):
    def test1():
        p=1
        while p:
            time.sleep(3)#3초에 한번씩 while문 돌아가기
            new_fish=random.choice([Fish(screen,p),Fish6(screen,p)])
            # 새로운 물고기는 Fish와 Fish6중에 랜덤으로 나온다.
            fishes.add(new_fish) #새로운 물고기 출현
    t1=threading.Thread(target=test1) 
    t1.start()
    
def makefish2(screen,fishes):
    def test2():
        p=1
        while p:
            time.sleep(4) #4초에 한번씩 while문 돌아감
            new_fish=random.choice([Fish2(screen,p),Fish5(screen,p)])
            fishes.add(new_fish)
    t2=threading.Thread(target=test2)
    t2.start()

def makefish3(screen,fishes):
    def test3():
        p=1
        while p:
            time.sleep(5) #5초에 한번씩 while문 돌아감
            new_fish=random.choice([Fish3(screen,p),Fish4(screen,p)])
            fishes.add(new_fish)
    t3=threading.Thread(target=test3)
    t3.start()

def makefish4(screen,fishes):
    def test4():
        p=1
        while p:
            time.sleep(6) #6초에 한번씩 while문 돌아감
            new_fish=random.choice([Fish(screen,p),Fish4(screen,p)])
            fishes.add(new_fish)
    t4=threading.Thread(target=test4)
    t4.start()
    
def makeshark(screen,fishes):
    def test5():
        num=random.randint(3,20) #num은 3에서 20사이에 정수중 랜덤하게 선택됨
        a = int(num) #a는 num의 정수형 변수 
        time.sleep(a) #a초가 지나면 함수가 돌아간다. 
        new_fish=Shark(screen) 
        fishes.add(new_fish)
    t5=threading.Thread(target=test5)
    t5.start()
