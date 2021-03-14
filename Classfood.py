import random
import pygame
from pprint import pprint

class Food:#setting up the food class
    def __init__(self, screen):
        self.screen = screen
        self.size_x = 1 #1 block on the screen will be converted to appropriate pickel number
        self.size_y = 1
        self.food_value = 20
        self.food_location = []
        self.score = 0
        
    def location(self, other):#location(self, array)
        '''
        check that we are not spanning the food on the snekk
        changes the loctaion of the food to a random position & gives the coordinates of it back
        '''
        while True:
            x = random.randint(0, len(other)-1)
            y = random.randint(0, len(other)-1)
            if other[y][x] == 0:
                other[y][x] = 5
                break
        self.food_location = [y, x]
        return self.food_location, other
    
    
    def draw(self, other):#draw(self, array)
        if self.food_location == []:
            self.location(other)
        #spans food at random position, draws the square & updates screen to appear at given location
        pygame.draw.rect(self.screen, (200, 200, 250), [self.food_location[1]*40, self.food_location[0]*40, self.size_x*40, self.size_y*40]) #BOARD_SIZE
        

    def food_score(self, other, second, position):#food_score(self, array, head(of the snekk)[x, y], snekkPosition)
        food_value = 20
        #check if the head of snekk is at food location meaning it ate it and adds points
        if second == self.food_location:
            self.score += self.food_value
            other[self.food_location[0]][self.food_location[1]] = 1
            self.location(other)
            position.append([position[-1][0],position[-1][1]])
        return self.score
    
    
