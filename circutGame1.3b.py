#this code is held together by sticks duct tape and prayers
import pygame
from collections import deque


screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen
bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen. bg stands for background in this case


#logic gate functions
def andGate(input1, input2):
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



#objects declared

#linked gates arrayed as such
"""
1. which gate is linked through input 1
2. which gate is linked through input 2
3. which gates am I outputting to

"""
class logicGate:
    def __init__ (self, type, shape, pickedUp, processingInfo, indegree, linkedGates, movedAtSomePoint):
        self.shape = shape
        self.type = type
        self.pickedUp = pickedUp
        self.processingInfo = processingInfo
        self.indegree = indegree
        self.linkedGates = linkedGates
        self.movedAtSomePoint = movedAtSomePoint

        #detects if gate only has one input and deletes one of the two input if so
        #NOTE (TODO?) to self, I still need to kill linked gates on wire disconnect
    def doLogic(self):
        if self.linkedGates[0] != None:
            self.processingInfo[0] = self.linkedGates[0].processingInfo[2]
        else:
            self.processingInfo[0] = False
        if self.linkedGates[1] != None:
            self.processingInfo[1] = self.linkedGates[1].processingInfo[2]
        else:
            self.processingInfo [1] = False
        self.computeGate()

    def computeGate(self):
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
        if isinstance(self.endPoint, connectorNode) and isinstance(self.startPoint, connectorNode):
            if self.startPoint.inputOutput[0] == "o":
                #print(self.startPoint.parent.processingInfo)
                self.endPoint.parent.processingInfo[int(self.endPoint.inputOutput[-1])-1] = self.startPoint.parent.processingInfo[2]
            else:
                self.startPoint.parent.processingInfo[int(self.startPoint.inputOutput[-1]) -1] = self.endPoint.parent.processingInfo[2]
        else:
            return

class output:
    def __init__(self, shape, processingInfo, color, indegree, linkedGates):
        self.shape = shape
        self.processingInfo = processingInfo
        self.color = color
        self.indegree = indegree
        self.linkedGates = linkedGates

    def changeColor(self):
        #print(self.processingInfo)
        if self.processingInfo[0] == True:
            self.color = "green"
        elif self.processingInfo[0] == False:
            self.color = "red"
class input:
    def __init__(self, shape, processingInfo, color, indegree, linkedGates):
        self.shape = shape
        self.processingInfo = processingInfo
        self.color = color
        self.indegree = indegree
        self.linkedGates = linkedGates

    def changeColor(self):
        #print(self.processingInfo)
        if self.processingInfo[2] == True:
            self.color = "green"
        elif self.processingInfo[2] == False:
            self.color = "red"

def main():

    #variables declared
    defaultGateShape = pygame.Rect(screen.get_width()/2, screen.get_height()/2,75,50)
    defaultNodeShape = pygame.Rect(0, 0, 15, 15)

    #create spawn buttons, probably could be shortened to some form of a for loop
    ANDButton = pygame.Rect(screen.get_width()-100, screen.get_height()-125,100,100)
    ORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-225,100,100)
    NOTButton = pygame.Rect(screen.get_width()-100, screen.get_height()-325,100,100)
    NORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-425,100,100)
    NANDButton = pygame.Rect(screen.get_width()-100, screen.get_height()-525,100,100)
    XORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-625,100,100)
    XNORButton = pygame.Rect(screen.get_width()-100, screen.get_height()-725,100,100)
    standardOutputRect = pygame.Rect(screen.get_width()/2, 0, 50, 50)
    standardInputRect = pygame.Rect(screen.get_width()/2, screen.get_height()-100, 50, 50)

    createdRectangles = []
    createdNodes = []
    createdWires = []

    manipulation_gate = False
    draggedWire = None
    standardProcessingInfo = [False, False, None]

    ableToSpawnRects = True

    #createGate func declared here due to weird python variable stuff (global and local var problems)
    def createGate(a):
        print("clicked on button")
        newShape = logicGate(a,defaultGateShape, False, standardProcessingInfo, 0, [None, None, None], False)
        newInput1 = connectorNode(defaultNodeShape, newShape, "input1", False)
        newInput2 = connectorNode(defaultNodeShape, newShape, "input2", False)
        newOutput = connectorNode(defaultNodeShape, newShape, "output", False)
        createdRectangles.append(newShape)
        createdNodes.append(newInput1)
        createdNodes.append(newInput2)
        createdNodes.append(newOutput)



    #input and output rectangles created (although not drawn)
    outputRect = output(standardOutputRect, [False], "red", 0, [None, None, None])
    inputRect = input(standardInputRect, [False, False, False], "red", 0, [None, None, None])
    newInput = connectorNode(defaultNodeShape, outputRect, "input1", False)
    newOutput = connectorNode(defaultNodeShape, inputRect, "output", False)
    createdNodes.append(newInput)
    createdNodes.append(newOutput)



    #thanks to prof while for the main gameplay loop
    pygame.init() # creates game window
    clock = pygame.time.Clock() # creates needed clock object

    # bg = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # creates fullscreen version
    # bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE) # creates resizable version

    while True: # game runs until user decides to end it
        clock.tick(30)  # set FPS

        font = pygame.font.Font(None, 36)
        font_inputOutput = pygame.font.Font(None, 18)

