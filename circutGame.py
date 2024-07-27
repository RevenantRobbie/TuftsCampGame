#basic frame of pygame code obtained from https://www.pygame.org/docs/.
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

testing_rectangle = pygame.Rect(screen.get_width()/2,screen.get_height()/2,250,100)
rectangleClickCount = 0
pickUpRectangle = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #thank you to https://medium.com/@01one/how-to-create-clickable-button-in-pygame-8dd608d17f1b for providing help with the code


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.mouse.get_pressed():
            if testing_rectangle.collidepoint(event.pos):
                rectangleClickCount += 1
                if rectangleClickCount % 2 == 1:
                    pickUpRectangle = True
                else:
                    pickUpRectangle = False
                #print(pygame.mouse.get_pos()[0])
                #print(type(pygame.mouse.get_pos()))
                #testing_rectangle = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], 250,100)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "white", testing_rectangle)
    # RENDER YOUR GAME HERE

    while pickUpRectangle == True:
        testing_rectangle = testing_rectangle = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], 250,100)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

