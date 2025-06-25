import random
import pygame, sys
import math

pygame.init()

def vittoria_2(punti1, punti2):
    risultato = "Player 2 ha vinto per " + str(punti2) + " a " + str(punti1)
    title_surface = font_title.render(risultato, True, pygame.Color('white'))
    instr_surface = font_menu.render("Premi SPAZIO per ricominciare", True, pygame.Color('white'))
    instr_surface2 = font_menu.render("Premi ESC per tornare al menù", True, pygame.Color('white'))

    window.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, SCREEN_HEIGHT // 3))
    window.blit(instr_surface, (SCREEN_WIDTH // 2 - instr_surface.get_width() // 2, SCREEN_HEIGHT // 2))
    window.blit(instr_surface2, (SCREEN_WIDTH // 2 - instr_surface2.get_width() // 2, SCREEN_HEIGHT // 2 +50))


def vittoria_1(punti1, punti2):
    risultato = "Player 1 ha vinto per " + str(punti1) + " a " + str(punti2)
    title_surface = font_title.render(risultato, True, pygame.Color('white'))
    instr_surface = font_menu.render("Premi SPAZIO per ricominciare", True, pygame.Color('white'))
    instr_surface2 = font_menu.render("Premi ESC per tornare al menù", True, pygame.Color('white'))

    window.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, SCREEN_HEIGHT // 3))
    window.blit(instr_surface, (SCREEN_WIDTH // 2 - instr_surface.get_width() // 2, SCREEN_HEIGHT // 2))
    window.blit(instr_surface2, (SCREEN_WIDTH // 2 - instr_surface2.get_width() // 2, SCREEN_HEIGHT // 2 +50))

#dichiarazione inizioale
colorino1 = (255, 242,0) 
colorino2 = (255,255,255)

game_over = False
font_title = pygame.font.SysFont(None, 100)
font_menu = pygame.font.SysFont(None, 50)
Playing = False
font = pygame.font.SysFont(None, 60)  # Nessun font specifico, grandezza 60
palla_ferma = True
tempo_ripartenza = pygame.time.get_ticks() + 2000  # 2 secondi

def mov_player_1(keys):
    if keys[pygame.K_w]:
        return -5
    elif keys[pygame.K_s]:
        return 5
    return 0

def mov_player_2(keys):
    if keys[pygame.K_UP]:
        return -5
    elif keys[pygame.K_DOWN]:
        return 5
    return 0
                
def check_collisione(ball_x, ball_y, ball_radius, rect_x, rect_y, rect_larghezza, rect_altezza):
    # Trova il punto più vicino sul rettangolo rispetto al centro della palla
    closest_x = max(rect_x, min(ball_x, rect_x + rect_larghezza))
    closest_y = max(rect_y, min(ball_y, rect_y + rect_altezza))
    
    # Calcola la distanza tra il centro della palla e questo punto
    distance_x = ball_x - closest_x
    distance_y = ball_y - closest_y
    
    distance = math.sqrt(distance_x**2 + distance_y**2)
    
    # Se la distanza è minore o uguale al raggio, c'è collisione
    if distance <= ball_radius:
        return True
    else:
        return False

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
d = SCREEN_HEIGHT
BLACK = (0,0,0)

#dichiarazione punteggio
punti_player_1 = 0
punti_player_2 = 0

#righa divisore 
div_larg = 5
div_x = (SCREEN_WIDTH // 2) - (div_larg // 2)
div_y = 0
div_hight = d

#paremetri palla

ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 0
ball_speed_y = 0
ball_radius = 10
ball_speed_x = random.choice([5,4,-5,-4])
ball_speed_y = random.choice([4,3,-4,-3]) 
#
#

#parametri rettangolo player 1
rect_x = 50
rect_y = 300
rect_larghezza = 30
rect_altezza = 100

rect_speed_y = 0

#parametri rettangolo player 2
rect_x_2 = 950
rect_y_2 = 300
rect_speed_y_2 = 0



window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
key = pygame.K_RIGHT
Scelta = True
competitiva = False
while True:
    
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_ESCAPE:
                game_over = False
        

        if not Playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Scelta = True
                    colorino1 = (255, 242, 0)
                    colorino2 = (255, 255, 255)
                elif event.key == pygame.K_RIGHT:
                    Scelta = False
                    colorino1 = (255, 255, 255)
                    colorino2 = (255, 242, 0)
                  
                if event.key == pygame.K_SPACE:
                    if Scelta:
                        competitiva = False
                        punti_player_1 = 0
                        punti_player_2 = 0
                        ball_x = SCREEN_WIDTH // 2
                        ball_y = SCREEN_HEIGHT // 2
                        ball_speed_x = random.choice([5, -5])
                        ball_speed_y = random.choice([3, -3])
                        palla_ferma = False
                        Playing = True
                    else:
                        competitiva = True
                        punti_player_1 = 0
                        punti_player_2 = 0
                        ball_x = SCREEN_WIDTH // 2
                        ball_y = SCREEN_HEIGHT // 2
                        ball_speed_x = random.choice([5, -5])
                        ball_speed_y = random.choice([3, -3])
                        palla_ferma = False
                        Playing = True                        

                
    if Playing and not competitiva:
            keys = pygame.key.get_pressed()
            rect_speed_y = mov_player_1(keys)
            rect_speed_y_2 = mov_player_2(keys)

            pygame.draw.circle(window, pygame.Color('white'), (ball_x, ball_y), ball_radius)

            if ball_y >= SCREEN_HEIGHT - ball_radius:
                ball_speed_y *= -1
            elif ball_y <= ball_radius:
                ball_speed_y *= -1

            if ball_x >= SCREEN_WIDTH - ball_radius:
                punti_player_1 += 1
                palla_ferma = True
                ball_speed_x = 0
                ball_speed_y = 0
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                tempo_ripartenza = pygame.time.get_ticks() + 2000
            elif ball_x <= 0:
                punti_player_2 += 1
                palla_ferma = True
                ball_speed_x = 0
                ball_speed_y = 0
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                tempo_ripartenza = pygame.time.get_ticks() + 2000

            if punti_player_1 >= 3 :
                Playing = False
                game_over = True
                
            if punti_player_2 >= 3 :
                Playing = False    
                game_over = True        

            if palla_ferma:
                if pygame.time.get_ticks() >= tempo_ripartenza:
                    palla_ferma = False
                    ball_speed_x = random.choice([4, -4])
                    ball_speed_y = random.choice([3, -3])
            else:
                ball_x += ball_speed_x
                ball_y += ball_speed_y

            if check_collisione(ball_x, ball_y, ball_radius, rect_x, rect_y, rect_larghezza, rect_altezza):
                ball_speed_x *= -1

            if check_collisione(ball_x, ball_y, ball_radius, rect_x_2, rect_y_2, rect_larghezza, rect_altezza):
                ball_speed_x *= -1

            rect_y += rect_speed_y
            rect_y_2 += rect_speed_y_2

            if rect_y < 0:
                rect_y = 0
            elif rect_y + rect_altezza > SCREEN_HEIGHT:
                rect_y = SCREEN_HEIGHT - rect_altezza

            if rect_y_2 < 0:
                rect_y_2 = 0
            elif rect_y_2 + rect_altezza > SCREEN_HEIGHT:
                rect_y_2 = SCREEN_HEIGHT - rect_altezza

            pygame.draw.rect(window, pygame.Color('white'), (div_x, div_y, div_larg, div_hight))
            pygame.draw.rect(window, pygame.Color('white'), (rect_x, rect_y, rect_larghezza, rect_altezza))
            pygame.draw.rect(window, pygame.Color('white'), (rect_x_2, rect_y_2, rect_larghezza, rect_altezza))

            text_p1 = font.render(str(punti_player_1), True, (255, 255, 255))
            text_p2 = font.render(str(punti_player_2), True, (255, 255, 255))

            window.blit(text_p1, (SCREEN_WIDTH // 4, 20))
            window.blit(text_p2, (SCREEN_WIDTH * 3 // 4, 20))
    elif Playing and competitiva:        
            keys = pygame.key.get_pressed()
            rect_speed_y = mov_player_1(keys)
            rect_speed_y_2 = mov_player_2(keys)

            pygame.draw.circle(window, pygame.Color('white'), (ball_x, ball_y), ball_radius)

            if ball_y >= SCREEN_HEIGHT - ball_radius:
                ball_speed_y *= -1
            elif ball_y <= ball_radius:
                ball_speed_y *= -1

            if ball_x >= SCREEN_WIDTH - ball_radius:
                punti_player_1 += 1
                palla_ferma = True
                ball_speed_x = 0
                ball_speed_y = 0
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                tempo_ripartenza = pygame.time.get_ticks() + 2000
            elif ball_x <= 0:
                punti_player_2 += 1
                palla_ferma = True
                ball_speed_x = 0
                ball_speed_y = 0
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                tempo_ripartenza = pygame.time.get_ticks() + 2000

            if punti_player_1 > punti_player_2 and punti_player_1 >= 3 and (punti_player_1-punti_player_2)>= 2 :
                Playing = False
                game_over = True
                
            if punti_player_2 > punti_player_1 and punti_player_2 >= 3 and (punti_player_2-punti_player_1)>= 2 :
                Playing = False    
                game_over = True        

            if palla_ferma:
                if pygame.time.get_ticks() >= tempo_ripartenza:
                    palla_ferma = False
                    ball_speed_x = random.choice([4, -4])
                    ball_speed_y = random.choice([3, -3])
            else:
                ball_x += ball_speed_x
                ball_y += ball_speed_y

            if check_collisione(ball_x, ball_y, ball_radius, rect_x, rect_y, rect_larghezza, rect_altezza):
                ball_speed_x *= -1

            if check_collisione(ball_x, ball_y, ball_radius, rect_x_2, rect_y_2, rect_larghezza, rect_altezza):
                ball_speed_x *= -1

            rect_y += rect_speed_y
            rect_y_2 += rect_speed_y_2

            if rect_y < 0:
                rect_y = 0
            elif rect_y + rect_altezza > SCREEN_HEIGHT:
                rect_y = SCREEN_HEIGHT - rect_altezza

            if rect_y_2 < 0:
                rect_y_2 = 0
            elif rect_y_2 + rect_altezza > SCREEN_HEIGHT:
                rect_y_2 = SCREEN_HEIGHT - rect_altezza

            pygame.draw.rect(window, pygame.Color('white'), (div_x, div_y, div_larg, div_hight))
            pygame.draw.rect(window, pygame.Color('white'), (rect_x, rect_y, rect_larghezza, rect_altezza))
            pygame.draw.rect(window, pygame.Color('white'), (rect_x_2, rect_y_2, rect_larghezza, rect_altezza))

            text_p1 = font.render(str(punti_player_1), True, (255, 255, 255))
            text_p2 = font.render(str(punti_player_2), True, (255, 255, 255))

            window.blit(text_p1, (SCREEN_WIDTH // 4, 20))
            window.blit(text_p2, (SCREEN_WIDTH * 3 // 4, 20))
            
    else:
        if game_over:
            if punti_player_1 >= punti_player_2:
                 vittoria_1(punti_player_1, punti_player_2)
            else:
                 vittoria_2(punti_player_1, punti_player_2)
        else:
            misure1 = (SCREEN_WIDTH//2) //2
            mid = (SCREEN_WIDTH//2)//2
            misure2 = (SCREEN_WIDTH//2) + mid
            title_surface = font_title.render("PONG", True, pygame.Color('white'))
            instr_surface1 = font_menu.render("Normale", True, pygame.Color(colorino1))
            instr_surface2 = font_menu.render("Competitiva", True, pygame.Color(colorino2))
            window.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, SCREEN_HEIGHT//3))
            window.blit(instr_surface1, (misure1 - instr_surface1.get_width()//2, SCREEN_HEIGHT//2))
            window.blit(instr_surface2, (misure2 - instr_surface2.get_width()//2, SCREEN_HEIGHT//2))
   



    pygame.display.update()
    clock.tick(60)


    



