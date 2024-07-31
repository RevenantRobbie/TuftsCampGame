#this code is held together by sticks duct tape and prayers
#going to attempt a topilogical sort like the one depicted here https://www.geeksforgeeks.org/topological-sorting/

import pygame

screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen
bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen. bg stands for background in this case



def andGate(input1, input2):
    #print("AND:", input1, input2)
    return input1 and input2

def orGate(input1, input2):
    if input1 or input2:
        return True
    else:
        return False

def notGate(input1, input2):
    if input1 or input2:
        return False
    else:
        return True

def norGate(input1, input2):
    return notGate(orGate(input1, input2), 0)

def nandGate(input1,input2):
    return notGate(andGate(input1, input2),0)

def xorGate(input1, input2):
    return (input1 or input2) and not (input1 == input2)

def xnorGate(input1, input2):
    return notGate(xorGate(input1, input2),0)
#


#objects declared
class logicGate:
    def __init__ (self, type, shape, pickedUp, processingInfo, idx):
        self.shape = shape
        self.type = type
        self.pickedUp = pickedUp
        self.processingInfo = processingInfo
        self.idx = idx

        #detects if gate only has one input and deletes one of the two input if so
    def doLogic(self):
        #print("doingLogic")
        if self.type == "AND":
            self.processingInfo[2] = andGate(self.processingInfo[0], self.processingInfo[1])
        elif self.type == "OR":
            self.processingInfo[2] = orGate(self.processingInfo[0], self.processingInfo[1])
        elif self.type == "NOT":
            self.processingInfo[2] = notGate(self.processingInfo[0], self.processingInfo[1])
        elif self.type == "NOR":
            self.processingInfo[2] = norGate(self.processingInfo[0], self.processingInfo[1])
        elif self.type == "NAND":
            self.processingInfo[2] = nandGate(self.processingInfo[0], self.processingInfo[1])
        elif self.type == "XOR":
            self.processingInfo[2] = xorGate(self.processingInfo[0], self.processingInfo[1])
        elif self.type == "XNOR":
            self.processingInfo[2] = xnorGate(self.processingInfo[0], self.processingInfo[1])
        else:
            print("no logic done")






#TODO create differentiation between input to output in use
class connectorNode:
    def __init__ (self, shape ,parent, inputOutput, inUse): #NOTE only circleLoc is a var here since the circle radius, color, and background remain consistent
        self.parent = parent
        self.shape = shape #idk if this is nessecary
        self.inputOutput = inputOutput
        self.inUse = inUse

    def redrawSelf(self):
        #TODO certain shapes may only have 1 input, scan self.parent to see how many inputs/outputs it has and adjust positions accordingly
        if self.inputOutput == "input1":
            self.shape = pygame.Rect(self.parent.shape[0] + self.parent.shape[2]*0.25, self.parent.shape[1]+ self.parent.shape[3], 15, 15)
        elif self.inputOutput == "input2":
            self.shape = pygame.Rect(self.parent.shape[0]+ self.parent.shape[2]*0.75, self.parent.shape[1]+ self.parent.shape[3], 15, 15) #input2
        elif self.inputOutput == "output":
            self.shape = pygame.Rect(self.parent.shape[0] + self.parent.shape[2]*0.5, self.parent.shape[1]-15, 15, 15)
        pygame.draw.rect(bg, "blue", self.shape)



    def returnSelf(self):
        return self



class wires:
    def __init__ (self, startPoint, endPoint, pickedUp, startConnectionType):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.pickedUp = pickedUp
        self.startConnectionType = startConnectionType
    def drawLine(self):
        if self.pickedUp == False:
            pygame.draw.line(bg, "orange", (self.startPoint.shape[0], self.startPoint.shape[1]),(self.endPoint.shape[0], self.endPoint.shape[1]), 3)
        elif self.pickedUp == True:
            pygame.draw.line(bg, "orange", (self.startPoint.shape[0], self.startPoint.shape[1]), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]),3)

    def updateGates(self):
        print("updating")
        if isinstance(self.endPoint, connectorNode) and isinstance(self.startPoint, connectorNode):
            if self.startPoint.inputOutput[0] == "o":
                #print(self.startPoint.parent.processingInfo)
                self.endPoint.parent.processingInfo[int(self.endPoint.inputOutput[-1])-1] = self.startPoint.parent.processingInfo[2]
            else:
                self.startPoint.parent.processingInfo[int(self.startPoint.inputOutput[-1]) -1] = self.endPoint.parent.processingInfo[2]
        else:
            return

class output:
    def __init__(self, shape, processingInfo, color):
        self.shape = shape
        self.processingInfo = processingInfo
        self.color = color

    def changeColor(self):
        #print(self.processingInfo)
        if self.processingInfo[0] == True:
            self.color = "green"
        elif self.processingInfo[0] == False:
            self.color = "red"

