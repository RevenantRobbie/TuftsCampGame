#AND gate
 #       NOT gate
  #      XOR gate
   #     XNOR gate
    #    NAND gate
     #   OR gate
      #  NOR gate



def andGate(input1, input2):
    if input1 and input2 == True:
        return True
    else:
        return False




def orGate(input1, input2):
    if input1 or input2:
        return True
    elif input1 and input2 == True:
            return True
    else:
        return False

def notGate(input1):
    if input1:
        return False
    else:
        return True

def norGate(input1, input2):
    if input1 == False and input2 == False


