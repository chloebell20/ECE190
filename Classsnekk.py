import pygame
import random
from Classfood import Food
from pprint import pprint

class Snekk: # setting up class
    def __init__ (self, screen):
        self.screen = screen
        self.snekkPosition = [[0,0]] # list of indices containing position of snake on board
        self.speed = 'RIGHT'
        self.snekk_score = 0
        self.timeout_counter = 0
        self.head = [self.snekkPosition[0][1], self.snekkPosition[0][0]]#coordinates of the head of snekk

    def move(self, other, game):#move(self, array, game_over)
######NOTE that snekkPosition has position y at index 0 and position x at index 1####
        for i in range(len(self.snekkPosition)-1, 0, -1): # starts at snake tail, ends at snake head
            self.snekkPosition[i] = [self.snekkPosition[i-1][0], self.snekkPosition[i-1][1]]# moves each snake coordinate to one before it, starting from tail
  
        for i in range(len(other)):#sets everything back to a 0, execpt for the food location
            for j in range(len(other)):
                if other[i][j] == 5:
                    continue
                else:
                    other[i][j] = 0
        
        if self.speed == 'RIGHT':
            self.snekkPosition[0][0] += 1
        if self.speed == 'LEFT':
            self.snekkPosition[0][0] -= 1
        if self.speed == 'UP':
            self.snekkPosition[0][1] -= 1
        if self.speed == 'DOWN':
            self.snekkPosition[0][1] += 1
            
        for i in range(len(self.snekkPosition)):
            if (self.snekkPosition[0][0] > len(other)-1) or (self.snekkPosition[0][1] >  len(other)-1):
                game = True
            else:
                other[self.snekkPosition[i][1]][self.snekkPosition[i][0]] = 1
        self.head = [self.snekkPosition[0][1], self.snekkPosition[0][0]]
        return self.snekkPosition, other, self.head, game

    def alive(self, other, over, food_loc):#alive(self, array, game_over, food_location)
        #if snake is out of bounds
        if (self.snekkPosition[0][0] <= -1) or (self.snekkPosition[0][1] <= -1):
            over = True            
            
        #if snake touches itself        
        for i in range(1, len(self.snekkPosition)):
            if over == True:
                pass
            else:
                if self.snekkPosition[0][0] == self.snekkPosition[i][0] and self.snekkPosition[0][1] == self.snekkPosition[i][1]:#end game on the page with current score
                    over = True

        #timeout
        cycle_allowance = 1.5
        time_out = (4*(len(other)) - 4) * cycle_allowance
        if over != True:
            if self.head == food_loc:
                self.timeout_counter = 0
            self.timeout_counter += 1
            if self.timeout_counter == time_out:
                over = True
        return self.timeout_counter, over

    def score(self, other, andanotherone):#score(food, game_over)
        if andanotherone == True:
            pass
        else:#if move() is called (and returns True)
            self.snekk_score += 1
        return self.snekk_score

    def draw(self):
        for i in range(len(self.snekkPosition)):
            #blit screen, update screen, clear previous output and put new output
            
            pygame.draw.rect(self.screen, (255, 255, 255), [(self.snekkPosition[i][0])*40, (self.snekkPosition[i][1])*40, 40, 40]) #BOARD_SIZE
        pygame.display.update()
    



                
                                    
           
        
        
        
        
