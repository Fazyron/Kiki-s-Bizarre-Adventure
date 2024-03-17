import pygame as pg
from sys import exit
from random import randint, choice
import random
import math


def display_timer():
    current_time = int(pg.time.get_ticks()/1000) - start_time
    timer_surf = font.render(f"Timer:{current_time}s",True, "Black")
    timer_rect = timer_surf.get_rect( midleft = (20,130))
    screen.blit(timer_surf, timer_rect)                                                                              
    return current_time
class Cats_animation(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'kiki':
            kiki1 = pg.image.load('graphics/kiki.png').convert_alpha()
            kiki1 = pg.transform.rotozoom(kiki1,0,1.5)
            kiki2 = pg.image.load("graphics/kiki_2.png")
            kiki2 = pg.transform.rotozoom(kiki2,0,1.5)
            self.list = [kiki1,kiki2]
            x_pos = 480
            y_pos = 570

        elif type == 'momo':
            momo1 = pg.image.load("graphics/momo.png").convert_alpha()
            momo1 = pg.transform.rotozoom(momo1,0,2)
            momo2 = pg.image.load("graphics/momo_2.png").convert_alpha()
            momo2 = pg.transform.rotozoom(momo2,0,2)
            self.list = [momo1,momo2]
            x_pos = 120
            y_pos = 120

        elif type == 'koko':
            koko1 = pg.image.load("graphics/koko.png").convert_alpha()
            koko1 = pg.transform.rotozoom(koko1,0,1.5)
            koko2 = pg.image.load("graphics/koko_2.png").convert_alpha()
            koko2 = pg.transform.rotozoom(koko2,0,1.5)
            self.list = [koko1,koko2]
            x_pos = 220
            y_pos = 570

        elif type == 'amoi':
            amoi1 = pg.image.load("graphics/Amoi.png").convert_alpha()
            amoi1 = pg.transform.rotozoom(amoi1,0,2.1)
            amoi2 = pg.image.load("graphics/Amoi_2.png").convert_alpha()
            amoi2 = pg.transform.rotozoom(amoi2,0,2.1)
            self.list = [amoi1,amoi2]
            x_pos = 580
            y_pos = 120
        
        elif type == 'noni':
            noni1 = pg.image.load("graphics/noni_1.png").convert_alpha()
            noni1 = pg.transform.rotozoom(noni1,0,2.4)
            noni2 = pg.image.load("graphics/noni_2.png").convert_alpha()
            noni2 = pg.transform.rotozoom(noni2,0,2.4)
            self.list = [noni1,noni2]
            x_pos = 350
            y_pos = 650
        
        elif type == 'bomb':
            bomb1 = pg.image.load("graphics/bomb.png").convert_alpha()
            bomb1 = pg.transform.rotozoom(bomb1,0,1.5)
            bomb2 = pg.image.load("graphics/bomb2.png").convert_alpha()
            bomb2 = pg.transform.rotozoom(bomb2,0,1.5)
            self.list = [bomb1,bomb2]
            x_pos = 100
            y_pos = 420
        
        elif type == 'fish':
            fish1 = pg.image.load("graphics/tuna_fish.png").convert_alpha()
            fish1 = pg.transform.rotozoom(fish1,0,1.5)
            fish2 = pg.image.load("graphics/gold_fish.png").convert_alpha()
            fish2 = pg.transform.rotozoom(fish2,0,1.5)
            self.list = [fish1,fish2]
            x_pos = 620
            y_pos = 420



        self.index = 0
        self.image = self.list[self.index]
        self.rect = self.image.get_rect( center = (x_pos,y_pos))
        self.mask = pg.mask.from_surface(self.image)
    
    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]
    
    def update(self):
        self.animation()

