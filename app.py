import pygame
import math
from obstacle import Obstacle
from source_object import SourceObject
from config import Config


# Application main
class AppWindow():
    # Constructor
    def __init__(self, config):
        self.config = config

        pygame.init()
        self.window = pygame.display.set_mode((640, 460))
        self.clock = pygame.time.Clock()
        self.running = True

        self.isDragging = False

        # Initialize Source
        self.sourcePosition = (300, 200)
        self.sourceRadius = 15
        self.source = SourceObject(self.window, self.sourceRadius, self.sourcePosition, config)

        # Initialize obstacles
        self.obstacles = [Obstacle(self.window, rect) for rect in self.config.obstacleDefinition]

        self.Run()
    
    # Application running code
    def Run(self):
        while self.running:
            self.UserInput()
            self.Render()

            self.clock.tick(60)
        
        pygame.quit()
    
    # User input
    def UserInput(self):
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                self.running = False
            # Drag on mouse button down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if _mousePosition in LightSourceCircle -> move function
                if event.button == 1:
                    self.isDragging = True
            # Undrag on mouse button up
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.isDragging = False

        # Drag event 
        if self.isDragging:
            self.Dragging()
    
    # Dragging
    def Dragging(self):
        # Set source position to mouse position
        self.source.position = pygame.mouse.get_pos()

        # Limits width (r, l)
        if pygame.mouse.get_pos()[0] > self.window.get_width():
            self.source.position = (self.window.get_width(), pygame.mouse.get_pos()[1])
        if pygame.mouse.get_pos()[0] < 0:
            self.source.position = (0, pygame.mouse.get_pos()[1])

        # Limits height (u, d)
        if pygame.mouse.get_pos()[1] > self.window.get_height():
            self.source.position = (pygame.mouse.get_pos()[0], self.window.get_height())
        if pygame.mouse.get_pos()[1] < 0:
            self.source.position = (pygame.mouse.get_pos()[0], 0)

        # Limits corners (br, tr, bl, tl)
        if pygame.mouse.get_pos()[0] > self.window.get_width() and pygame.mouse.get_pos()[1] > self.window.get_height():
            self.source.position = (self.window.get_width(), self.window.get_height())
        if pygame.mouse.get_pos()[0] > self.window.get_width() and pygame.mouse.get_pos()[1] < 0:
            self.source.position = (self.window.get_width(), 0)
        if pygame.mouse.get_pos()[0] < 0 and pygame.mouse.get_pos()[1] > self.window.get_height():
            self.source.position = (0, self.window.get_height())
        if pygame.mouse.get_pos()[0] < 0 and pygame.mouse.get_pos()[1] < 0:
            self.source.position = (0, 0)

        # Updated limits - optimize a bit further before replacing it with this
        # _positionLimitX = min(max(pygame.mouse.get_pos()[0], 0), self.window.get_width())
        # _positionLimitY = min(max(pygame.mouse.get_pos()[1], 0), self.window.get_height())
        # self.source.position = (_positionLimitX, _positionLimitY)

        # Debug
        # print(pygame.mouse.get_pos())

    # Rendering
    def Render(self):
        self.window.fill("black")

        self.source.Render(self.obstacles)

        for obstacle in self.obstacles:
            obstacle.Render()

        pygame.display.flip()