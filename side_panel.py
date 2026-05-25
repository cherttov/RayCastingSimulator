import pygame
import pygame_widgets


class SidePanel():
    def __init__(self, root, config):
        self.root = root

        # Config
        self.config = config

        # Side Panel
        self.sidePanelRectangle = pygame.Rect(self.config.gameAreaWidth, 0, self.config.sidePanelWidth, self.config.sidePanelHeight)

        # Container
        self.elementsAmount = 10
        self.elementHeight = int(self.config.sidePanelHeight / self.elementsAmount)

        _getElementPositions = lambda i: (self.config.gameAreaWidth + 16, i * self.elementHeight + 16)
        self.elementRowsDefinition = [_getElementPositions(i) for i in range(self.elementsAmount)]

        # Text
        self.font = pygame.font.Font(None, 24)
        self.textColour = self.config.sidePanelTextColour

        # Button

        # Slider


        self.Render()

    # Rendering
    def Render(self):
        pygame.draw.rect(self.root, self.config.sidePanelBackgroundColour, self.sidePanelRectangle)
        pygame_widgets.update(pygame.event.get())
        self.RenderElements()
        
    
    # Text/Buttons/Sliders rendering
    def RenderElements(self):
        textRayAmount = self.TextTemplate("Number of rays:", self.elementRowsDefinition[0])
        textRayLength = self.TextTemplate("Length of rays:", self.elementRowsDefinition[2])

    # Text
    def TextTemplate(self, _text, _location):
        text = self.font.render(_text, True, self.textColour)
        self.root.blit(text, _location)

    # Button
    def ButtonTemplate(self):
        pass

    # Slider
    def SliderTemplate(self):
        pass
        