#this code is held together by sticks duct tape and prayers
'''''''''
5 Now when Jesus saw the crowds, he went up on a mountainside and sat down. His disciples came to him, 2 and he began to teach them.

The Beatitudes
He said:

3 “Blessed are the poor in spirit,
    for theirs is the kingdom of heaven.
4 Blessed are those who mourn,
    for they will be comforted.
5 Blessed are the meek,
    for they will inherit the earth.
6 Blessed are those who hunger and thirst for righteousness,
    for they will be filled.
7 Blessed are the merciful,
    for they will be shown mercy.
8 Blessed are the pure in heart,
    for they will see God.
9 Blessed are the peacemakers,
    for they will be called children of God.
10 Blessed are those who are persecuted because of righteousness,
    for theirs is the kingdom of heaven.

11 “Blessed are you when people insult you, persecute you and falsely say all kinds of evil against you because of me. 12 Rejoice and be glad, because great is your reward in heaven, for in the same way they persecuted the prophets who were before you.

Salt and Light
13 “You are the salt of the earth. But if the salt loses its saltiness, how can it be made salty again? It is no longer good for anything, except to be thrown out and trampled underfoot.

14 “You are the light of the world. A town built on a hill cannot be hidden. 15 Neither do people light a lamp and put it under a bowl. Instead they put it on its stand, and it gives light to everyone in the house. 16 In the same way, let your light shine before others, that they may see your good deeds and glorify your Father in heaven.

The Fulfillment of the Law
17 “Do not think that I have come to abolish the Law or the Prophets; I have not come to abolish them but to fulfill them. 18 For truly I tell you, until heaven and earth disappear, not the smallest letter, not the least stroke of a pen, will by any means disappear from the Law until everything is accomplished. 19 Therefore anyone who sets aside one of the least of these commands and teaches others accordingly will be called least in the kingdom of heaven, but whoever practices and teaches these commands will be called great in the kingdom of heaven. 20 For I tell you that unless your righteousness surpasses that of the Pharisees and the teachers of the law, you will certainly not enter the kingdom of heaven.

Murder
21 “You have heard that it was said to the people long ago, ‘You shall not murder,[a] and anyone who murders will be subject to judgment.’ 22 But I tell you that anyone who is angry with a brother or sister[b][c] will be subject to judgment. Again, anyone who says to a brother or sister, ‘Raca,’[d] is answerable to the court. And anyone who says, ‘You fool!’ will be in danger of the fire of hell.

23 “Therefore, if you are offering your gift at the altar and there remember that your brother or sister has something against you, 24 leave your gift there in front of the altar. First go and be reconciled to them; then come and offer your gift.

25 “Settle matters quickly with your adversary who is taking you to court. Do it while you are still together on the way, or your adversary may hand you over to the judge, and the judge may hand you over to the officer, and you may be thrown into prison. 26 Truly I tell you, you will not get out until you have paid the last penny.

Adultery
27 “You have heard that it was said, ‘You shall not commit adultery.’[e] 28 But I tell you that anyone who looks at a woman lustfully has already committed adultery with her in his heart. 29 If your right eye causes you to stumble, gouge it out and throw it away. It is better for you to lose one part of your body than for your whole body to be thrown into hell. 30 And if your right hand causes you to stumble, cut it off and throw it away. It is better for you to lose one part of your body than for your whole body to go into hell.

#Divorce
#31 “It has been said, ‘Anyone who divorces his wife must give her a certificate of divorce.’[f] 32 But I tell you that anyone who divorces his wife, except for sexual immorality, makes her the victim of adultery, and anyone who marries a divorced woman commits adultery.

#Oaths
#33 “Again, you have heard that it was said to the people long ago, ‘Do not break your oath, but fulfill to the Lord the vows you have made.’ 34 But I tell you, do not swear an oath at all: either by heaven, for it is God’s throne; 35 or by the earth, for it is his footstool; or by Jerusalem, for it is the city of the Great King. 36 And do not swear by your head, for you cannot make even one hair white or black. 37 All you need to say is simply ‘Yes’ or ‘No’; anything beyond this comes from the evil one.[g]

#Eye for Eye
#38 “You have heard that it was said, ‘Eye for eye, and tooth for tooth.’[h] 39 But I tell you, do not resist an evil person. If anyone slaps you on the right cheek, turn to them the other cheek also. 40 And if anyone wants to sue you and take your shirt, hand over your coat as well. 41 If anyone forces you to go one mile, go with them two miles. 42 Give to the one who asks you, and do not turn away from the one who wants to borrow from you.

#Love for Enemies
#43 “You have heard that it was said, ‘Love your neighbor[i] and hate your enemy.’ 44 But I tell you, love your enemies and pray for those who persecute you, 45 that you may be children of your Father in heaven. He causes his sun to rise on the evil and the good, and sends rain on the righteous and the unrighteous. 46 If you love those who love you, what reward will you get? Are not even the tax collectors doing that? 47 And if you greet only your own people, what are you doing more than others? Do not even pagans do that? 48 Be perfect, therefore, as your heavenly Father is perfect.
'''