class Cats_animation_ending(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'kiki':
            kiki1 = pg.image.load("graphics/kiki.png").convert_alpha()
            kiki1 = pg.transform.rotozoom(kiki1,0,1.5)
            kiki2 = pg.image.load("graphics/kiki_2.png").convert_alpha()
            kiki2 = pg.transform.rotozoom(kiki2,0,1.5)
            self.list = [kiki1,kiki2]
            x_pos = 500
            y_pos = 610

        elif type == 'momo':
            momo1 = pg.image.load("graphics/momo.png").convert_alpha()
            momo1 = pg.transform.rotozoom(momo1,0,2)
            momo2 = pg.image.load("graphics/momo_2.png").convert_alpha()
            momo2 = pg.transform.rotozoom(momo2,0,2)
            self.list = [momo1,momo2]
            x_pos = 110
            y_pos = 570

        elif type == 'koko':
            koko1 = pg.image.load("graphics/koko.png").convert_alpha()
            koko1 = pg.transform.rotozoom(koko1,0,1.5)
            koko2 = pg.image.load("graphics/koko_2.png").convert_alpha()
            koko2 = pg.transform.rotozoom(koko2,0,1.5)
            self.list = [koko1,koko2]
            x_pos = 220
            y_pos = 610

        elif type == 'amoi':
            amoi1 = pg.image.load("graphics/Amoi.png").convert_alpha()
            amoi1 = pg.transform.rotozoom(amoi1,0,2.1)
            amoi2 = pg.image.load("graphics/Amoi_2.png").convert_alpha()
            amoi2 = pg.transform.rotozoom(amoi2,0,2.1)
            self.list = [amoi1,amoi2]
            x_pos = 610
            y_pos = 570
        
        elif type == 'noni':
            noni1 = pg.image.load("graphics/noni_1.png").convert_alpha()
            noni1 = pg.transform.rotozoom(noni1,0,2.4)
            noni2 = pg.image.load("graphics/noni_2.png").convert_alpha()
            noni2 = pg.transform.rotozoom(noni2,0,2.4)
            self.list = [noni1,noni2]
            x_pos = 355
            y_pos = 630
        
        elif type == 'fish':
            fish1 = pg.image.load("graphics/tuna_fish.png").convert_alpha()
            fish1 = pg.transform.rotozoom(fish1,0,1.5)
            fish2 = pg.image.load("graphics/gold_fish.png").convert_alpha()
            fish2 = pg.transform.rotozoom(fish2,0,1.5)
            self.list = [fish1,fish2]
            x_pos = 360
            y_pos = 480



        self.index = 0
        self.image = self.list[self.index]
        self.rect = self.image.get_rect( center = (x_pos,y_pos))
        self.mask = pg.mask.from_surface(self.image)
    
    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]
    
    def update(self):
        self.animation()
######################################## first game #########################################################
class Fish(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("graphics/tuna_fish.png").convert_alpha()
        self.rect = self.image.get_rect( center = ((randint(150,650),randint(300,600))))
        self.mask = pg.mask.from_surface(self.image)


class Koko(pg.sprite.Sprite):
    def __init__(self):
     super().__init__()
     self.image = pg.image.load("graphics/koko.png").convert_alpha()
     koko1 = pg.image.load("graphics/koko.png").convert_alpha()
     koko2 = pg.image.load("graphics/koko_2.png").convert_alpha()
     self.list = [koko1,koko2]
     self.index = 0
     self.image = self.list[self.index]
     self.rect = self.image.get_rect( center = (350,700))
     self.max_health = 5
     self.mask = pg.mask.from_surface(self.image)
    
    def health(self):
        for i in range(self.max_health):
            screen.blit(heart, (i*50,20))

    
    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 700:
            self.rect.right = 700
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 750:
            self.rect.bottom = 750

        
    def Koko_input(self):
        keys = pg.key.get_pressed()
        if keys [pg.K_w]:
            self.rect.y -= 5
        if keys [pg.K_s]:
            self.rect.y += 5
        if keys [pg.K_a]:
            self.rect.x -= 5
        if keys [pg.K_d]:
            self.rect.x += 5

    def update(self):
        self.Koko_input()
        self.animation()
        self.health()

class Bomb(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "bomb1":
            bomb1 = pg.image.load("graphics/bomb.png").convert_alpha()
            bomb2 = pg.image.load("graphics/bomb2.png").convert_alpha()
            self.list = [bomb1,bomb2]
            y_pos = 600
        elif type == "bomb2":
            bomb3 = pg.image.load("graphics/bomb.png").convert_alpha()
            bomb4 = pg.image.load("graphics/bomb2.png").convert_alpha()
            self.list = [bomb3,bomb4]
            y_pos = 500
        elif type == "bomb3":
            bomb5 = pg.image.load("graphics/bomb.png").convert_alpha()
            bomb6 = pg.image.load("graphics/bomb2.png").convert_alpha()
            self.list = [bomb5,bomb6]
            y_pos = 400
        else:
            bomb7 = pg.image.load("graphics/bomb.png").convert_alpha()
            bomb8 = pg.image.load("graphics/bomb2.png").convert_alpha()
            self.list = [bomb7,bomb8]
            y_pos = 300
        self.index = 0
        self.image = self.list[self.index]
        self.rect = self.image.get_rect( center = (randint(750,950),  y_pos))
        self.mask = pg.mask.from_surface(self.image)
    
    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]

    def destroy(self):
        if self.rect.x <= -50:
            self.kill()
    def update(self):
        self.animation()
        self.destroy()
        self.rect.x -= 5



######################################## first game #########################################################

######################################## second game #########################################################
        
class CATS_3(pg.sprite.Sprite):
    def __init__(self,type):
     super().__init__()
     if type == "Momo":
        Momo1 = pg.image.load("graphics/momo.png").convert_alpha()
        Momo2 = pg.image.load("graphics/momo_2.png").convert_alpha()
        self.list = [Momo1,Momo2]
     if type == "Amoi":
        Amoi1 = pg.image.load("graphics/Amoi.png").convert_alpha()
        Amoi2 = pg.image.load("graphics/Amoi_2.png").convert_alpha()
        self.list = [Amoi1,Amoi2]
     if type == "Noni":
        Noni1 = pg.image.load("graphics/noni_1.png").convert_alpha()
        Noni2 = pg.image.load("graphics/noni_2.png").convert_alpha()
        self.list = [Noni1,Noni2]
     self.index = 0
     self.image = self.list[self.index]
     self.rect = self.image.get_rect( center = (randint(150,650), 10))
     self.mask = pg.mask.from_surface(self.image)

     
    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]

        
    def destroy(self):
       if self.rect.y >= 800:
           self.kill()

    def update(self):
        self.animation()
        self.destroy
        self.rect.y += 8
    
