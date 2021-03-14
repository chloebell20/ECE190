import pygame
from Classsnekk import *
from Classfood import *
from classAI import *


pygame.init()#initializes the game
screen = pygame.display.set_mode((440, 440))#sets a screen size
pygame.display.update()
#clock = pygame.time.Clock()
#clock.tick(1000)#for testing slower, when done testing can remove clock or change it to 25

def draw_array():
    '''
    draw_screen will create the dimentional array made of a list with nested lists
    the number of nested lists which reprersents the number of rows and the length of each nested list represents the number of columns.
    the array is initialised with 0 and when the snake is on that position, then the number is updated to a 1
    '''
    array = []
    for i in range(0, 10): #BOARD_SIZE
        array.append([])
    for i in range(0, 10): #BOARD_SIZE
        for j in range(0, 10): #BOARD_SIZE
            array[i].append(0)
    return array
array = draw_array()

food = Food(screen)
snekk = Snekk(screen)
AI = AI(screen, array)
pygame.display.set_caption("Snekk by Stephanie Gao and Chloe Bell")


def draw_background(screen):
    #display of the screen
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 440, 440))#black screen
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, 400, 400))#grey screen inside is where snekk is alive, show boarders
draw_background(screen)

#build the list for the points
AI.buildList(array)

half_board = ((len(array))**2)/2#want half the size of the board
game_over = False #allows to escape the loop to end the game    
while not game_over:
    if len(snekk.snekkPosition) < int(half_board):
        AI.skip(snekk.snekkPosition, array)
        if AI.speed == 'LEFT' and snekk.speed != 'RIGHT':
            snekk.speed = 'LEFT'
        if AI.speed == 'RIGHT' and snekk.speed != 'LEFT':
            snekk.speed = 'RIGHT'
        if AI.speed == 'DOWN' and snekk.speed != 'UP':
            snekk.speed = 'DOWN'
        if AI.speed == 'UP' and snekk.speed != 'DOWN':
            snekk.speed = 'UP'
    if len(snekk.snekkPosition) == (len(array)**2)-1:
        game_over = True
    else:
        AI.changeDirection(snekk.snekkPosition)
        if AI.speed == 'LEFT' and snekk.speed != 'RIGHT':
            snekk.speed = 'LEFT'
        if AI.speed == 'RIGHT' and snekk.speed != 'LEFT':
            snekk.speed = 'RIGHT'
        if AI.speed == 'DOWN' and snekk.speed != 'UP':
            snekk.speed = 'DOWN'
        if AI.speed == 'UP' and snekk.speed != 'DOWN':
            snekk.speed = 'UP'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#quits the game when user exits (the x top right of screen)
            game_over = True
            '''#code below allows to take the human input and make snekk move acordingly
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snekk.speed != 'RIGHT':
                    snekk.speed = 'LEFT'
                if event.key == pygame.K_RIGHT and snekk.speed != 'LEFT':
                    snekk.speed = 'RIGHT'
                if event.key == pygame.K_DOWN and snekk.speed != 'UP':
                    snekk.speed = 'DOWN'
                if event.key == pygame.K_UP and snekk.speed != 'DOWN':
                    snekk.speed = 'UP'
            '''
                
    draw_background(screen)
    food.draw(array)
    snekk.draw()
    s = food.food_score(array, snekk.head, snekk.snekkPosition)
    condition1 = snekk.move(array, game_over)
    condition = snekk.alive(array, game_over, food.food_location)
    s1 = snekk.score(food, game_over)
    pygame.time.delay(0)#stops the screen flikering
    if condition[1] == True or condition1[3] == True:
        game_over = True

def total_score(s, s1): #sums the Moogle score and the score for the snake moving, use s and s1 b/c call on functions and what they return
    total_score = s + s1
    return total_score
        
def end_screen():
    pygame.init()
    screen1 = pygame.display.set_mode((440, 440))
    pygame.display.update()
    font = pygame.font.SysFont("comicsansms", 30) #writting type, size
    message = font.render("GAME OVER!!!", True, (0, 255, 255))# message, bool??? had a 5 before can't find what it is, colour
    screen1.blit(message, (200, 200))###need to figure out the location because screen size will change!!!!!!!!!!!!
    end_score = font.render("End score: " + str(total_score(s, s1)), True, (178, 34, 34))##############doesn't print the actual score
    screen1.blit(end_score, (100, 400))#display on end screen, need to find location too!!!!!!!!!!
    pygame.time.delay(100)
    pygame.display.update()
    pygame.quit()
if game_over == True:
    end_screen()
print(total_score(s, s1))
pygame.quit()#closes screen
quit()
