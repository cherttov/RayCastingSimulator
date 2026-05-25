import pygame
from obstacle import Obstacle
from source_object import SourceObject
from config import Config
from side_panel import SidePanel


# Application main
class AppWindow():
    # Constructor
    def __init__(self, config):
        # Config
        self.config = config

        # Window
        pygame.init()
        self.window = pygame.display.set_mode((self.config.windowWidth, self.config.windowHeight))
        self.clock = pygame.time.Clock()
        self.running = True

        # Init var
        self.isDragging = False

        # Initialize Source
        self.sourcePosition = (300, 200)
        self.sourceRadius = 15
        self.source = SourceObject(self.window, self.sourceRadius, self.sourcePosition, self.config)

        # Initialize Obstacles
        self.obstacles = [Obstacle(self.window, rect) for rect in self.config.obstacleDefinition]

        # Initialize SidePanel
        self.sidePanel = SidePanel(self.window, self.config)

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
        # Set & clamp source position to mouse position
        _mouseX, _mouseY = pygame.mouse.get_pos()
        _windowX, _windowY = (self.config.gameAreaWidth, self.config.gameAreaHeight)

        _positionLimitX = min(max(_mouseX, 0), _windowX)
        _positionLimitY = min(max(_mouseY, 0), _windowY)
        
        self.source.position = (_positionLimitX, _positionLimitY)

        # Debug
        # print(pygame.mouse.get_pos())

    # Rendering
    def Render(self):
        self.window.fill(self.config.windowBackgroundColour)

        self.source.Render(self.obstacles)

        for obstacle in self.obstacles:
            obstacle.Render()

        self.sidePanel.Render()

        pygame.display.flip()