import pygame
import random

class player:
    pos = ()

    def __init__(self):
        #spawnar spelare o kontrollerar att han inte hamnar på maten
        self.pos = (random.randint(0,4),random.randint(0,4))
        while mapp.food == self.pos:
                self.pos = (random.randint(0,4),random.randint(0,4))
        

    def draw(self):
        pygame.draw.circle(screen, BLACK, coord_to_pixel(self.pos), 45)
        pygame.draw.circle(screen, YELLOW, coord_to_pixel(self.pos), 35)
        
    
    def move(self, key):
        (x, y) = self.pos
        
        if key == 273:
            y -= 1
            
        if key == 274:
            y += 1
        
        if key == 275:
            x += 1
        
        if key == 276:
            x -= 1
        
        self.pos = (x % 5, y % 5)


class world:
        food = ()
        length = 10

        
        def __init__(self):
            #spawnar mat
            self.food = (random.randint(0,4),random.randint(0,4))
            
            
        def draw(self):
            for i in range(0,7):
                x = 99*i + 2
                
                pygame.draw.line(screen, BLUE, (0,x), (self.length, x), 6)
                pygame.draw.line(screen, BLUE, (x,0), (x, self.length), 6)

            if self.length < 500:
                self.length += 1
                return False
            else:
                pygame.draw.circle(screen, BLACK, coord_to_pixel(self.food), 35)
                pygame.draw.circle(screen, RED, coord_to_pixel(self.food), 25)
                return True
        
        
class start_screen:
    
    #visar logan i start skärmen
    def title():
        global pause
        logo = pygame.image.load("hg_logo.png")
        
        if pause == True or east_egg == True:
            #animation för spelets logo
            for i in range(0,11):
                screen.fill(BLACK)
                x = 38*i
                y = 16*i
                logo_scale = pygame.transform.scale(logo, (x, y))
                screen.blit(logo_scale, (253 - x/2, 140 - y/2))
                pygame.display.flip()
                pygame.time.wait(20)
            pygame.display.flip()
        logo_scale = pygame.transform.scale(logo, (380, 160))
        screen.blit(logo_scale, (63, 60))
        pygame.time.wait(250)    
        return False
    
    #ritar upp en cirkel för start knappen
    def startbutton():
        global pause
        pygame.draw.circle(screen, RED, (150, 340), 38)
        start_font= pygame.font.SysFont('Comic Sans MS', 30)
        start_text = start_font.render('Start', False, (BLACK))
        screen.blit(start_text, (127, 330))
        if pause == True:
            pygame.display.flip()
            pygame.time.wait(250)
        
    #ritar upp en kvadrat för quit knappen    
    def quitbutton():
        pygame.draw.rect(screen, RED, (300, 300, 75, 75))
        quit_font= pygame.font.SysFont('Comic Sans', 30)
        quit_text = quit_font.render('Quit', False, (BLACK))
        screen.blit(quit_text, (317,329))
        return False
        
    #kontrollerar om spelare trycker på "quit" eller "start"
    def start_screen_action(mouse):
        (x,y) = mouse
        if x > 300 and y > 300:
            if x < 375 and y < 375:
                print("You chose to close the application!")
                return False
            else:
                return True
        
        if x > 112 and y > 302:
            if x < 188 and y < 375:
                return "start"
        
        return True
    
    
    def fade_in():
        #transition när spelet börjar eller efter at spelare vinner spelet
        for i in range(0,256):
            trans = [255-i, 255-i, 255-i]
            trans_tuple = tuple(trans)
            screen.fill(trans_tuple)
            pygame.time.wait(2)
            pygame.display.flip()
            
        if i == 255:
            return False
        
    #transition för när spelaren stänger spelet    
    def fade_out():
        for i in range(0, 256):
            trans = [i, i, i]
            trans_tuple = tuple(trans)
            screen.fill(trans_tuple)
            pygame.time.wait(1)
            pygame.display.flip()
        return False
    
    #kontrollerar om spelaren försöker aktivera easter egget och aktiverar den
    def easteregg(mouse):
        (x, y) = mouse
        if x > 200 and y > 0:
            if x < 300 and y < 30:
                return True
        return False
    
    #aktiverar easter egget 
    def easteregg_circle(n, status):
        if status == True:
            n = random.randint(0,5)
        pygame.draw.circle(screen, COLOURS[n], (250, 0), 50)
        pygame.display.flip()
        return n
    
    def easteregg2(mouse):
        (x,y) = mouse
        logo = pygame.image.load("UU_logo.png")
        if x > 450 and y > 450:
            if x < 500 and y < 500:
                screen.fill(BLACK)
                logo_scale = pygame.transform.scale(logo, (200, 190))
                screen.blit(logo_scale, (150, 60))
                eastegg_font= pygame.font.SysFont('Times New Roman', 26)
                eastegg_text = eastegg_font.render('This game was designed', False, (WHITE))
                eastegg_text2 = eastegg_font.render('for academic purpose!', False, (WHITE))
                screen.blit(eastegg_text, (125, 260))
                screen.blit(eastegg_text2, (135, 295))
                pygame.display.flip()
                pygame.time.wait(5000)

        
