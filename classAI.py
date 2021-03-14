import pygame

class AI: #sets up class
    def __init__(self, screen, array):
        self.screen = screen
        self.points = [] ##initializes list of points where direction changes
        self.directions = [] ##initializes corresponding direction changes
        self.y_down = len(array) - 2 ##stores value of direction change for y-coordinate when snake is at bottom of grid
        self.speed = 'RIGHT'
    ##builds points and directions list
    ##call once at the beginning of the game
    def buildList(self, grid): ##(array)
        ##initializes the beginning array
        self.points.append([0, 0]) 
        self.points.append([1, 0])
        self.points.append([1, self.y_down])
        self.points.append([2, self.y_down])

        ##builds list of direction changes
        for i in range(0, int(len(grid)/2)):    
            self.directions.append('RIGHT')
            self.directions.append('DOWN')
            self.directions.append('RIGHT')
            self.directions.append('UP')

        self.directions[-2] = 'LEFT' 
        ##builds list of key points
        for i in range(0, int(len(grid)/2)- 1):
            pt_1 = self.points[i*4][:]
            pt_1[0] = self.points[i*4][0] + 2
            self.points.append(pt_1)

            pt_2 = self.points[(i*4)+1][:]
            pt_2[0] = self.points[(i*4)+1][0] + 2
            self.points.append(pt_2)
            
            pt_3 = self.points[(i*4)+2][:]
            pt_3[0] = self.points[(i*4)+2][0] + 2
            self.points.append(pt_3)

            pt_4 = self.points[(i*4)+3][:]
            pt_4[0] = self.points[(i*4)+3][0] + 2
            self.points.append(pt_4)

        self.points[-1] = [0, len(grid) - 1]
        self.points[-2] = [len(grid)-1, len(grid)-1]
        return self.points, self.directions

    ##changes snekk direction based on points and directions list
    ##call in while loop in main (while game_over == False)
    def changeDirection(self, snekkPosition): ##(snekkPosition)
        if snekkPosition[0] == self.points[0]:##if snekk head reaches a key direction point
            self.speed = self.directions[0] ##change direction of snake head to corresponding direction in list
            p = self.points.pop(0) ##pop (dequeue) off first element
            d = self.directions.pop(0)
            self.points.append(p) ##push(enqueue) first element to back
            self.directions.append(d)
        return self.points, self.directions, self.speed

    def skip(self, snekkPosition, array):#(self, snekkPosition, array)
        column  = []
        for i in range(len(array) - 1):#-2 because dont want to check the last line and the index is separte
            column.append(array[i][self.points[0][0]])
            if self.points[0][0] != (len(array)-1):
                column.append(array[i][self.points[0][0]+1])
            else:
                self.changeDirection(snekkPosition)
        c1 = False if 5 in column else True
        c2 = snekkPosition[0]==self.points[0]
        c3 = self.directions[0] == 'DOWN'#if snekk head reaches a key direction point
        c4 = False if self.points[3] in snekkPosition[:-1] else True
        if(c1 == True and c2 == True and c3 == True and c4 == True):
            self.helper()
        else:
            self.changeDirection(snekkPosition)
        
    def helper(self):#skips 4 points at once
        a = self.points.pop(0)
        b = self.directions.pop(0)
        self.points.append(a)
        self.directions.append(b)
        c = self.points.pop(0)
        d = self.directions.pop(0)
        self.points.append(c)
        self.directions.append(d)
        e = self.points.pop(0)
        f = self.directions.pop(0)
        self.points.append(e)
        self.directions.append(f)
        g = self.points.pop(0)
        h = self.directions.pop(0)
        self.points.append(g)
        self.directions.append(h)
        return self.points, self.directions, self.speed