class Bomb_Fall(pg.sprite.Sprite):
    def __init__(self):
     super().__init__()
     self.image = pg.image.load("graphics/bomb.png").convert_alpha()
     bomb1 = pg.image.load("graphics/bomb.png").convert_alpha()
     bomb2 = pg.image.load("graphics/bomb2.png").convert_alpha()
     self.list = [bomb1,bomb2]
     self.index = 0
     self.image = self.list[self.index]
     self.rect = self.image.get_rect( center = (randint(150,650),10))
     self.mask = pg.mask.from_surface(self.image)
    
    
    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]

    
    def destroy(self):
        if self.rect.y >= 800:
            self.kill()

    def update(self):
        self.animation()
        self.rect.y += 10


class Basket(pg.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pg.image.load("graphics/basket pixel.png").convert_alpha()
      self.rect = self.image.get_rect( center = (350,600))
      self.mask = pg.mask.from_surface(self.image)
      self.max_health = 5
      self.speed = 6

   def health(self):
      for i in range(self.max_health):
            screen.blit(heart, (i*50,20))


   def basket_input(self):
      keys = pg.key.get_pressed()
      if keys [pg.K_a]:
        self.rect.x -= self.speed
      if keys [pg.K_d]:
        self.rect.x += self.speed

      if self.rect.left <=0:
        self.rect.left = 0
      if self.rect.right >= 700:
        self.rect.right = 700

   def update(self):
       self.basket_input()
       self.health()

class Heart_Regen(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("graphics/heart regen.png").convert_alpha()
        self.rect = self.image.get_rect( center = (randint(150,650),10))
        self.mask = pg.mask.from_surface(self.image)
    def movement(self):
            if self.rect.y >= 800:
                self.kill()
    def update(self):
        self.movement()
        self.rect.y += 9

######################################## second game #########################################################
        
######################################## third game #########################################################
class Gold_Fish(pg.sprite.Sprite):
    def __init__(self,group,x,y):
        super().__init__(group)
    
        golf_fish_1 = pg.image.load("graphics/gold_fish.png").convert_alpha()
        gold_fish_2 = pg.image.load("graphics/gold fish 2.png").convert_alpha()
        self.list = [golf_fish_1,gold_fish_2]
        self.index = 0
        self.image = self.list[self.index]
        self.rect = self.image.get_rect( center = (x,y))
        self.mask = pg.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

        self.fish_lifetime = 1500
        self.spawn_time = pg.time.get_ticks()


    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]

    def update(self):
        global score3
        self.animation()
        if self.rect.colliderect(kiki.rect):
            score3 += 1
            if score3%2 == 0:
                kiki_sfx.play()
            self.kill()
        

        if pg.time.get_ticks() - self.spawn_time > self.fish_lifetime:
            self.kill()


class health_regen(pg.sprite.Sprite):
    def __init__(self,group,type):
        super().__init__(group)
        if type == 'pos1':
            x_pos = 1
            y_pos = 1
        elif type == 'pos2':
            x_pos = 1*3200
            y_pos = 1
        elif type == 'pos3':
            x_pos = 1
            y_pos = 1*2816
        else:
            x_pos = 1*3200
            y_pos = 1*2816
        self.image = pg.image.load("graphics/heart regen.png").convert_alpha()
        self.rect = self.image.get_rect( center = (x_pos,y_pos))
        self.mask = pg.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

    def movement(self):
        distance_x = kiki.rect.x - self.rect.x
        distance_y = kiki.rect.y - self.rect.y
        distance = (distance_x**2 + distance_y**2)**0.5

        speed = 4
        if distance != 0:
            self.rect.x += speed * distance_x / distance
            self.rect.y += speed * distance_y / distance
    
    def update(self):
        self.movement()
        if self.rect.colliderect(kiki.rect):
            health_sfx.play()
            kiki.max_health += 1
            self.kill()
        for fish in fish_bullet:
            if pg.sprite.spritecollide(fish,health_add,False,pg.sprite.collide_mask):
                self.kill()
                fish.kill()


class Bomb_Enemy(pg.sprite.Sprite):
    def __init__(self,group,type):
        super().__init__(group)

        if type == 'pos1':
            x_pos = 1
            y_pos = 1
        elif type == 'pos2':
            x_pos = 1*3200
            y_pos = 1
        elif type == 'pos3':
            x_pos = 1
            y_pos = 1*2816
        else:
            x_pos = 1*3200
            y_pos = 1*2816
            
        
        bomb1 = pg.image.load("graphics/bomb.png").convert_alpha()
        bomb2 = pg.image.load("graphics/bomb2.png").convert_alpha()
        self.list = [bomb1,bomb2]
        self.index = 0
        self.image = self.list[self.index]
        self.image = pg.transform.rotozoom(self.image,0,1.5)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.mask = pg.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()



    def animation(self):
        self.index += 0.1
        if self.index >= len(self.list):
            self.index = 0
        self.image = self.list[int(self.index)]
    
    def movement(self):
        distance_x = kiki.rect.x - self.rect.x
        distance_y = kiki.rect.y - self.rect.y
        distance = (distance_x**2 + distance_y**2)**0.5

        speed = 6
        if distance != 0:
            self.rect.x += speed * distance_x / distance
            self.rect.y += speed * distance_y / distance
        
    def update(self):
        global screen_shake
        self.animation()
        self.movement()
        if self.rect.colliderect(kiki.rect):
            screen_shake = 32
            kiki.max_health -= 1
            bomb_sfx.play()
            self.kill()
        

class Kiki(pg.sprite.Sprite):
    def __init__(self,group,pos):
        super().__init__(group)

        self.pos = pg.math.Vector2(pos)
        kiki1 = pg.image.load("graphics/kiki.png").convert_alpha()
        kiki2 = pg.image.load("graphics/kiki_2.png").convert_alpha()
        self.list = [kiki1,kiki2]
        self.index = 0
        self.image = self.list[self.index]
        self.image = pg.transform.rotozoom(self.image,0,1.5)
        self.rect = self.image.get_rect( center = (self.pos))
        self.mask = pg.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

        self.direction = pg.math.Vector2()
        self.speed = 10

        self.max_health = 7

        self.ready = True
        self.shoot_time = 0
        self.shoot_cooldown = 300

    def animation(self):
            self.index += 0.1
            if self.index >= len(self.list):
                self.index = 0
            self.image = self.list[int(self.index)]

    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.direction.y = -1

        elif keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if pg.mouse.get_pressed()==(1,0,0) and self.ready:
            self.shoot_fish()
            self.ready = False
            self.shoot_time = pg.time.get_ticks() 
        
    
    def movement(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.dy = (self.mouse_pos[1]-(self.rect.centery - camera.offset.y))
        self.dx = (self.mouse_pos[0]-(self.rect.centerx - camera.offset.x))
        self.angle = math.degrees(math.atan2(self.dy,self.dx))


    def recharge(self):
        if not self.ready:
            time = pg.time.get_ticks()
            if time - self.shoot_time >= self.shoot_cooldown:
                self.ready = True
    
    def shoot_fish(self):
        fish_bullet.add(Fish_Bullet(camera,self.rect.x,self.rect.y,self.angle))

    def update(self):
        self.animation()
        self.input()
        self.recharge()
        self.movement()
        self.rect.center += self.direction*self.speed
        

class Fish_Bullet(pg.sprite.Sprite):
    def __init__(self,group,x,y,angle):
        super().__init__(group)
        self.image = pg.image.load("graphics/tuna fish better.png")
        self.fish_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center =(x,y)
        self.mask = pg.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()

        self.speed = 8 
        self.x = x
        self.y = y
        self.angle = angle
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) *self.speed
        self.y_vel = math.sin(self.angle * (2*math  .pi/360)) *self.speed

        self.bullet_lifetime = 750
        self.spawn_time = pg.time.get_ticks()

    
    def rotation(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.dy = (self.mouse_pos[1]-(self.rect.centery - camera.offset.y))
        self.dx = (self.mouse_pos[0]-(self.rect.centerx - camera.offset.x))
        self.angle = math.degrees(math.atan2(self.dy,self.dx))
        self.image = pg.transform.rotate(self.fish_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    def movement(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if pg.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill()

    def update(self):
        global gold_fish_appear_count

        self.movement()
        self.rotation()
        for bomb in enemy:
            if pg.sprite.spritecollide(bomb,fish_bullet,False,pg.sprite.collide_mask):
                gold_fish_appear_count += 1
                bomb.kill()
                self.kill()
                if gold_fish_appear_count != 0:
                    if gold_fish_appear_count % 2 == 0:
                        gold_fish.add(Gold_Fish(camera,self.rect.x,self.rect.y))
                

class Camera(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        #camera offset
        self.offset = pg.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2

        self.ground = pg.image.load("Background/screen3 awesome map.png").convert_alpha()
        self.ground_rect = self.ground.get_rect(topleft = (0,0))



    def center_target(self,target):
         self.offset.x = target.rect.centerx - self.half_w
         self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self,player):
        global score3
        global timer3
        self.center_target(player)

        self.score_message3 = font.render(f'Score : {score3}',True,'Black')
        self.score_rect3 = self.score_message3.get_rect( midleft = (20,90))

        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground,ground_offset)
        screen.blit(self.score_message3,self.score_rect3)

        for i in range(kiki.max_health):
            screen.blit(heart3, (i*50,20))

        timer3 = display_timer()
        
        kiki.rect.clamp_ip(self.ground_rect)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft- self.offset
            self.display_surface.blit(sprite.image,offset_pos)
######################################## third game #########################################################
pg.init()
WIDTH, HEIGHT = 700, 750
org_screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Kiki and Friend's Bizzare Adventure")
icon = pg.image.load("graphics/kiki.png")
pg.display.set_icon(icon)
clock = pg.time.Clock()
bg_sound = pg.mixer.Sound("sound effect/meatball parade by kevin macleod.mp3")
bg_sound.set_volume(1)

screen_shake = 0

screen = pg.display.set_mode((WIDTH,HEIGHT))
screen_rect = screen.get_rect()



cats_animation = pg.sprite.Group()
type_cat = ['kiki','koko','momo','amoi','noni','bomb','fish']
for i in type_cat:
    cats_animation.add(Cats_animation(i))

cats_animation_ending = pg.sprite.Group()
type_cat_end = ['kiki','koko','momo','amoi','noni','fish']
for j in type_cat_end:
    cats_animation_ending.add(Cats_animation_ending(j))

Game_initial = True
Game_start_1 = False
Game_Letsgo_1 = False
Game_retry_1 = False
start_time = 0
timer = 0
score = 0
instuction1 = False

Game_start_2 = False
Game_Letsgo_2 = False
Game_retry_2 = False
timer2 = 0
score2 = 0
instuction2 = False

Game_start_3 = False
Game_letsgo_3 = False
Game_retry_3 = False
score3 = 0
timer3 = 0
gold_fish_appear_count = 0
instuction3 = False
start_countdown = None

countdown = False
Game_ending = False

font = pg.font.Font("graphics/ComicNeueSansID.ttf",30)
font2 = pg.font.Font("graphics/ComicNeueSansID.ttf",50)

bomb_sfx = pg.mixer.Sound("sound effect/short explosion.MP3")
bomb_sfx.set_volume(1)
health_sfx = pg.mixer.Sound("sound effect/heal sound effect.MP3")
health_sfx.set_volume(1)
letsgo_sfx = pg.mixer.Sound("sound effect/Game Success Sound Effect  No Copyright.mp3")
letsgo_sfx.set_volume(1)
retry_sfx = pg.mixer.Sound("sound effect/Fail SFX.MP3")
retry_sfx.set_volume(1)
kiki_sfx = pg.mixer.Sound("sound effect/kiki.MP3")
kiki_sfx.set_volume(1)
koko_sfx = pg.mixer.Sound("sound effect/koko meow.MP3")
koko_sfx.set_volume(1)
amoi_sfx = pg.mixer.Sound("sound effect/amoi meow.MP3")
amoi_sfx.set_volume(1)
momo_sfx = pg.mixer.Sound("sound effect/momo  sfx.MP3")
momo_sfx.set_volume(1)

######################################## intro screen #########################################################
pteb_logo = pg.image.load("Background/Pusat_Tingkatan_Enam_Belait-removebg-preview__1_-removebg-preview (1).png").convert_alpha()
pteb_logo_rect = pteb_logo.get_rect(center = (350,100))

click_play = font.render("Click Space button to play", True, "Black")
click_play_rect = click_play.get_rect(center = (350,450))

message_start1 = font.render("IT Crowd Presents...", True, "Black")
message_start_rect1 = message_start1.get_rect(center = (360,240))
message_start2 = font.render("Kiki and Friend's Bizarre Adventure!", True, "Black")
message_start_rect2 = message_start1.get_rect(center = (250,320))
######################################## initscreen #########################################################

######################################## endscreen #########################################################

c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)


message_end1 = font2.render("CONGRATULATIONS!",True,(c1,c2,c3))
message_end1_rect = message_end1.get_rect( topleft = (100,60))

message_end2 = font.render("You successfully saved the cats\n     and bested those bombs!",True,'Black') 
message_end2_rect = message_end2.get_rect( topleft = (135,200))

######################################## endscreen #########################################################



######################################## first game #########################################################
screen2 = pg.image.load("Background/park backgorund (1).png").convert()
heart = pg.image.load("graphics/Heart_life.png").convert_alpha()



#Sprite Related
Koko_game = pg.sprite.GroupSingle()
Koko_game.add(Koko())
bombing = pg.sprite.Group()
fish_game = pg.sprite.GroupSingle()



bombing_timer = pg.USEREVENT + 1
pg.time.set_timer(bombing_timer, 500)

fish_timer = pg.USEREVENT + 2
pg.time.set_timer(fish_timer, 1500)
######################################## first game #########################################################

######################################## second game #######################################################
screen3 = pg.image.load("Background/Pixel_Art_Background- screen 4.jpg").convert()


cats_3 = pg.sprite.Group()
bombing_fall = pg.sprite.Group()
bombing_fall.add(Bomb_Fall())
basket = pg.sprite.GroupSingle()
basket.add(Basket())
heart_regen = pg.sprite.GroupSingle()
heart_regen.add(Heart_Regen())

bomb_fall_timer = pg.USEREVENT + 3
pg.time.set_timer(bomb_fall_timer, 700)

cats_3_timer = pg.USEREVENT + 4
pg.time.set_timer(cats_3_timer, 850)

heart_regen_timer = pg.USEREVENT + 5
pg.time.set_timer(heart_regen_timer, 6000)



######################################## second game #########################################################

######################################## third game #########################################################
heart3 = pg.image.load("graphics/Heart_life.png").convert_alpha()
fish3 = pg.image.load("graphics/gold_fish.png").convert_alpha()
screen4 = pg.image.load("Background/screen3 awesome map.png")

camera = Camera()
kiki = Kiki(camera,(25*64,22*64))

gold_fish = pg.sprite.Group()
enemy = pg.sprite.Group()
fish_bullet = pg.sprite.Group()
health_add = pg.sprite.Group()


bomb_enemy_timer = pg.USEREVENT + 6
pg.time.set_timer(bomb_enemy_timer, 1000)

heart_gainer_timer = pg.USEREVENT + 7
pg.time.set_timer(heart_gainer_timer, 20000 )
######################################## third game #########################################################
bg_sound.play(-1)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        if Game_initial:
            if event.type == pg.KEYDOWN:
                     if event.key == pg.K_SPACE:
                        Game_initial = False
                        instuction1 = True
                        countdown = True
######################################## first game ######################################################### 
        if instuction1:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    instuction1 = False
                    Game_start_1 = True

        if Game_start_1:
            if event.type == bombing_timer:
                bombing.add(Bomb(choice(['bomb1','bomb2','bomb3','bomb4'])))

            if event.type == fish_timer:
                fish_game.add(Fish())

        if countdown:
            start_countdown = pg.time.get_ticks()

        if Game_retry_1:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    score = 0
                    start_time = int(pg.time.get_ticks()/1000)
                    bombing.empty()
                    Koko_game.sprite.max_health = 5
                    Koko_game.sprite.rect.centerx = 350
                    Koko_game.sprite.rect.centery = 700
                    Game_start_1 = True
                    Game_retry_1 = False 
        if Game_Letsgo_1:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    score = 0
                    start_time = int(pg.time.get_ticks()/1000)
                    bombing.empty()
                    Game_Letsgo_1 = False
                    instuction2 = True
                    Game_start_1 = False


######################################## first game #########################################################
                    
######################################## second game #########################################################
        if instuction2:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    instuction2 = False
                    Game_start_2 = True

        if Game_start_2:
            if event.type == cats_3_timer:
                cats_3.add(CATS_3(choice(['Momo','Amoi','Noni'])))

            if event.type == bomb_fall_timer:
                bombing_fall.add(Bomb_Fall())
            
            if event.type == heart_regen_timer:
                heart_regen.add(Heart_Regen())
            
        if Game_retry_2:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    score2 = 0
                    start_time = int(pg.time.get_ticks()/1000)
                    cats_3.empty()
                    bombing_fall.empty()
                    heart_regen.empty()
                    basket.sprite.speed = 6
                    basket.sprite.max_health = 5
                    basket.sprite.rect.centerx = 350
                    basket.sprite.rect.centery = 600
                    Game_start_2 = True
                    Game_retry_2 = False 

        if Game_Letsgo_2:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    score2 = 0
                    start_time = int(pg.time.get_ticks()/1000)
                    cats_3.empty()
                    bombing_fall.empty()
                    heart_regen.empty()
                    basket.sprite.max_health = 5
                    Game_Letsgo_2 = False
                    Game_start_2 = False
                    instuction2 = False
                    instuction3 = True

######################################## second game #########################################################  

######################################## third game #########################################################  
        if instuction3:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    instuction3 = False
                    Game_start_3 = True

        if Game_start_3:
            if event.type == bomb_enemy_timer:
                types = ['pos1','pos2','pos3','pos4']
                enemy.add(Bomb_Enemy(camera,choice(types)))
            if event.type == heart_gainer_timer:
                types = ['pos1','pos2','pos3','pos4']
                health_add.add(health_regen(camera,choice(types)))

        
        if Game_retry_3:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    start_time = int(pg.time.get_ticks()/1000)
                    score3 = 0
                    kiki.max_health = 7
                    kiki.rect.centerx = 25*64
                    kiki.rect.centery = 22*64
                    Game_start_3 = True
                    Game_retry_3 = False         

######################################## third game #########################################################


######################################## first game #########################################################   

    if instuction1:
        screen2_copy = screen2.copy()
        screen2_copy.fill((199,199,199,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen2_copy, (0,0))
        instuction_message1 = font.render("         Collect 10 fishes with Koko\n\n      and avoid the incoming bombs!\n\n Use the W A S D button for movement\n\n               Click Enter to Play",True,'Black')
        instuction_message1_rect = instuction_message1.get_rect( center = (350,450))
        screen.blit(instuction_message1,instuction_message1_rect)
        

    if Game_start_1:
        screen.blit(screen2, (0, 0))
        timer = display_timer()

        score_message = font.render(f"Score:{score}", True, 'Black')
        score_rect = score_message.get_rect( midleft = (20,90))
        screen.blit(score_message,score_rect)

        if pg.sprite.spritecollide(Koko_game.sprite,fish_game,True,pg.sprite.collide_mask):
            score += 1
            if score % 2 == 0:
                koko_sfx.play()
        
        if pg.sprite.spritecollide(Koko_game.sprite,bombing,True,pg.sprite.collide_mask):
            screen_shake = 32
            bomb_sfx.play()
            Koko_game.sprite.rect.centerx = 350
            Koko_game.sprite.rect.centery = 700
            Koko_game.sprite.max_health -= 1


        Koko_game.draw(screen)
        Koko_game.update()

        bombing.draw(screen)
        bombing.update()
        fish_game.update()
        fish_game.draw(screen)

    if score >= 10:
        Game_start_1 = False
        Game_Letsgo_1 = True
        letsgo_sfx.play()
        screen2_copy = screen2.copy()
        screen2_copy.fill((128,128,128,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen2_copy, (0,0))
        congrats = font.render('                     Congrats!\nClick space button for the next stage.', True,'Black')
        lets_go = pg.image.load("graphics/lets_go.png").convert_alpha()
        lets_go = pg.transform.rotozoom(lets_go,0,2)
        lets_go_rect = lets_go.get_rect( center = (350, 450))
        screen.blit(lets_go,lets_go_rect)
        screen.blit(congrats, congrats.get_rect(center = (350,350)))


    if Koko_game.sprite.max_health <= 0:
        Game_start_1 = False
        Game_retry_1 = True
        retry_sfx.play()
        screen2_copy = screen2.copy()
        screen2_copy.fill((128,128,128,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen2_copy, (0,0))
        try_again = font.render('Click Space Button to try again', True , 'Black')
        retry = pg.image.load("graphics/retry.png")
        retry = pg.transform.rotozoom(retry,0,2)
        retry_rect = retry.get_rect( center = (350,450))
        screen.blit(retry,retry_rect)
        screen.blit(try_again, try_again.get_rect( center = (350,300)))


######################################## first game #########################################################
        
######################################## second game #########################################################

    if instuction2:
        screen3_copy = screen3.copy()
        screen3_copy.fill((199,199,199,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen3_copy, (0,0))
        instuction_message2 = font.render(" Noni, Amoi and Momo are falling from the Sky!\n\n        Use the basket and grab 10 of them!\n      and avoid the incoming bombs.....again!\n\n\n           Use the A D button for movement\n\n                      Click Enter to Play",True,'Black')
        instuction_message2_rect = instuction_message2.get_rect( center = (350,330))
        screen.blit(instuction_message2,instuction_message2_rect)

    if Game_start_2:
        screen.blit(screen3, (0,0))
        timer2 = display_timer()

        score_message2 = font.render(f"Score:{score2}", True, 'Black')
        score_rect2 = score_message2.get_rect( midleft = (20,90))
        screen.blit(score_message2,score_rect2)

        if pg.sprite.spritecollide(basket.sprite,cats_3,True,pg.sprite.collide_mask):
            score2 += 1
            basket.sprite.speed = 6
            if score2 %3 == 0:
                meow = ['amoi','momo']
                meowing = choice(meow)
                if meowing == 'amoi':
                    amoi_sfx.play()
                else:
                    momo_sfx.play()


        if pg.sprite.spritecollide(basket.sprite,bombing_fall,True,pg.sprite.collide_mask):
            screen_shake = 32
            bomb_sfx.play()
            basket.sprite.max_health -= 1
            basket.sprite.speed = 2
        
        if pg.sprite.spritecollide(basket.sprite,heart_regen,True,pg.sprite.collide_mask):
            basket.sprite.max_health += 1
            basket.sprite.speed = 6
            health_sfx.play()


        cats_3.draw(screen)
        cats_3.update()

        bombing_fall.draw(screen)
        bombing_fall.update()

        basket.draw(screen)
        basket.update()

        heart_regen.draw(screen)
        heart_regen.update()

    if score2 >= 10:
        letsgo_sfx.play()
        Game_start_2 = False
        Game_Letsgo_2 = True
        screen3_copy = screen3.copy()
        screen3_copy.fill((128,128,128,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen3_copy, (0,0))
        congrats2 = font.render('                     Congrats!\nClick space button for the next stage.', True,'Black')
        lets_go2 = pg.image.load("graphics/lets_go.png").convert_alpha()
        lets_go2 = pg.transform.rotozoom(lets_go2,0,2)
        lets_go2_rect = lets_go2.get_rect( center = (350, 450))
        screen.blit(lets_go2,lets_go2_rect)
        screen.blit(congrats2, congrats2.get_rect(center = (350,300)))

    if basket.sprite.max_health <= 0:
        retry_sfx.play()
        Game_start_2 = False
        Game_retry_2 = True
        screen3_copy = screen3.copy()
        screen3_copy.fill((128,128,128,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen3_copy, (0,0))
        try_again2 = font.render('Click Space button to try again', True , 'Black')
        retry2 = pg.image.load("graphics/retry.png")
        retry2 = pg.transform.rotozoom(retry2,0,2)
        retry_rect2 = retry2.get_rect( center = (350,450))
        screen.blit(retry2,retry_rect2)
        screen.blit(try_again2, try_again2.get_rect( center = (350,300)))

######################################## second game #########################################################
        
######################################## third game #########################################################

    if instuction3:
        screen4_copy = screen4.copy()
        screen4_copy.fill((199,199,199,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen4_copy, (0,0))
        instuction_message3 = font.render("Kiki now gains the power of the Fishes!\n\nUse the mouse and the left click button\nto aim and shoot the incoming bombs\n            and get the Golden Fish!\n\n    Collect a total of 10 Golden Fishes\n\n\n Use the W A S D button for movement\n\n                Click Enter to Play",True,'Black')
        instuction_message3_rect = instuction_message3.get_rect( center = (360,360))
        screen.blit(instuction_message3,instuction_message3_rect)

    if Game_start_3:
        screen.fill('#f0e8c0')

        camera.update()
        camera.custom_draw(kiki)

        
    if kiki.max_health <= 0:
        retry_sfx.play()
        instuction3 = False
        Game_start_3 = False
        Game_retry_3 = True
        screen4_copy = screen4.copy()
        screen4_copy.fill((128,128,128,128), None, pg.BLEND_RGBA_MULT)
        screen.blit(screen4_copy, (0,0))
        try_again3 = font.render('Click Space Button to try again', True, 'Black')
        retry3 = pg.image.load("graphics/retry.png")
        retry3 = pg.transform.rotozoom(retry3,0,2)
        retry_rect3 = retry3.get_rect( center = (350,450))
        screen.blit(retry3,retry_rect3)
        screen.blit(try_again3, try_again3.get_rect( center = (350,300)))


    if score3 >= 7:
        letsgo_sfx.play()
        Game_start_3 = False
        Game_ending = True
        countdown = False
        
######################################## third game #########################################################
        
    if Game_initial:
        screen.fill('#f0e8c0')

        cats_animation.update()
        cats_animation.draw(screen)
        screen.blit(pteb_logo,pteb_logo_rect)
        screen.blit(click_play,click_play_rect)
        screen.blit(message_start1,message_start_rect1)
        screen.blit(message_start2,message_start_rect2)
    
    if Game_ending:
        screen.fill('#f0e8c0')

        cats_animation_ending.update()
        cats_animation_ending.draw(screen)

        elapsed_time = start_countdown
        elapsed_time_text = font.render(f'Elapsed time: {elapsed_time} ms',True,'Black')
        elapsed_time_text_rect = elapsed_time_text.get_rect(center = (350,350))
        screen.blit(message_end1,message_end1_rect)
        screen.blit(message_end2,message_end2_rect)
        screen.blit(elapsed_time_text,elapsed_time_text_rect)

    if screen_shake > 0:
        screen_shake -= 1
    
    render_offset = [0,0]
    if screen_shake:
        render_offset[0] = random.randint(0,8) - 4
        render_offset[1] = random.randint(0,8) - 4


    org_screen.blit(screen, render_offset)
    clock.tick(60)
    pg.display.update()