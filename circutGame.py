import pygame

screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen

class logicGate:
    def __init__ (self, shape, pickedUp, input1, input2, output):
        self.shape = shape
        self.pickedUp = pickedUp
        self.input1 = input1
        self.input2 = input2
        self.output = output

    def togglePickedUp():
        if self.pickedUp == True:
            self.pickedUp = False
        else:
            self.pickedUp = True


defaultGateShape = pygame.Rect(screen.get_width()/2, screen.get_height()/2,250,100)
testingRect = pygame.Rect(screen.get_width()/4, screen.get_height()/4,100,100)
createdShapes = []
pickedUp = False

def main():
    pygame.init() # creates game window
    clock = pygame.time.Clock() # creates needed clock object
    bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen. bg stands for background in this case
    # bg = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # creates fullscreen version
    # bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE) # creates resizable version

    while True: # game runs until user decides to end it
        clock.tick(30)  # set FPS

        for event in pygame.event.get(): # check for input
            if event.type == pygame.QUIT: # closes program if X in top right clicked
                exit() # this function call closes the program
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.mouse.get_pressed():
                if testingRect.collidepoint(event.pos):
                    newShape = logicGate(defaultGateShape, False, False, False,False)
                    createdShapes.append(newShape)
                for shape in createdShapes:
                    if shape.shape.collidepoint(event.pos):
                        print(shape)

        bg.fill((0, 0, 0))  # reset bg to black (0,0,0) screen rgb is out of 255, not 1 like rblx

        pygame.draw.rect(bg, "purple", testingRect)

        for shape in createdShapes:
            pygame.draw.rect(bg, "white", shape.shape)
        # ======================
        # game stuff goes here!
        # ======================

        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()
