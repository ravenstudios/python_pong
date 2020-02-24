import pygame
import ball
import player
import cpu

game_width, game_height = 800, 600
game_size = {"width": game_width, "height": game_height}
font_size = 50

surface = pygame.display.set_mode((game_size.get("width"), game_size.get("height")))
ball = ball.Ball(game_size)
player = player.Player(game_size)
cpu = cpu.CPU(game_size);

pygame.init()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        surface.fill((0, 0, 0))
        draw()
        update()
        pygame.display.update()

    pygame.quit()



def draw():
    ball.draw(surface)
    player.draw(surface)
    cpu.draw(surface)
    draw_scores()
    draw_court()



def draw_court():
    blocks = 10
    width = 32
    height = game_size.get("height") / blocks
    gap = height / 2
    x = game_size.get("width") / 2 - width / 2
    for i in range(blocks):
        y = i * height + i * gap
        pygame.draw.rect(surface, [255, 255, 255], (x, y, width, height));



def draw_scores():
    message_display(str(player.score), game_width / 2 - font_size, font_size)
    message_display(str(cpu.score), game_width / 2 + font_size, font_size)



def update():
    ball.update(player, cpu)
    player.update(ball)
    cpu.update(ball)


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()



def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)



if __name__ == "__main__":
    main()
