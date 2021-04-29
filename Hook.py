import pygame

class Hook():
    def __init__(self,screen,line): #hook 초기값
        self.screen=screen
        self.image=pygame.image.load("img/hook.png")
        self.rect=self.image.get_rect()
        self.rect.centerx = line.rect.centerx#hook와 line은 붙어다닌다.
        self.rect.top=line.rect.bottom
        
    def update(self,line):
        self.rect.centerx = line.rect.centerx
        self.rect.top=line.rect.bottom
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
