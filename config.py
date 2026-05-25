class Config():
    def __init__(self):
        # Window
        self.windowWidth = 860
        self.windowHeight = 580
        self.windowBackgroundColour = (0, 0, 0)
        
        # Game area
        self.gameAreaWidth= 660
        self.gameAreaHeight = 580
        self.gameAreaBackgroundColour = (0, 0, 0)

        # Side panel
        self.sidePanelWidth = 200 # windowX - gameX
        self.sidePanelHeight = 580 # windowY - gameY
        self.sidePanelBackgroundColour = (17, 24, 39)
        self.sidePanelTextColour = (209, 213, 219)
        self.sidePanelButtonColour = (209, 213, 219)

        # Source 
        self.sourceRadius = 15
        self.sourceColour = (103, 232, 249)

        # Rays
        self.rayAmount = 360
        self.rayLength = 1000
        self.rayColour = (255, 255, 255)

        # Obstacles
        self.obstacleDefinition = [
            [40, 40, 80, 80],
            [120, 120, 140, 140],
            [70, 360, 400, 2]
        ]
        self.obstacleColour = (100, 100, 100)
    
    # @property
    # def rayAmount(self):
    #     return self._rayAmount
    
    # @rayAmount.setter
    # def rayAmount(self, value):
    #     print(f"[CONFIG] rayAmount changed to {value}")
    #     self._rayAmount = value