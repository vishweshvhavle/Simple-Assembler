#Done By
#Vishwesh Vhavle, 2020156
#Dev Thakkar, 2020052
#Sahil Deshpande, 2020114

#ISA OPERATIONS

#Performs reg1 = reg2 + reg3. If the computation
#overflows, then the overflow flag is set

def add():
    return


#Performs reg1 = reg2 - reg3. In case reg3 > reg2,
#0 is written to reg1 and overflow flag is set.

def sub():
    return


#Performs reg1 = $Imm where Imm is a 8 bit value.

def moveImmediate():
    return


#Performs reg1 = reg2.

def moveRegister():
    return


#Loads data from mem_addr into reg1.

def load():
    return


#Stores data from reg1 to mem_addr.

def store():
    return


#Performs reg1 = reg2 x reg3. If the computation
#overflows, then the overflow flag is set.

def mul():
    return


#Performs reg3/reg4. Stores the quotient
#in R0 and the remainder in R1.

def div():
    return


#Right shifts reg1 by $Imm,
#where $Imm is an 8 bit value.

def rightShift():
    return


#Left shifts reg1 by $Imm,
#where $Imm is an 8 bit value.

def leftShift():
    return


#Performs bitwise XOR of reg2 and reg3.
#Stores the result in reg1.

def xor():
    return


#Performs bitwise OR of reg2 and reg3.
#Stores the result in reg1.

def Or():
    return


#Performs bitwise AND of reg2 and reg3.
#Stores the result in reg1.

def And():
    return


#Performs bitwise NOT of reg2.
#Stores the result in reg1.

def invert():
    return


#Compares reg1 and reg2 and sets up the FLAGS register.

def compare():
    return


#Jumps to mem_addr, where mem_addr is a memory address.

def jmp():
    return


#Jump to mem_addr if the less than flagis set (less than
#flag = 1), where mem_addr is a memory address.

def jlt():
    return


#Jump to mem_addr if the greater than flag is set (greater than
#flag = 1), where mem_addr is a memory address.

def jgt():
    return


#Jump to mem_addr if the equal flag is set (equal flag =
#1), where mem_addr is a memory address.

def je():
    return

#Stops the machine from executing until reset

def halt():
    return