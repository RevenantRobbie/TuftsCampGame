#basic frame of pygame code obtained from https://www.pygame.org/docs/.
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

testing_rectangle = pygame.Rect(screen.get_width()/2,screen.get_height()/2,250,100)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "white", testing_rectangle)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

