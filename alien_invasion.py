import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()
    ai_settings = Settings()    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    #窗口标题
    pygame.display.set_caption("Alien Invasion")
    
    play_button = Button(ai_settings,screen,"Play")
    ship = Ship(ai_settings,screen)
    bullets = Group()    
    aliens = Group()
   
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    print("Screen has" + ' ' + str(len(aliens)) + ' ' + "aliens")
    stats = GameStats(ai_settings)
    
    
    while True:
        gf.check_events(ai_settings,screen,ship,bullets, stats, play_button,
                        aliens)
        if (stats.game_active == True):
             
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,aliens,ship,stats,screen,bullets)
        
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,
                         stats)
        
                                 
        

run_game()
