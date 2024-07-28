#basic frame of pygame code obtained from https://www.pygame.org/docs/.
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
clicked = False

testing_rectangle = pygame.Rect(screen.get_width()/2,screen.get_height()/2,250,100)
testing_rectangle2 = pygame.Rect(screen.get_width()/3, screen.get_height()/3, 100, 100)
testing_rectangle3 = pygame.Rect(screen.get_width()/2,screen.get_height()/2,250,100)
rectangleClickCount = 0
pickUpRectangle = False

def cloneRectangle(thing):
    print("cloning")
    return thing.copy()


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
                    print("picked up")
                    pickUpRectangle = True
                    print("dropped")
                else:
                    pickUpRectangle = False
            elif testing_rectangle2.collidepoint(event.pos):
                print("wahoo")
                clicked = True

                #print(pygame.mouse.get_pos()[0])
                #print(type(pygame.mouse.get_pos()))
                #testing_rectangle = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], 250,100)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "white", testing_rectangle)
    pygame.draw.rect(screen,  "blue", testing_rectangle2)
    # RENDER YOUR GAME HERE

    #the drag rectangle function was made by Aidan Z. That's why it looks so janky.
    if pickUpRectangle == True:
        testing_rectangle = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], 250,100)
        pygame.draw.rect(screen, "white", testing_rectangle)
    if clicked == True:

        otherRect = pygame.draw.rect(screen, "white", cloneRectangle(testing_rectangle))
        #otherRect = pygame.Rect(100,100,100,100)
        #clicked = False
    elif clicked == True:
        clicked = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

