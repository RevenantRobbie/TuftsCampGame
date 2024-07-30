import pygame

screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen

#objects declared
class logicGate:
    def __init__ (self, shape, pickedUp, input1, input2, output):
        self.shape = shape
        self.pickedUp = pickedUp
        self.input1 = input1
        self.input2 = input2
        self.output = output

class connectorNode:
    def __init__ (self, parent, circleLoc, inputOutput, inUse): #NOTE only circleLoc is a var here since the circle radius, color, and background remain consistent
        self.parent = parent
        self.circleLoc = circleLoc
        self.inputOutput = inputOutput
        self.inUse = inUse

#variables declared
defaultGateShape = pygame.Rect(screen.get_width()/2, screen.get_height()/2,250,100)
testingRect = pygame.Rect(screen.get_width()/4, screen.get_height()/4,100,100)
createdRectangles = []
createdCircles = []
pickedUp = False



def main():
    dragging = False
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickedOnGate = False
                #print("down")
                for shape in createdRectangles:
                    if shape.shape.collidepoint(event.pos):
                        print("clicked on gate")
                        clickedOnGate = True
                        if dragging == False:
                            dragging = True
                            shape.pickedUp = True
                            print(createdRectangles)
                        elif dragging == True:
                            dragging = False
                            shape.pickedUp = False
                if testingRect.collidepoint(event.pos):
                    print("clicked on button")
                    newShape = logicGate(defaultGateShape, False, False, False,False)
                    pygame.draw.circle(bg, "blue", (75, 0), 25)
                    pygame.draw.circle(bg, "blue", (175, 0), 25)
                    print("oaoaoao")
                    #print(inputNode2)
                    print(newShape)
                    createdRectangles.append(newShape)
                    #createdCircles.append(inputNode1)
                    #createdCircles.append(inputNode2)
                else:
                    if clickedOnGate == False:
                        print("clicked on nothing")
                        dragging == False
                        for shape in createdRectangles:
                            shape.pickedUp = False




        bg.fill((0, 0, 0))  # reset bg to black (0,0,0) screen rgb is out of 255, not 1 like rblx

        pygame.draw.rect(bg, "purple", testingRect)

        for shape in createdRectangles:
            pygame.draw.rect(bg, "white", shape.shape)

        for shape in createdRectangles:
            if dragging == True:
                if shape.pickedUp == True:
                    shape.shape = pygame. Rect (pygame.mouse.get_pos () [0], pygame.mouse.get_pos () [1], 250,100)
        # ======================
        # game stuff goes here!
        # ======================

        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()
