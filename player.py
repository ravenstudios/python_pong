import pygame

class Player:


    def __init__(self, game_size):
        self.gs = game_size
        self.width = 30
        self.height = 175
        self.x = 0
        self.y = game_size.get("height") / 2 - self.height / 2
        self.speed = 5
        self.color = (255, 255, 255)
        self.score = 0

    def update(self, ball):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.y > 0:
                self.y += -self.speed
        if keys[pygame.K_DOWN]:
            if self.y + self.height < self.gs.get("height"):
                self.y += self.speed

    def reset(self):
        self.y = self.gs.get("height") / 2 - self.height / 2

    def update_score(self):
        self.score += 1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
