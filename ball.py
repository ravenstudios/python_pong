import pygame
import collide

class Ball:
    """
    Ball class that creates a ball.
    All collision detections are done by this class.
    """
    def __init__(self, game_size):
        self.gs = game_size
        self.game_width = self.gs.get("width")
        self.game_height = self.gs.get("height")
        self.width = 20
        self.height = self.width
        self.x = game_size.get("width") / 2 - self.width / 2
        self.y = game_size.get("height") / 2 - self.height / 2
        self.x_speed = 2
        self.y_speed = 2
        self.color = (255, 255, 255)



    def update(self, player, cpu):
        """
        Call the update methods of each object.
        """
        self.move(player, cpu)
        self.score(player, cpu)
        self.collide(player, cpu)


    def collide(self, player, cpu):
        """
        Checks if ball has hit a paddle
        """
        if collide.collide(self, cpu) == True:
            self.x_speed = -self.x_speed
        if collide.collide(self, player):
            self.x_speed = -self.x_speed



    def reset(self, player, cpu):
        """
        -reverse ball direction
        -delays for 1000 mils
        -calls objects reset methods to center paddles
        """
        self.x_speed = -self.x_speed
        pygame.time.delay(1000)
        player.reset()
        cpu.reset()



    def score(self, player, cpu):
        """
        If ball goes past the paddles then we
        -update player score
        -centers ball 
        """
        if self.x + self.width > self.gs.get("width"):
            player.update_score()
            self.reset(player, cpu)
            self.x = self.gs.get("width") / 2 - self.width / 2

        if self.x - self.width < 0:
            cpu.update_score()
            self.reset(player, cpu)
            self.x = self.gs.get("width") / 2 - self.width / 2




    def move(self, player, cpu):
        """
        Adds velocity to the ball's x and y.
        If ball hits top or bottom, then reverse y velocity
        """
        self.x += self.x_speed
        self.y += self.y_speed

        if self.y + self.height > self.gs.get("height"):
            self.y_speed = -self.y_speed
        if self.y - self.height < 0:
            self.y_speed = -self.y_speed



    def draw(self, surface):
        """
        Draws ball to screen
        """
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.width))