#---events---
        for event in pygame.event.get(): # check for input
            if event.type == pygame.QUIT: # closes program if X in top right clicked
                exit() # this function call closes the program
#---m1 event---
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickedOnNothing = True
                if event.button == 1:
#check if clicked on a node
                    for shape in createdNodes:
                        if shape.shape.collidepoint(event.pos):
                            clickedOnNothing = False
                            if shape.inUse == False and draggedWire == None: #create wire
                                newWire = wires(shape, [0,0], True, shape.inputOutput)
                                createdWires.append(newWire)
                                draggedWire = newWire
                                if shape.inputOutput != "output":
                                    shape.inUse = True
                            elif shape.inUse == False and draggedWire != None:
                                if shape.inputOutput[0] != draggedWire.startConnectionType[0]:
                                    print("aeiou")
                                    draggedWire.endPoint = shape
                                    draggedWire.pickedUp = False
                                    if shape.inputOutput != "output":
                                        shape.inUse = True
                                    #draggedWire.startPoint.parent. + draggedWire.startConnectionType #find startConnectionType
                                    draggedWire.endPoint.parent
                                    draggedWire = None

#check if clicked on a logicGate
                    for shape in createdRectangles: #check if rectangles are clicked on

                        if shape.shape.collidepoint(event.pos):
                            clickedOnNothing = False
                            shape.movedAtSomePoint = True
                            print("clicked on gate")
                            if manipulation_gate == True and shape.pickedUp == True:
                                manipulation_gate = False
                                shape.pickedUp = False
                            elif manipulation_gate == False:
                                manipulation_gate = True
                                shape.pickedUp = True
                        print(manipulation_gate)
                        if shape.movedAtSomePoint == False:
                            ableToSpawnRects = False
#check if clicked on the input button
                    if standardInputRect.collidepoint(event.pos):
                        inputRect.processingInfo[2] = not inputRect.processingInfo[2]
#check if the logic gate spawning buttons are clicked on
                    if ableToSpawnRects != False:
                        if ANDButton.collidepoint(event.pos):
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
                    ableToSpawnRects = True
#if all else fails, say that nothing was clicked on
                    if manipulation_gate == False and clickedOnNothing == True:
                        print("clicked on nothing")
                        if len(createdWires) >= 1 and draggedWire != None:
                            createdWires[-1].startPoint.inUse = False
                            createdWires.pop(-1)
                            draggedWire = None
                            for shape in createdRectangles:
                                shape.pickedUp = False
#---m2 event---
#check if m2 was clicked and we need to delete a shape
                elif event.button == 3: #deletes shapes
                    print("m2 clicked")
#check if any logic gates were clicked on
                    for  shape in createdRectangles: #this monster of a loop will iterate through every single created wire and node to see if it has any association with the deleted shape to delete it.
                        if shape.shape.collidepoint(event.pos):
                            print("deleting something")
                            len_Node = len(createdNodes)
                            for i in range(len_Node):
                                Node =createdNodes.pop(0)
                                for v in enumerate(createdWires):
                                    wire = createdWires.pop(0)
                                    if wire.startPoint.parent != shape and wire.endPoint.parent != shape:
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
                            createdRectangles.remove(shape)
#---Reset most shape parameters to prep them for logic---
        for shape in createdRectangles:
            shape.indegree = 0
            shape.processingInfo = [False, False, None]
        for wire in createdWires:
            wire.startPoint.parent.linkedGates = [None, None, None]
            if type(wire.endPoint) != list:
                wire.endPoint.parent.linkedGates = [None, None, None]