import pygame
from collections import deque


screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen
bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen. bg stands for background in this case



def andGate(input1, input2):
    print("AND:", input1, input2)
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
    def __init__ (self, type, shape, pickedUp, processingInfo, indegree, linkedGates):
        self.shape = shape
        self.type = type
        self.pickedUp = pickedUp
        self.processingInfo = processingInfo
        self.indegree = indegree
        self.linkedGates = linkedGates

        #detects if gate only has one input and deletes one of the two input if so
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

    def createGate(a):
        print("clicked on button")
        newShape = logicGate(a,defaultGateShape, False, standardProcessingInfo, 0, [None, None, None])
        newInput1 = connectorNode(defaultNodeShape, newShape, "input1", False)
        newInput2 = connectorNode(defaultNodeShape, newShape, "input2", False)
        newOutput = connectorNode(defaultNodeShape, newShape, "output", False)
        createdRectangles.append(newShape)
        createdNodes.append(newInput1)
        createdNodes.append(newInput2)
        createdNodes.append(newOutput)

    #initializeGame

    outputRect = output(standardOutputRect, [False], "red", 0, [None, None, None])
    inputRect = input(standardInputRect, [False, False, False], "red", 0, [None, None, None])
    newInput = connectorNode(defaultNodeShape, outputRect, "input1", False)
    newOutput = connectorNode(defaultNodeShape, inputRect, "output", False)
    createdNodes.append(newInput)
    createdNodes.append(newOutput)




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
                    if standardInputRect.collidepoint(event.pos):
                        inputRect.processingInfo[2] = not inputRect.processingInfo[2]

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
#---Wires process connections and calculate indegrees---
        for shape in createdRectangles:
            shape.indegree = 0
        for wire in createdWires:
            if type(wire.endPoint) == connectorNode:
                if type(wire.endPoint.parent) == output:
                    outputRect.processingInfo[0] = wire.startPoint.parent.processingInfo[2]
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
        for shape in createdRectangles:
            print(shape.indegree)

        q = deque() #q acts as an "advanced list"
        topoSort = []
        markedShapes = []
        iteration = 0

        while len(topoSort) < len(createdRectangles):
            for shape in createdRectangles:
                if shape.indegree == 0:
                    for i,v in enumerate(shape.linkedGates):
                        if i > 1:
                            markedShapes.append(v)
                    q.append(shape)
                if iteration == 0:
                    q.append(outputRect)
            while q:
                shape = q.popleft()
                topoSort.append(shape)
            for v in markedShapes:
                if v != None:
                    v.indegree -= 1
            iteration += 1

        print(topoSort)
        for node in topoSort:
            if type(node) == logicGate:
                node.doLogic()








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
        inputRect.changeColor()
        pygame.draw.rect(bg, inputRect.color, inputRect.shape)




        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()

