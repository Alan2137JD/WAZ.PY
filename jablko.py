import random
import pygame
import lekcja1

class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.kolor=(255,255,0)
        self.applePosition=(lekcja1.rozdzielczosc)
        self.randomPosition()
    def setPosition(self,x,y):
        self.applePosition=(x,y)
    def getPosition(self):
        return self.applePosition
    def randomPosition(self):
        xApple=random.randint(0,9)*40+20
        yApple=random.randint(0,9)*40+20
        self.setPosition(xApple,yApple)
    def drawApple(self,OknoGry):
        pygame.draw.circle(OknoGry,self.kolor,(self.applePosition[0],self.applePosition[1]),20)