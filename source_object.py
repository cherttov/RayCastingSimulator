import pygame
import math


# Source object class
class SourceObject():
    def __init__(self, window, circleRadius, position, config):
        self.config = config
        # Root
        self.window = window
        # Circle var
        self.circleRadius = circleRadius
        self.position = position
        # Ray var
        self.rayAmount = self.config.rayAmount
        self.rayLength = self.config.rayLength
        self.rayColour = self.config.rayColour

    # Rendering
    def Render(self, obstacles):
        print(self.position)
        self.DrawCircle()
        self.DrawRays(obstacles)

        pygame.draw.circle(self.window, (0, 255, 0), self.position, self.circleRadius)
    
    # Circle for rays calculations
    def DrawCircle(self):
        self.circle = pygame.Rect(0, 0, self.circleRadius * 2, self.circleRadius * 2)
        self.circle.center = self.position

    # Draw rays
    def DrawRays(self, obstacles):
        angleBetween = math.radians(360 / self.rayAmount)

        for i in range(0, self.rayAmount):
            currentAngle = i * angleBetween

            # Calculate end position of 'ray'
            newRayX = self.circle.centerx + self.rayLength * math.cos(currentAngle)
            newRayY = self.circle.centery + self.rayLength * math.sin(currentAngle)

            # If collided -> clip it to the collision point & Round it for rendering purposes
            newClippedRayXY = self.CollisionDetection(obstacles, newRayX, newRayY)
            newClippedRayXY = (round(newClippedRayXY[0]), round(newClippedRayXY[1]))

            pygame.draw.line(self.window, self.rayColour, self.circle.center, newClippedRayXY, 1)
            
    # Detect & Process collision
    def CollisionDetection(self, obstacles, _newRayX, _newRayY):
        # # Works partially
        # for i in range(1, len(obstacles)):
        #     _clippedCords1 = obstacles[i-1].rect.clipline(self.circle.center, (_newRayX, _newRayY))
        #     _clippedCords2 = obstacles[i].rect.clipline(self.circle.center, (_newRayX, _newRayY))
        #     if not _clippedCords1 and _clippedCords2:
        #         break
        #     elif not _clippedCords2:
        #         if _clippedCords1:
        #             return (_clippedCords1[0])
        #     elif not _clippedCords1:
        #         if _clippedCords2:
        #             return (_clippedCords2[0])

        #     if _clippedCords1 and _clippedCords2:
        #         ggs1 = _clippedCords1[0][0]
        #         ggs2 = _clippedCords1[0][1]
        #         qqs1 = _clippedCords2[0][0]
        #         qqs2 = _clippedCords2[0][1]
        #         pos = self.position
        #         idk1 = math.sqrt(((pos[0]-ggs1)**2)+((pos[1]-ggs2)**2))
        #         idk2 = math.sqrt(((pos[0]-qqs1)**2)+((pos[1]-qqs2)**2))
        #         print(_clippedCords1, _clippedCords2)
        #         if idk1 < idk2:
        #             return (_clippedCords1[0])
        #         elif idk1 > idk2:
        #             return (_clippedCords2[0])
        #         else:
        #             return (_newRayX, _newRayY)
        # return (_newRayX, _newRayY)
    
        for _obstacle in obstacles:
            _clippedCords = _obstacle.rect.clipline(self.circle.center, (_newRayX, _newRayY))
            if _clippedCords:
                return (_clippedCords[0])
        return (_newRayX, _newRayY)