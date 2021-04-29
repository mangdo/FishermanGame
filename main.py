import pygame
import gamefunction as gf
from ship import Ship
from line import Line
from Hook import Hook
from fish import Fish
from pygame.sprite import Group #fish의 그룹처리위해
import sys
from tkinter import *
import time

def run_game():    
    screen=pygame.display.set_mode((800,700))
    pygame.display.set_caption("gamegame")
    background=pygame.image.load('img/sea.png')
    screen.blit(background,(0,0))
    ship=Ship(screen) #ship객체만듬
    line=Line(screen,ship) #line 객체만듬
    hook=Hook(screen,line)#hook객체만듬
    fishes=Group() #그룹처리
    gf.makefish1(screen,fishes) #초마다 물고기 새로만들기
    gf.makefish2(screen,fishes)#두번째 물고기
    gf.makefish3(screen,fishes)#세번째 물고기
    gf.makefish4(screen,fishes)
    gf.makeshark(screen,fishes)
    pygame.time.Clock() #pygame 진행시간계산
    
    while True:
        screen.blit(background,(0,0))
        ship.blitme() #배 screen에 띄우기
        ship.update() #배 위치 업뎃        
        fishes.update(fishes) #물고기 위치업뎃, 화면밖지나가면 없앰
        for fish in fishes.sprites():
            fish.blitme()
        line.blitme()
        line.update(ship) 
        hook.update(line)
        hook.blitme()
        t=pygame.time.get_ticks()//1000 # 진행시간을 1/1000초로 받아옴
        if (t>40):
            print("시간초과!!") #millisecond로 받아옴(1000분의 1초)
            pygame.quit() #40초가 지나면 게임종료
            sys.exit()
        gf.check_event(ship,line,fishes,hook,t) #이벤트일어날때 ship움직임처리하는 함수
        pygame.display.flip() #최신이미지로 다시 띄우기


window = Tk() 
window.title('Game Start')

def Start():
    window.destroy() #GUI를 종료시킴
    window.quit() #윈도우를 종료시킴
    run_game() #run_game 함수 호출
       
photo = PhotoImage(file = 'img/게임설명.png')
ilabel = Label(window, image =  photo) #게임 첫화면
ilabel.grid(row=0, column=0)
        
b1 = Button(window, text='Game Start!',command = Start) #게임 시작 버튼
b1.grid(row=1,column=0, columnspan=5)
