#이 클래스는 shipclass와 유사하다.
import pygame
from pygame.sprite import Sprite
import random

class Fish(Sprite):
    """첫번째 물고기 하나를 표현하는 클래스"""
    
    def __init__(self, screen,p):
        """물고기를 초기화하고 시작 위치를 지정한다"""
        super(Fish, self).__init__()
        self.screen = screen

        #물고기 이미지를 불러오고 이 이미지를 rect 속성으로 설정한다
        self.image = pygame.image.load('img/fish4.png')
        self.rect = self.image.get_rect()
        try:
            self.screen_rect = screen.get_rect()
        except:
            p=0
        
        #물고기는 화면 왼쪽에서 나옵니다.
        self.x = float(self.rect.x)
        self.rect.y = random.randint(250,450) #이 물고기는 y좌표 250부터 450사이에서 나옵니다
        self.speed_factor = 11
        self.name=("현재잡은 물고기는 2.5kg에요 (게임 상)\n 이름: 꽁치, 꽁치는 봄이 되면 동해안에서 떼를 지어 산란하고 동해와 남해, 북태평양에 서식해요!|\n") #물고기 설명
        self.weight=2.5 #물고기 무게
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes): #물고기 위치 업데이트
        """물고기를 오른쪽으로 움직이고 화면밖을 지나가면 없애버림"""
        self.x += self.speed_factor
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)
        
    def blitme(self): #물고기를 스크린에 띄우기
        self.screen.blit(self.image, self.rect)
        

class Fish2(Sprite):
    """두번째 물고기를 표현하는 클래스"""
    
    def __init__(self, screen,p):
        super(Fish2, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/fish2.png')
        self.rect = self.image.get_rect()
        try:
            self.screen_rect = screen.get_rect()
        except:
            p=0
        self.x = float(self.rect.x)
        self.rect.y = random.randint(320,520)
        self.speed_factor = 8
        self.name=("현재잡은 물고기는 2kg에요 (게임 상)\n이름: 아귀, 아귀는 주로 태평양과 인도양에서 서식하며 물고기와 오징어를 먹어요!\n")
        self.weight=2
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes):
        self.x += self.speed_factor
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
class Fish3(Sprite):
    def __init__(self, screen,p):
        super(Fish3, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/fish3.png')
        self.rect = self.image.get_rect()
        try:
            self.screen_rect = screen.get_rect()
        except:
            p=0
        self.x = float(self.rect.x)
        self.rect.y = random.randint(400,600)
        self.speed_factor = 8
        self.name=("현재잡은 물고기는 3.5kg에요 (게임 상)\n이름: 홍가자미, 홍가자미는 일본 북부 캄차카반도까지 서식하며 갑각류를 먹어요!\n")
        self.weight=3.5
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes): 
        self.x += self.speed_factor

        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)
    def blitme(self): 
        self.screen.blit(self.image, self.rect)
   
class Fish4(Sprite):
    
    def __init__(self, screen,p):
        super(Fish4, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/fish_1.png')
        self.rect = self.image.get_rect()
        try:
            self.screen_rect = screen.get_rect()
        except:
            p=0
        self.x = float(self.rect.x)
        self.rect.y = random.randint(460,620)
        self.speed_factor = 6
        self.name=("현재잡은 물고기는 1.5kg에요 (게임 상)\n이름: 고등어, 태평양, 고등어는 대서양에서 주로 서식하고 오징어,작은 어류를 주로 먹어요!\n")
        self.weight=1.5
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes): 
        self.x += self.speed_factor
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Fish5(Sprite):    
    def __init__(self, screen,p):
        super(Fish5, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/fish5.png')
        self.rect = self.image.get_rect()
        try:
            self.screen_rect = screen.get_rect()
        except:
            p=0
        self.x = float(self.rect.x)
        self.rect.y = random.randint(300,450)
        self.speed_factor = 5
        self.name=("현재잡은 물고기는 4kg에요 (게임 상)\n광어(넙치), 광어는 바다의 바닥에 붙어서 살고 바닥에 따라 몸의 무늬가 바뀌어요!\n")
        self.weight=3.5
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes):
        self.x += self.speed_factor
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)

    def blitme(self): 
        self.screen.blit(self.image, self.rect)

class Fish6(Sprite):    
    def __init__(self, screen,p):
        super(Fish6, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('img/fish6.png')
        self.rect = self.image.get_rect()
        try:
            self.screen_rect = screen.get_rect()
        except:
            p=0
        
        #물고기는 화면 왼쪽에서 나옵니다.
        self.x = float(self.rect.x)
        self.rect.y = random.randint(350,550)
        self.speed_factor = 12
        self.name=("현재잡은 물고기는 1kg에요 (게임 상)\n이름: 망상어,망상어는 알을 품어 그 새끼가 알에서 나오면새끼를 낳아요!\n")
        self.weight=1
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes): #물고기 위치 업데이트
        self.x += self.speed_factor
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)               

    def blitme(self): #물고기를 스크린에 띄우기
        self.screen.blit(self.image, self.rect)
        
class Shark(Sprite):
    """아기상어를 표현하는 클래스"""
    
    def __init__(self, screen):
        """상어를 초기화하고 시작 위치를 지정한다"""
        super(Shark, self).__init__()
        self.screen = screen

        #상어 이미지를 불러오고 이 이미지를 rect 속성으로 설정한다
        self.image = pygame.image.load('img/Shark.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #상어는 다른물고기와 다르게 화면 오른쪽에서 나옵니다.
        self.x = float(800-(self.rect.x)) 
        self.rect.y = random.randint(250,550)
        self.speed_factor = 18
        self.name=("이름:백상아리, 백상아리는 무시무시한 바다의 포식자에요!\n")
        self.weight=21 #상어를 잡으면 게임종료
        
    def nameing(self):
        print(self.name)
        
    def update(self,fishes): #상어 위치 업데이트
        """물고기를 오른쪽으로 움직이고 화면밖을 지나가면 없애버림"""
        self.x -= self.speed_factor 
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.right<=0:  
                fishes.remove(fish) 
                
    def blitme(self): #상어를 스크린에 띄우기
        self.screen.blit(self.image, self.rect)
        
