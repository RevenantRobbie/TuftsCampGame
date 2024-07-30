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


screen = pygame.display.set_mode((1280,720))

SCREEN_W = screen.get_width()  # height of screen
SCREEN_H = screen.get_height()  # width of screen
bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen. bg stands for background in this case
#objects declared
class logicGate:
    def __init__ (self, type, shape, pickedUp, input1, input2, output):
        self.shape = shape
        self.type = type
        self.pickedUp = pickedUp
        self.input1 = input1
        self.input2 = input2
        self.output = output

        #detects if gate only has one input and deletes one of the two input if so


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
            self.shape = pygame.Rect(self.parent.shape[0]+75, self.parent.shape[1]+100, 15, 15)
        elif self.inputOutput == "input2":
            self.shape = pygame.Rect(self.parent.shape[0]+175, self.parent.shape[1]+100, 15, 15) #input2
        elif self.inputOutput == "output":
            self.shape = pygame.Rect(self.parent.shape[0]+125, self.parent.shape[1]-15, 15, 15)
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




def main():
    #variables declared
    defaultGateShape = pygame.Rect(screen.get_width()/2, screen.get_height()/2,250,100)
    defaultNodeShape = pygame.Rect(0, 0, 15, 15)
    testingRect = pygame.Rect(screen.get_width()/4, screen.get_height()/4,100,100)
    createdRectangles = []
    createdNodes = []
    createdWires = []
    #inUse = False #checks if the mouse is doing something so it can't do 2 things at once
    manipulation_gate = False
    draggedWire = None

    # dragging = False
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
                if event.button == 1:
                    #TODO drop logic on m1 click on anything. This can probably be done by changing pickedUp/inUse whenever a m1 event takes place.
                    for shape in createdNodes:
                        if shape.shape.collidepoint(event.pos):
                            if shape.inUse == False and draggedWire == None: #create wire
                                newWire = wires(shape, [0,0], True, shape.inputOutput)
                                createdWires.append(newWire)
                                draggedWire = newWire
                                shape.inUse = True
                            elif shape.inUse == False and draggedWire != None:
                                if shape.inputOutput[0] != draggedWire.startConnectionType[0]:
                                    print("aeiou")
                                    draggedWire.endPoint = shape
                                    draggedWire.pickedUp = False
                                    shape.inUse = True
                                    draggedWire.startPoint.parent. + draggedWire.startConnectionType #find startConnectionType
                                    draggedWire.endPoint.parent #find current connection type
                                    draggedWire = None









                    for shape in createdRectangles: #check if rectangles are clicked on
                        if shape.shape.collidepoint(event.pos):
                            print("clicked on gate")
                            if manipulation_gate == True:
                                manipulation_gate = False
                                shape.pickedUp = False
                            elif manipulation_gate == False:
                                manipulation_gate = True
                                shape.pickedUp = True

                    if testingRect.collidepoint(event.pos): #check if spawning rectangle is clicked on
                        print("clicked on button")
                        newShape = logicGate("AND ",defaultGateShape, False, False, False,False)
                        newInput1 = connectorNode(defaultNodeShape, newShape, "input1", False)
                        newInput2 = connectorNode(defaultNodeShape, newShape, "input2", False)
                        newOutput = connectorNode(defaultNodeShape, newShape, "output", False)


                        createdRectangles.append(newShape)
                        createdNodes.append(newInput1)
                        createdNodes.append(newInput2)
                        createdNodes.append(newOutput)
                        for v in createdNodes:
                            print (v.parent)
                    else: #check if nothing was clicked on
                        if manipulation_gate == False:
                            print("clicked on nothing")
                            for shape in createdRectangles:
                                shape.pickedUp = False

                elif event.button == 3:
                    print("m2 clicked")

                    for v in createdNodes:
                            print (v.parent)

                    for  shape in createdRectangles: #check if rectangles are clicked on
                        if shape.shape.collidepoint(event.pos):
                            print("deleting something")
                            len_Node = len(createdNodes)
                            for i in range(len_Node):

                                #print(node.parent)
                                Node =createdNodes.pop(0)
                                if Node.parent != shape:
                                    createdNodes.append(Node)

                            #nodes need to be deleted
                            createdRectangles.remove(shape)








#---create or recreate all shapes---
        bg.fill((0, 0, 0))  # reset bg to black (0,0,0) screen rgb is out of 255, not 1 like rblx

        pygame.draw.rect(bg, "purple", testingRect)

        for shape in createdNodes:
            shape.redrawSelf()

        for shape in createdRectangles:
            pygame.draw.rect(bg, "white", shape.shape)
            #TODO make circles a seperate class where you can click on them and drag a line to other circles

        for shape in createdRectangles:
            # if dragging == True:
            if manipulation_gate == True:
                if shape.pickedUp == True:
                    shape.shape = pygame.Rect (pygame.mouse.get_pos () [0], pygame.mouse.get_pos () [1], 250,100)

        for shape in createdWires:
            shape.drawLine()


        pygame.display.update()  # update screen
        #sometimes ppl do pygame.display.flip()
        #update is better in most situations

#for most games, this should get you through

if __name__ == '__main__':
    main()

