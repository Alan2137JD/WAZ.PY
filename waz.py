from tkinter import Y
from typing_extensions import Self
import pygame

class Snake():

    #konstruktor klasy
    def __init__(self):
        self .dlugosc=1
        self .punkty=0
        self .pozycje=[(120,120)]
    def getHead(self):
        return self .pozycje[-1]
    def eating(self):
        self .dlugosc+=1
        self .punkty+=1
    def drawSnake(self, OknoGry):
        for wspolrzendne in self.pozycje[::-1]: 
            wazShape=pygame.Rect((wspolrzendne[0],wspolrzendne[1]),(40,40))
            pygame.draw.rect(OknoGry,(255,192,203),wazShape)
    def snakeMouve(self,x,y):

        #dodanie nowej pozycji weza
        self.pozycje.append(x.y)
        if self.dlugosc<len(self.pozycje):
            del self.pozycje[0]

        #sprawdzenie czy wąż sam siebie nie zjadł
        for wspol in self.pozycje[::]:
            if x==wspol[0] and y==wspol[1]:
                self.pozycje=[]
                self.dlugosc=1
                punkty=0

        #dodawanie nowej pozycji węża
        self.pozycje.append((x,y))
        if self.dlugosc<len(self.pozycje):
            del self.pozycje[0]