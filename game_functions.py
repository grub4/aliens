import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,bullets, stats, play_button,aliens):
     for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                 if len(bullets)< ai_settings.bullet_allowed:
                      new_bullet = Bullet(ai_settings,screen,ship)
                      bullets.add(new_bullet)
                 #发射子弹时同时打印子弹数量
                 print(len(bullets)-1)
            elif event.key == pygame.K_q:
                 pygame.quit()
                 sys.exit()
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x,mouse_y = pygame.mouse.get_pos()
             check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y,aliens,
                       bullets, ship)

def check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y,aliens,
                      bullets, ship ):
     if play_button.rect.collidepoint(mouse_x, mouse_y):
          stats.reset_stats()
          stats.game_active = True

          aliens.empty()
          bullets.empty()

          create_fleet(ai_settings,screen, ship, aliens)
          ship.center_ship()
                

def create_fleet(ai_settings,screen,ship,aliens):
     """创建外星人群"""
     alien = Alien(ai_settings,screen)
     number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
     number_rows = get_number_rows(ai_settings,ship.rect.height,
                                   alien.rect.height)
     #创建一行外星人/创建外星人群
     for row_number in range(number_rows):
          for alien_number in range(number_aliens_x  ):
               create_alien(ai_settings,screen,aliens,alien_number,
                            row_number)

def get_number_aliens_x(ai_settings,alien_width):
     """计算每行容纳多少个外星人"""
     avilable_space_x = ai_settings.screen_width - 2*alien_width
     number_aliens_x = int(avilable_space_x / (2 * alien_width))
     return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
     """创建外星人并将它放在当前行"""
     alien = Alien(ai_settings,screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2 * alien_width * alien_number
     alien.y = alien.rect.height + 2 * alien.rect.height * row_number
     alien.rect.x = alien.x
     alien.rect.y = alien.y
     aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
     """计算屏幕可容纳外星人的行数"""
     avilable_space_y = (ai_settings.screen_height -
                         (2 * alien_height) - ship_height)
     number_rows = int(avilable_space_y/(2 * alien_height))
     return number_rows

def update_aliens(ai_settings,aliens,ship,stats,screen,bullets):
     """更新外星人的位置"""
     check_fleet_edge(ai_settings,aliens)
     aliens.update()
     #检测外星人和飞船之间碰撞
     if pygame.sprite.spritecollideany(ship,aliens):
          ship_hit(ai_settings,stats,screen,ship,aliens,bullets)                
     check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
                 
def update_screen(ai_settings,screen,ship,aliens,bullets,
                  play_button,stats):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():          
          bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen) 
    
    if not stats.game_active:
         play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
     
     bullets.update()     
     for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
     check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
     
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
     """相应子弹和外星人碰撞"""
     collision = pygame.sprite.groupcollide(bullets,aliens,True,True)
     if len(aliens) == 0:
          #删除现有子弹,重建一组外星人
          bullets.empty()
          create_fleet(ai_settings,screen,ship,aliens)
         

def check_fleet_edge(ai_settings,aliens):
     for alien in aliens.sprites():
          if alien.check_edge():
               change_fleet_direction(ai_settings,aliens)
               break

def change_fleet_direction(ai_settings,aliens):
     for alien in aliens.sprites():
          alien.rect.y += ai_settings.fleet_drop_speed
     ai_settings.fleet_direction *= -1
     
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
     """响应飞船被撞"""
     if stats.ship_left > 0:
          stats.ship_left -= 1

          #
          aliens.empty()
          bullets.empty()
          
          #
          create_fleet(ai_settings,screen,ship,aliens)
          ship.center = ship.screen_rect.centerx

          #暂停
          sleep(0.5)
     else:
          stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
     """"""
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
          if alien.rect.bottom >= screen_rect.bottom:
               ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
               break
          

          
