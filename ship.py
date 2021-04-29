import pygame
class Ship():
    def __init__(self,screen): # 배 초기값
        self.screen=screen
        self.image=pygame.image.load('img/ship1.png')
        self.rect=self.image.get_rect() #pygame에서는 rect로 객체를 조정함
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=int(130) #배를 수평선위에 위치시킴
        self.moving_right=False
        self.moving_left=False
        
    def update(self): #배 위치 업뎃
        if self.moving_right:
            self.rect.centerx+=10
        elif self.moving_left:
            self.rect.centerx-=10
    def blitme(self): # 배를 스크린에 띄우기
        self.screen.blit(self.image,self.rect)
