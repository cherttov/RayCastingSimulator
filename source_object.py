import pygame
import math


# Source object class
class SourceObject():
    def __init__(self, root, circleRadius, position):
        self.root = root
        # Circle var
        self.circleRadius = circleRadius
        self.position = position
        # Ray var
        self.rayAmount = 36
        self.rayLength = 200

    # Rendering
    def Render(self, obstacles):
        self.DrawCircle()
        self.DrawRays(obstacles)

        pygame.draw.circle(self.root, (0, 255, 0), self.position, self.circleRadius)
    
    # Circle for rays calculations
    def DrawCircle(self):
        self.circle = pygame.Rect(0, 0, self.circleRadius * 2, self.circleRadius * 2)
        self.circle.center = self.position

    # Draw rays
    def DrawRays(self, obstacles):
        angleBetween = math.radians(360 / self.rayAmount)

        for i in range(0, self.rayAmount):
            currentAngle = i * angleBetween

            newRayX = self.circle.centerx + self.rayLength * math.cos(currentAngle)
            newRayY = self.circle.centery + self.rayLength * math.sin(currentAngle)

            newClippedRayXY = self.CollisionDetection(obstacles, newRayX, newRayY)
            newClippedRayXY = (round(newClippedRayXY[0]), round(newClippedRayXY[1]))

            pygame.draw.line(self.root, (255, 0, 255), self.circle.center, newClippedRayXY, 4)
            
    # Detect & Process collision
    def CollisionDetection(self, obstacles, _newRayX, _newRayY):
        for obstacle in obstacles:
            _clippedCords = obstacle.rect.clipline(self.circle.center, (_newRayX, _newRayY))
            if _clippedCords:
                return (_clippedCords[0])
        return (_newRayX, _newRayY)