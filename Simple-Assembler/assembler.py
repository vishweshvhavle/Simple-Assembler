#Done By
#Vishwesh Vhavle, 2020156
#Dev Thakkar, 2020052
#Sahil Deshpande, 2020114

import operations
import errors
from sys import stdin

#OPCODES
# add 00000 | sub 00001 | mov $Imm 00010 | mov 00011 | ld 00100 | st 00101
# mul 00110 | div 00111 | rs 01000 | ls 01001 | xor 01010 | or 01011 | and 01100
# not 01101 | cmp 01110 | jmp 01111 | jlt 10000 | jgt 10001 | je 10010 | hlt 10011

#FLAGS
V = False #Overflow
L = False #Less than in comparator
G = False #Greater than in comparator
E = False #Equal to in comparator

#-----------------------------------------------------------------------------------

#Storing stdin inputs of assembly code in array
assembly_code = []
machine_code = []
for line in stdin:
    if line == '':
        break
    else:
        assembly_code.append(line.split())

line_number = 0
for line in assembly_code:
    if line != []:
        if line[0] == 'add':
            machine_code.append(operations.add(line[1],line[2],line[3],line_number))

        if line[0] == 'sub':
            machine_code.append(operations.sub(line[1],line[2],line[3],line_number))

        if line[0] == 'add':
            machine_code.append(operations.add(line[1],line[2],line[3],line_number))

        if line[0] == 'add':
            machine_code.append(operations.add(line[1],line[2],line[3],line_number))