currentIndex = 1

def main():

    #variables declared
    defaultGateShape = pygame.Rect(screen.get_width()/2, screen.get_height()/2,75,50)
    defaultNodeShape = pygame.Rect(0, 0, 15, 15)

    ANDButton = pygame.Rect(screen.get_width()-100, screen.get_height()-125,100,100)
    ORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-225,100,100)
    NOTButton = pygame.Rect(screen.get_width()-100, screen.get_height()-325,100,100)
    NORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-425,100,100)
    NANDButton = pygame.Rect(screen.get_width()-100, screen.get_height()-525,100,100)
    XORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-625,100,100)
    XNORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-725,100,100)
    standardOutputRect = pygame.Rect(screen.get_width()/2, 25, 50, 50)

    createdRectangles = []
    createdNodes = []
    createdWires = []
    output_order = []


    manipulation_gate = False
    draggedWire = None
    standardProcessingInfo = [False, False, None]

    def createGate(a):
        global currentIndex
        print("clicked on button")
        newShape = logicGate(a, defaultGateShape, False, standardProcessingInfo, currentIndex + 1)
        currentIndex += 1
        newInput1 = connectorNode(defaultNodeShape, newShape, "input1", False)
        newInput2 = connectorNode(defaultNodeShape, newShape, "input2", False)
        newOutput = connectorNode(defaultNodeShape, newShape, "output", False)
        createdRectangles.append(newShape)
        createdNodes.append(newInput1)
        createdNodes.append(newInput2)
        createdNodes.append(newOutput)

    def Topological_Sort():
        global currentIndex
        global output_order
        next_point = [None for i in range(65535)]
        from_point_number= [None for i in range(65535)]
        for shape in createdWires:
            in_point = out_point = 0
            if type(shape.startPoint) == logicGate and shape.startPoint.inputOutput[0] == 'o':
                in_point = shape.endPoint.parent.idx
                out_point = shape.startPoint.parent.idx
            elif type(shape.endPoint) == logicGate and shape.endPoint.inputOutput[0] == 'i':
                in_point = shape.startPoint.parent.idx
                out_point = shape.endPoint.parent.idx

            if next_point[in_point] == None:
                next_point[in_point]=[out_point]
            else: next_point[in_point].append(out_point)

            if from_point_number[out_point] == None:
                from_point_number[out_point] =1
            else:
                from_point_number[out_point] += 1

        temper = []
        for shape in createdRectangles:
            if from_point_number[shape.idx] == 0:
                temper.append(shape)

        while len(temper) != 0:
            shape =temper.pop()
            output_order.append(shape)
            for point in next_point[shape.idx]:
                from_point_number[point] -= 1
                if from_point_number[point] == 0:
                    for tem_shape in createdRectangles:
                        if tem_shape.idx == point:
                            temper.append(point)
        print(output_order)
    #initializeGame

    outputRect = output(standardOutputRect, [False], "red")
    newInput = connectorNode(defaultNodeShape, outputRect, "input1", False)
    createdNodes.append(newInput)




    pygame.init() # creates game window
    clock = pygame.time.Clock() # creates needed clock object

    # bg = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # creates fullscreen version
    # bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE) # creates resizable version

    while True: # game runs until user decides to end it
        clock.tick(30)  # set FPS

        font = pygame.font.Font(None, 36)

#---events---
        for event in pygame.event.get(): # check for input
            if event.type == pygame.QUIT: # closes program if X in top right clicked
                exit() # this function call closes the program
