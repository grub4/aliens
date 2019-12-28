import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        #左右移动都是1，可以让同时按下左右键时候飞船静止不动
        if self.moving_right:
            if self.rect.centerx < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            #self.rect.centerx += 1
        if self.moving_left:
            if self.rect.centerx > self.screen_rect.left:
                self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -= 1
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def center_ship(self):

        self.center = self.screen_rect.centerx
        
