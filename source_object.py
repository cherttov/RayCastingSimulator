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
        _linesCoordinates = []

        angleBetween = math.radians(360 / self.rayAmount)

        for i in range(0, self.rayAmount):
            currentAngle = i * angleBetween

            _newRayX = self.circle.centerx + self.rayLength * math.cos(currentAngle)
            _newRayY = self.circle.centery + self.rayLength * math.sin(currentAngle)

            # _newRayX = lastRayX * math.cos(math.radians(currentAngle)) - lastRayY * math.sin(math.radians(currentAngle))
            # _newRayY = lastRayX * math.sin(math.radians(currentAngle)) + lastRayY * math.cos(math.radians(currentAngle))

            pygame.draw.line(self.root, (255, 0, 255), self.circle.center, (_newRayX, _newRayY), 4)
            _linesCoordinates.append((_newRayX, _newRayY))

        self.CollisionDetection(obstacles, _linesCoordinates)

    # Detect collissions
    def CollisionDetection(self, obstacles, lines):
        for obstacle in obstacles:
            for line in lines:
                _clippedCords = obstacle.rect.clipline(self.circle.center, line)
                if _clippedCords:
                    print(_clippedCords)