#---m1 event---

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickedOnNothing = True
                if event.button == 1:
                    #TODO drop logic on m1 click on anything. This can probably be done by changing pickedUp/inUse whenever a m1 event takes place.
                    for shape in createdNodes:
                        if shape.shape.collidepoint(event.pos):
                            print("node clicked")
                            clickedOnNothing = False
                            if shape.inUse == False and draggedWire == None: #create wire
                                newWire = wires(shape, [0,0], True, shape.inputOutput)
                                createdWires.append(newWire)
                                draggedWire = newWire
                                if shape.inputOutput != "output":
                                    shape.inUse = True
                                print("wire created")
                            elif shape.inUse == False and draggedWire != None:
                                if shape.inputOutput[0] != draggedWire.startConnectionType[0]:
                                    print("aeiou")
                                    draggedWire.endPoint = shape
                                    draggedWire.pickedUp = False
                                    if shape.inputOutput != "output":
                                        shape.inUse = True
                                    #draggedWire.startPoint.parent. + draggedWire.startConnectionType #find startConnectionType
                                    draggedWire.endPoint.parent #find current connection type
                                    draggedWire = None









                    for shape in createdRectangles: #check if rectangles are clicked on
                        if shape.shape.collidepoint(event.pos):
                            clickedOnNothing = False
                            print("clicked on gate")
                            if manipulation_gate == True:
                                manipulation_gate = False
                                shape.pickedUp = False
                            elif manipulation_gate == False:
                                manipulation_gate = True
                                shape.pickedUp = True

                    if ANDButton.collidepoint(event.pos): #check if spawning rectangle is clicked on
                        clickedOnNothing = False
                        createGate("AND")
                    elif ORButton.collidepoint(event.pos):
                        clickedOnNothing = False
                        createGate("OR")
                    elif NORButton.collidepoint(event.pos):
                        clickedOnNothing = False
                        createGate("NOR")
                    elif NANDButton.collidepoint(event.pos):
                        clickedOnNothing = False
                        createGate("NAND")
                    elif XORButton.collidepoint(event.pos):
                        clickedOnNothing = False
                        createGate("XOR")
                    elif XNORButton.collidepoint(event.pos):
                        clickedOnNothing = False
                        createGate("XNOR")
                    elif NOTButton.collidepoint(event.pos):
                        clickedOnNothing = False
                        createGate("NOT")
                    else: #check if nothing was clicked on
                        if manipulation_gate == False and clickedOnNothing == True:
                            print("clicked on nothing")
                            if len(createdWires) >= 1 and draggedWire != None:
                                createdWires[-1].startPoint.inUse = False
                                createdWires.pop(-1)

                                draggedWire = None
                            for shape in createdRectangles:
                                shape.pickedUp = False

                elif event.button == 3: #deletes shapes
                    print("m2 clicked")

                    for v in createdNodes:
                            print (v.parent)

                    for  shape in createdRectangles: #check if rectangles are clicked on
                        if shape.shape.collidepoint(event.pos):


                            print("deleting something")
                            len_Node = len(createdNodes)
                            for i in range(len_Node):

                                Node =createdNodes.pop(0)
                                for i in range(len(createdWires)):
                                    wire = createdWires.pop(0)
                                    if wire.startPoint != Node and wire.endPoint != Node:
                                        createdWires.append(wire)
                                    else:
                                        if wire.endPoint.inputOutput[0] == "i":
                                            wire.endPoint.parent.processingInfo[int(wire.endPoint.inputOutput[-1])-1] = False
                                        elif wire.startPoint.inputOutput[0] == "i":
                                            wire.startPoint.parent.processingInfo[int(wire.startPoint.inputOutput[-1])-1] = False
                                        wire.endPoint.inUse = False
                                        wire.startPoint.inUse = False
                                if Node.parent != shape:
                                    createdNodes.append(Node)

                            #nodes need to be deleted
                            createdRectangles.remove(shape)








#---create or recreate all shapes---

        bg.fill((0, 0, 0))  # reset bg to black (0,0,0) screen rgb is out of 255, not 1 like rblx
        #draw buttons to spawn in gates


        pygame.draw.rect(bg, "purple", ANDButton)
        pygame.draw.rect(bg, "blue", ORButton)
        pygame.draw.rect(bg, "green", NOTButton)
        pygame.draw.rect(bg, "yellow", NORButton)
        pygame.draw.rect(bg, "orange", NANDButton)
        pygame.draw.rect(bg, "cyan", XORButton)
        pygame.draw.rect(bg, "pink", XNORButton)

        #draw input and output box




        for shape in createdNodes:
            shape.redrawSelf()

        for shape in createdRectangles:
            pygame.draw.rect(bg, "white", shape.shape)
            #TODO make circles a seperate class where you can click on them and drag a line to other circles

        output_order = []
        Topological_Sort()
        for shape in output_order:
            print("shapes")
            for node in createdNodes:
                print("nodes")
                if node.inputOutput[0] == 'i' and node.parent == shape:
                    print("if statement")
                    for wire in createdWires:
                        if wire.startPoint ==  node and wire.startPoint.inputOutput == 'o':
                            wire.updateGates()
                        elif wire.endPoint == node and wire.endpoint.inputOutput =='o':
                            wire.updateGates()

        for shape in createdWires:
            shape.drawLine()


        for shape in createdRectangles:
            bg.blit(font.render(shape.type, 1, "black"), (shape.shape[0], shape.shape[1]))
            # if dragging == True:
            shape.doLogic()
            #print("gate", shape.type, "outputting",  shape.processingInfo)
            #print(shape.processingInfo[2])
            if manipulation_gate == True:
                if shape.pickedUp == True:
                    shape.shape = pygame.Rect (pygame.mouse.get_pos () [0], pygame.mouse.get_pos () [1], defaultGateShape[2],defaultGateShape[3])

        outputRect.changeColor()
        pygame.draw.rect(bg, outputRect.color, outputRect.shape)




        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()

