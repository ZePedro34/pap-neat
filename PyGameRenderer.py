import pygame

from WorldState import WorldState

class PyGameRenderer:
    def __init__(self, showGrid = True) -> None:
        pygame.init()
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()

        self.showGrid = showGrid

    def destroy(self) -> None:
        pygame.quit


    def render(self, ws: WorldState) -> None:
        for event in pygame.event.get():
            None
        self.screen.fill("white")

        cellWidth = self.screenWidth / ws.numCols
        cellHeight = self.screenHeight / ws.numRows

        if (self.showGrid):
            for i in range(ws.numCols):
                for j in range(ws.numRows):
                    pygame.draw.rect(self.screen, "black", (i*cellWidth, j*cellHeight, cellWidth, cellHeight), 1)

        for p in ws.preys:
            pygame.draw.circle(self.screen, "red", (p.posX*cellWidth + cellWidth/2, p.posY*cellHeight + cellHeight/2), cellWidth/3)

        for f in ws.food:
            pygame.draw.circle(self.screen, "purple", (f.posX*cellWidth + cellWidth/2, f.posY*cellHeight + cellHeight/2), cellWidth/4)



        
        pygame.display.flip()
        #self.clock.tick(framerate)
        