#gör så maten och spelaren spawnar i gridden och inte på linjerna         
def coord_to_pixel(coord):
    (x,y) = coord
    return (99*x + 52, 99*y + 52)

#kallar på pygame funktioner så vi kan använda pygame
pygame.init()
pygame.font.init()


pygame.display.set_caption("Hunger Games 2.1")

#initierar variablerna som falskt innan while loopen, standard!
running = False
started = False
pause = False

BLUE = (70,130,180)
YELLOW = (240,230,140)
BLACK = (0,0,0)
RED = (178,34,34)
WHITE = (255, 255, 255)
GREEN = (0, 153, 51)
PURPLE = (139,0,139)
COLOURS = [BLUE, YELLOW, PURPLE, RED, WHITE, GREEN]

#storleken på skärmen som öppnas och rektangeln för knappen quit
size = width, height = 500, 500

rect = width, height = 50, 50

screen = pygame.display.set_mode(size)

mapp = world()
spelare = player()

#öppnar fönstret, alla globala variabler tilldelas
running = True
trans_in = True
pause = True
east_egg = False
trans_out = False
east_egg_circle = False
east_egg_stat = False
n = 0
while running:
    if trans_in:
        trans_in = start_screen.fade_in()
    
    if east_egg_circle:
        n = start_screen.easteregg_circle(n, east_egg_stat)
        east_egg_stat = False
        
    
    #så länge started är falskt så syns endast start skärmen
    if not started:
        screen.fill(BLACK)
        east_egg = start_screen.title()
        start_screen.startbutton()
        pause = start_screen.quitbutton()
        pygame.display.flip()
        
    #kontrollerar om spelaren intragerar med spelet    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = start_screen.start_screen_action(pygame.mouse.get_pos())
                east_egg = start_screen.easteregg(pygame.mouse.get_pos())
                east_egg2 = start_screen.easteregg2(pygame.mouse.get_pos())
                if east_egg:
                    east_egg = start_screen.title()
                    east_egg_circle = True
                    east_egg_stat = True
                if running == "start":
                    started = True
                    running = True
                    trans_out = True
            if event.type == pygame.QUIT:
                running = False
        
            
    #här så startas spelet        
    else:
        east_egg_circle = False
        if trans_out:
            trans_out = start_screen.fade_out()
       
    #ritar kartan, maten och spelaren
        screen.fill(WHITE)
        if mapp.draw():
            spelare.draw()
            
            #om spelaren äter upp maten så skickas han till start menyn
            if spelare.pos == mapp.food:
                print("You WON, thank you for playing our game!")
                trans = True
                started = False
                pause = True
                mapp = world()
                spelare = player()
                start_screen.fade_in()

        pygame.display.flip()

        #Stänger fönstret
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                spelare.move(event.__dict__["key"])
            if event.type == pygame.QUIT:
                running = False
                
start_screen.fade_out()
