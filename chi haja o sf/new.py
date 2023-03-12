from screeninfo import get_monitors
import pygame 
import time
import os
from random import randrange


#PASSWORD MUST CONTAIN ONLY LOWER CASE ALPH OR NUMS
PASSWORD = 'qwerty'

import socket

#FULLNAME MUST BE IN THIS FORMAT 'Brian Gauss'
FULLNAME = ''
CURRENTPOST = 'mds_1.0-p - {}'.format(socket.getfqdn())

monitors = get_monitors()
tm = time.time()
MonitorWidth = monitors[0].width 
MonitorHeight = monitors[0].height
running = True

pygame.init()
isQuitting = False


screen = pygame.display.set_mode([MonitorWidth, MonitorHeight], pygame.FULLSCREEN)

w, h = screen.get_size()
COLOR_INACTIVE = pygame.Color(152, 131, 102, 150)#pygame.Color(123, 98, 70, 150)
# COLOR_INACTIVE = pygame.Color(103, 78, 50, 150)
COLOR_ACTIVE = pygame.Color('white')
COLOR_TEXT = pygame.Color('white')
COLOR_TEXT_SHADOW = pygame.Color(0, 0, 0, 10)

FONT = pygame.font.Font(None, 42)
NAMEFONT = pygame.font.Font(None, 24)
NAMEFONTSHADOW = pygame.font.Font(None, 26)

MISCFONT = pygame.font.Font(None, 22)


shakektime = time.time()
shakeDir = -1

