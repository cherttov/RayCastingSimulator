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
    def CollisionDetection(self, obstacles, _newRayX, _newRayY): # still buged where it goes through 1 pixel
        _lastClipped = ()
        for _obstacle in obstacles:
            _newClipped = _obstacle.rect.clipline(self.circle.center, (_newRayX, _newRayY))
            if _newClipped:
                _newClipped = _newClipped[0]
                if not _lastClipped:
                    _lastClipped = _newClipped
                else:
                    _lastDistance = math.sqrt(((_lastClipped[0]-self.circle.center[0])**2)+((_lastClipped[1]-self.circle.center[1])**2))
                    _newDistance = math.sqrt(((_newClipped[0]-self.circle.center[0])**2)+((_newClipped[1]-self.circle.center[1])**2))
                    if _newDistance < _lastDistance:
                        _lastClipped = _newClipped
        if _lastClipped:
            return _lastClipped
        else:
            return (_newRayX, _newRayY)