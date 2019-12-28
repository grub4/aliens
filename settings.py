class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (200,200,150)
        self.ship_speed_factor = 7

        #子弹设置
        self.bullet_speed_factor = 8
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 255,0,0
        self.bullet_allowed = 100
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1
        self.ship_limit = 3
            
         