#---Wires process connections and calculate indegrees---
        for wire in createdWires:
            if type(wire.endPoint) == connectorNode:
                #breakpoint()
                if type(wire.endPoint.parent) == output:
                    outputRect.processingInfo[0] = wire.startPoint.parent.processingInfo[2]
                    wire.startPoint.parent.linkedGates[2] = outputRect
                elif wire.endPoint.inputOutput[0] == "o":
                    wire.startPoint.parent.linkedGates[int(wire.startPoint.inputOutput[-1])-1] = wire.endPoint.parent
                    if wire.endPoint.parent.linkedGates[2] != None:
                        wire.endPoint.parent.linkedGates.append(wire.startPoint.parent)
                    else:
                        wire.endPoint.parent.linkedGates[2] = wire.startPoint.parent
                    wire.startPoint.parent.indegree +=1
                elif wire.endPoint.inputOutput[0] == "i":
                    if wire.startPoint.parent.linkedGates[2] != None:
                        wire.startPoint.parent.linkedGates.append(wire.endPoint.parent)
                    else:
                        wire.startPoint.parent.linkedGates[2] = wire.endPoint.parent
                    wire.endPoint.parent.linkedGates[int(wire.endPoint.inputOutput[-1])-1] = wire.startPoint.parent
                    wire.endPoint.parent.indegree += 1




#---process logic---
        #findLowestIndegree and store all in q
        #huge thanks to https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/ for helping with topo sorts

        q = deque() #q acts as an "advanced list"
        topoSort = []
        markedShapes = []
        unsortedShapes = createdRectangles[:]
        unsortedShapes.append(inputRect)
        count = 0
#finds shaped with a indegree of 0 and puts into q. Also marks any adjacent shapes to decrease their indegree by 1
#if your still confused, we're using something called Kahn's algory
        while len(topoSort) != len(createdRectangles)+1: #still error prone, be careful around here
            count += 1
            #print(count)
            print(len(topoSort))
            if count > 256:
                #breakpoint()
                break

            for shape in unsortedShapes:
                if shape.indegree == 0:

                    for i,v in enumerate(shape.linkedGates):

                        if i > 1:
                            markedShapes.append(v)
                            #print("appended")
                            #print(markedShapes)
                    q.append(shape)
                #else:
                    #breakpoint()


            while q:
                e = q.popleft()
                unsortedShapes.remove(e)
                topoSort.append(e)
                #print("topoSort:",topoSort)
            for v in markedShapes:
                if v != None and v.indegree > 0:
                    v.indegree -= 1
                elif v != None and v.indegree < 0:
                    v.indegree = 0
            #print("free")

            #print(topoSort)
            #print(unsortedShapes)


        for node in topoSort:
            if type(node) == logicGate:
                node.doLogic()
                #print(node.processingInfo)









#---create or recreate all shapes---

        bg.fill((0, 0, 0))  # reset bg to black (0,0,0) screen rgb is out of 255, not 1 like rblx
        #draw buttons to spawn in gates


        pygame.draw.rect(bg, "purple", ANDButton)
        bg.blit(font.render("AND", 1, "black"), (ANDButton[0], ANDButton[1]))
        pygame.draw.rect(bg, "blue", ORButton)
        bg.blit(font.render("OR", 1, "black"), (ORButton[0], ORButton[1]))
        pygame.draw.rect(bg, "green", NOTButton)
        bg.blit(font.render("NOT", 1, "black"), (NOTButton[0], NOTButton[1]))
        pygame.draw.rect(bg, "yellow", NORButton)
        bg.blit(font.render("NOR", 1, "black"), (NORButton[0], NORButton[1]))
        pygame.draw.rect(bg, "orange", NANDButton)
        bg.blit(font.render("NAND", 1, "black"), (NANDButton[0], NANDButton[1]))
        pygame.draw.rect(bg, "cyan", XORButton)
        bg.blit(font.render("XOR", 1, "black"), (XORButton[0], XORButton[1]))
        pygame.draw.rect(bg, "pink", XNORButton)
        bg.blit(font.render("XNOR", 1, "black"), (XNORButton[0], XNORButton[1]))
        #draw input and output box




        for shape in createdNodes:
            shape.redrawSelf()

        for shape in createdRectangles:
            pygame.draw.rect(bg, "white", shape.shape)
            #TODO make circles a seperate class where you can click on them and drag a line to other circles

        for shape in createdWires:
            shape.drawLine()
            shape.updateGates()

        for shape in createdRectangles:
            bg.blit(font.render(shape.type, 1, "black"), (shape.shape[0], shape.shape[1]))
            # if dragging == True:
            #shape.doLogic()
            #print(shape.processingInfo[2])
            if manipulation_gate == True:
                if shape.pickedUp == True:
                    shape.shape = pygame.Rect (pygame.mouse.get_pos () [0], pygame.mouse.get_pos () [1], defaultGateShape[2],defaultGateShape[3])

        outputRect.changeColor()
        pygame.draw.rect(bg, outputRect.color, outputRect.shape)
        bg.blit(font_inputOutput.render("OUTPUT", 1, "black"), outputRect.shape.midleft)
        inputRect.changeColor()
        pygame.draw.rect(bg, inputRect.color, inputRect.shape)
        bg.blit(font_inputOutput.render("  INPUT", 1, "black"), inputRect.shape.midleft)




        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()