def quitwithblack():
    isQuitting = True
    #time.sleep(1)
    running = False
    pygame.quit()
    exit()

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.size = w, h
        self.pos = (x, y)
        self.x = x
        self.y = y
        self.bg = pygame.Surface(self.size)
        self.bg.fill(COLOR_INACTIVE)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.realtext = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = True
        self.isWrong = 0
        self.original_image = pygame.Surface((w, h))
        self.size = (w, h)
        self.rect_image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.textColor = COLOR_TEXT


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            #if self.active: #and isWrong == 0:
            if event.key == pygame.K_RETURN:
                if self.realtext == PASSWORD:
                    print('hello fibo')
                    quitwithblack()
                    # screen.fill((0, 0, 0))
                    # time.sleep(1)
                    # pygame.quit()
                    # exit()
                #self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                self.realtext = self.realtext[:-1]
            else:
                char = ''
                char += str(event.unicode)
                if len(self.text) < 15 and char :
                    self.text += '\u2022'
                    self.realtext += char #event.unicode
            # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.textColor)
                
    def clear(self):
        self.text = ''
        self.realtext = ''
        self.txt_surface = FONT.render(self.text, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        #self.rect.w = width

    def draw(self, screen):
        # # Blit the rect.
        # pygame.draw.rect(self.rect_image, COLOR_TEXT_SHADOW, (0, 2, * self.size), border_radius = 0)
        # screen.blit(self.rect_image, (self.x - 10, self.y - 10))
        # # 
        # pygame.draw.rect(self.rect_image, COLOR_INACTIVE, (0, 0, * self.size), border_radius = 2)
        # screen.blit(self.rect_image, (self.x - 10, self.y - 10))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x - (self.rect.w / 20) + 5, self.rect.y - (self.rect.h / 10) - 10))
        


       






box = InputBox(MonitorWidth / 2 - (MonitorWidth / 38), MonitorHeight / 2, MonitorWidth / 15, 25)
pygame.mouse.set_visible(False)

lock_img = pygame.image.load('./10.png')
# lock_img = pygame.image.load('./user_icon.png')
lock_img = pygame.transform.scale(lock_img, (MonitorWidth, MonitorHeight))

user_icon = pygame.image.load('./user_icon.png')
user_icon =  pygame.transform.scale(user_icon, (MonitorWidth / 17 , MonitorWidth / 17))
user_icon_pos = ((MonitorWidth / 2) - (user_icon.get_width() / 2), (MonitorHeight / 2) - (user_icon.get_height() / 2) - (MonitorHeight / 10))






while running:
    if (time.time() > tm + 5) or isQuitting == True: #TODO:
        screen.fill((0, 0, 0))
        box.clear()
    else:
        # push wallpaper to screen 
        screen.blit(lock_img, (0, 0))
        # create and push black overlay to screen
        # alpha = pygame.Surface((MonitorWidth, MonitorHeight), pygame.SRCALPHA)
        # alpha.fill((0, 0, 0, 80))
        # screen.blit(alpha, (0,0))

        # push user Default Icon to screen
        #screen.blit(user_icon, user_icon_pos)
        #FULL NAME TEXT
        dropshadow_offset = 1
        Name_surface = NAMEFONT.render(FULLNAME, True, COLOR_TEXT_SHADOW)
        w, h = Name_surface.get_size()
        # make the drop-shadow
        screen.blit(Name_surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight / 2) - (h * 3) + dropshadow_offset))
        screen.blit(Name_surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight / 2) - (h * 3) + dropshadow_offset))
        # make the overlay text
        Name_surface = NAMEFONT.render(FULLNAME, True, COLOR_TEXT)
        w, h = Name_surface.get_size()
        screen.blit(Name_surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight / 2) - (h * 3)))

        dropshadow_offset = 1
        Post_Surface = MISCFONT.render(CURRENTPOST, True, COLOR_TEXT_SHADOW)
        w, h = Post_Surface.get_size()
        # make the drop-shadow
        # screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight) - (MonitorHeight / 5) + dropshadow_offset))
        # screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight / 2) - (h * 3) + dropshadow_offset))
        # make the overlay text
        Post_Surface = MISCFONT.render(CURRENTPOST, True, COLOR_TEXT)
        w, h = Post_Surface.get_size()
        screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight) - ((MonitorHeight / 5) - 100)))

        dropshadow_offset = 1
        hour = int(time.strftime("%H"))
        half = ' AM'
        if hour >= 12:
            hour -= 12
            half = ' PM'
        hour = str(hour)
        minute = time.strftime("%M")
        currenttime = hour + ':' + minute + half
        Post_Surface = MISCFONT.render(currenttime, True, COLOR_TEXT_SHADOW)
        w, h = Post_Surface.get_size()
        # make the drop-shadow
        screen.blit(Post_Surface, ((MonitorWidth ) - (w) - 5, (h / 2) + dropshadow_offset))
        # screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight / 2) - (h * 3) + dropshadow_offset))
        # make the overlay text
        Post_Surface = MISCFONT.render(currenttime, True, COLOR_TEXT)
        w, h = Post_Surface.get_size()
        screen.blit(Post_Surface, ((MonitorWidth ) - (w) - 5, (h / 2)))



        # dropshadow_offset = 1
        # Post_Surface = MISCFONT.render('Cancel', True, COLOR_TEXT_SHADOW)
        # w, h = Post_Surface.get_size()
        # make the drop-shadow
        # screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight) - (MonitorHeight / 10) + dropshadow_offset))
        # screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight / 2) - (h * 3) + dropshadow_offset))
        # make the overlay text
        # Post_Surface = MISCFONT.render('Cancel', True, COLOR_TEXT)
        # w, h = Post_Surface.get_size()
        # screen.blit(Post_Surface, ((MonitorWidth / 2) - (w / 2), (MonitorHeight) - (MonitorHeight / 10)))


        


        box.update()
        box.draw(screen)

    # Did the user click the window close button?
    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN or ((event.type == pygame.MOUSEMOTION) and (x != MonitorWidth - 100) and (y != MonitorHeight - 100)):
            tm = time.time()
        if event.type == pygame.QUIT:
            running = False
        box.handle_event(event)




    # Flip the display
    pygame.display.flip()

    if pygame.mouse.get_focused() == 0:
        pygame.mouse.set_pos(MonitorWidth - 100, MonitorHeight - 100)
    if pygame.mouse.get_focused() == 0:
        os.system('pmset displaysleepnow')
        exit()

# Done! Time to quit.
pygame.quit()
