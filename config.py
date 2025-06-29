class Config():
    def __init__(self):
        # Rays
        self.rayAmount = 36
        self.rayLength = 800
        self.rayColour = (255, 255, 255)

        # Obstacles
        self.obstacleDefinition = [
            [40, 40, 80, 80],
            [120, 120, 140, 140]
        ]
    
    # @property
    # def rayAmount(self):
    #     return self._rayAmount
    
    # @rayAmount.setter
    # def rayAmount(self, value):
    #     print(f"[CONFIG] rayAmount changed to {value}")
    #     self._rayAmount = value