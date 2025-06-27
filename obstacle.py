import pygame


# Obstacle class
class Obstacle():
    def __init__(self, root, positionArray):
        self.root = root
        self.positionArray = positionArray
        self.rect = pygame.Rect(positionArray)

        self.Render()
    
    # Rendering
    def Render(self):
        pygame.draw.rect(self.root, (100, 100, 100), self.rect)