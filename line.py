import pygame
class Line():
    def __init__(self,screen,ship): #line초기값
        self.moving=False
        self.height=0
        self.screen=screen
        self.color=(60,60,60)
        self.rect=pygame.Rect(0,0,5,5+self.height)
        self.rect.centerx=ship.rect.centerx #ship과 line은 붙어다닌다.
        self.rect.centery=ship.rect.centery
        self.rect.top=ship.rect.bottom
        self.speed=5
        
    def update(self,ship): #줄 위치 업데이트
        if self.moving:
            self.height+=self.speed # 낚시줄의 스피드 조정을 위해
            self.rect.height=self.height
        if ship.moving_right or ship.moving_left: #여기추가함
            self.rect.centerx=ship.rect.centerx
    def blitme(self): # 줄 화면 띄우기
        pygame.draw.rect(self.screen,self.color,self.rect)
    def up(self): #줄올리기
        while (self.height>=0):
            self.height-=5
            self.rect.height=self.height
