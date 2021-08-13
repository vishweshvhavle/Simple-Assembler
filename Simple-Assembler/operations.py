#ISA OPERATIONS

import assembler.py

#OPCODES for reference
# add 00000 | sub 00001 | mov $Imm 00010 | mov 00011 | ld 00100 | st 00101 
# mul 00110 | div 00111 | rs 01000 | ls 01001 | xor 01010 | or 01011 | and 01100
# not 01101 | cmp 01110 | jmp 01111 | jlt 10000 | jgt 10001 | je 10010 | hlt 10011

#Performs reg1 = reg2 + reg3. If the computation
#overflows, then the overflow flag is set

#Empty string for output
output = ""


def add():
    if operation == 'ADD':
        output = output + '00000'
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

def hlt():
  output = output + '10011'