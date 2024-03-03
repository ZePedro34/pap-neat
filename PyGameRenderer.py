import math
import pygame
from MathUtils import getAngDegrees
from WorldState import WorldState

class PyGameRenderer:
    def __init__(self, showGrid = True) -> None:
        pygame.init()
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()

        self.carImg = pygame.image.load('assets/racecar.png')
        self.carImgScale = 40
        self.carImg = pygame.transform.scale(self.carImg, (self.carImgScale, self.carImgScale))
        self.carImg = pygame.transform.rotate(self.carImg, -90)

    def destroy(self) -> None:
        pygame.quit


    def render(self, ws: WorldState) -> None:
        for event in pygame.event.get():
            None
        self.screen.fill("white")

        for p in ws.preys:
            preyScreen = self.world2Screen(p.transform.pos, ws)
            carRotated = pygame.transform.rotate(self.carImg, getAngDegrees(p.transform.ori))
            self.screen.blit(carRotated, (preyScreen[0]-self.carImgScale/2, preyScreen[1]-self.carImgScale/2))

        for f in ws.food:
            foodScreen = self.world2Screen(f.pos, ws)
            pygame.draw.circle(self.screen, "purple", foodScreen, 10)

        for p in ws.predators:
            predatorScreen = self.world2Screen(p.transform.pos, ws)
            pygame.draw.circle(self.screen, "red", predatorScreen, 15)

        
        pygame.display.flip()
        #self.clock.tick(framerate)
    
    def world2Screen(self, pos, ws: WorldState):
        return (pos[0]+abs(ws.min[0]), -pos[1]+abs(ws.min[1]))