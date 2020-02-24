import player
class CPU(player.Player):


    def __init__(self, game_size):
        super().__init__(game_size)
        self.x = self.gs["width"] - self.width
        self.speed = 1

    def update(self, ball):
        self.move(ball)


    def move(self, ball):

        if ball.y > self.y + self.height / 2 and self.y + self.height < self.gs["height"]:
            self.y += self.speed
        else:
            if self.y > 0:
                self.y += -self.speed
