import pygame

screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen
bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen. bg stands for background in this case
#objects declared
class logicGate:
    def __init__ (self, shape, pickedUp, input1, input2, output):
        self.shape = shape
        self.pickedUp = pickedUp
        self.input1 = input1
        self.input2 = input2
        self.output = output

class connectorNode:
    def __init__ (self, shape ,parent, inputOutput, inUse): #NOTE only circleLoc is a var here since the circle radius, color, and background remain consistent
        self.parent = parent
        self.shape = shape #idk if this is nessecary
        self.inputOutput = inputOutput
        self.inUse = inUse

    def redrawSelf(self):
        #TODO certain shapes may only have 1 input, scan self.parent to see how many inputs/outputs it has and adjust positions accordingly
        if self.inputOutput == "input1":
            self.shape = pygame.Rect(self.parent.shape[0]+75, self.parent.shape[1]+100, 15, 15)
        elif self.inputOutput == "input2":
            self.shape = pygame.Rect(self.parent.shape[0]+175, self.parent.shape[1]+100, 15, 15) #input2
        elif self.inputOutput == "output":
            self.shape = pygame.Rect(self.parent.shape[0]+125, self.parent.shape[1]-15, 15, 15)
        pygame.draw.rect(bg, "blue", self.shape)


#variables declared
defaultGateShape = pygame.Rect(screen.get_width()/2, screen.get_height()/2,250,100)
defaultNodeShape = pygame.Rect(0, 0, 15, 15)
testingRect = pygame.Rect(screen.get_width()/4, screen.get_height()/4,100,100)
createdRectangles = []
createdNodes = []
inUse = False #checks if the mouse is doing something so it can't do 2 things at once



def main():
    dragging = False
    pygame.init() # creates game window
    clock = pygame.time.Clock() # creates needed clock object

    # bg = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # creates fullscreen version
    # bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE) # creates resizable version

    while True: # game runs until user decides to end it
        clock.tick(30)  # set FPS

#---events---
        for event in pygame.event.get(): # check for input
            if event.type == pygame.QUIT: # closes program if X in top right clicked
                exit() # this function call closes the program
#---m1 event---
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickedOnGate = False
                #TODO check if circle nodes are clicked on

                #TODO drop logic on m1 click on anything. This can probably be done by changing pickedUp/inUse whenever a m1 event takes place.

                for shape in createdNodes:
                    if shape.shape.collidepoint(event.pos):

                        if shape.inUse == False: #create wire
                            print(shape)
                            print(shape.inUse)
                            shape.inUse = True
                        else: #sever connection
                            shape.inUse = False
                            print(shape.inUse)

                for shape in createdRectangles: #check if rectangles are clicked on
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

                if testingRect.collidepoint(event.pos): #check if spawning rectangle is clicked on
                    print("clicked on button")
                    newShape = logicGate(defaultGateShape, False, False, False,False)
                    newInput1 = connectorNode(defaultNodeShape, newShape, "input1", False)
                    newInput2 = connectorNode(defaultNodeShape, newShape, "input2", False)
                    newOutput = connectorNode(defaultNodeShape, newShape, "output", False)

                    createdRectangles.append(newShape)
                    createdNodes.append(newInput1)
                    createdNodes.append(newInput2)
                    createdNodes.append(newOutput)
                else: #check if nothing was clicked on
                    if clickedOnGate == False:
                        print("clicked on nothing")
                        dragging == False
                        for shape in createdRectangles:
                            shape.pickedUp = False


#---create or recreate all shapes---
        bg.fill((0, 0, 0))  # reset bg to black (0,0,0) screen rgb is out of 255, not 1 like rblx

        pygame.draw.rect(bg, "purple", testingRect)

        for shape in createdNodes:
            shape.redrawSelf()

        for shape in createdRectangles:
            pygame.draw.rect(bg, "white", shape.shape)
            #TODO make circles a seperate class where you can click on them and drag a line to other circles

        for shape in createdRectangles:
            if dragging == True:
                if shape.pickedUp == True:
                    shape.shape = pygame.Rect (pygame.mouse.get_pos () [0], pygame.mouse.get_pos () [1], 250,100)


        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()
