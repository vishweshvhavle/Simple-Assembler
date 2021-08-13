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
FLAG = 0000000000000000

#-----------------------------------------------------------------------------------

no_vars = 0 #number of variables

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

        elif line[0] == 'sub':
            machine_code.append(operations.sub(line[1],line[2],line[3],line_number))

        elif line[0] == 'mov':
            if line[2][0] == '$':
                machine_code.append(operations.moveImmediate(line[1],line[2][1:],line_number))
            else:
                machine_code.append(operations.moveRegister(line[1],line[2],line_number))

        elif line[0] == 'ld':
            machine_code.append(operations.load(line[1],line[2],line_number))

        elif line[0] == 'st':
            machine_code.append(operations.store(line[1],line[2],line_number))

        elif line[0] == 'mul':
            machine_code.append(operations.mul(line[1],line[2],line[3],line_number))

        elif line[0] == 'div':
            machine_code.append(operations.div(line[1],line[2],line[3],line_number))

        elif line[0] == 'rs':
            machine_code.append(operations.rightShift(line[1],line[2],line[3],line_number))

        elif line[0] == 'ls':
            machine_code.append(operations.leftShift(line[1],line[2],line[3],line_number))

        elif line[0] == 'xor':
            machine_code.append(operations.xor(line[1],line[2],line[3],line_number))

        elif line[0] == 'or':
            machine_code.append(operations.Or(line[1],line[2],line[3],line_number))

        elif line[0] == 'not':
            machine_code.append(operations.invert(line[1],line[2],line_number))

        elif line[0] == 'cmp':
            machine_code.append(operations.compare(line[1],line[2],line_number))

        elif line[0] == 'jmp':
            machine_code.append(operations.jmp(line[1],line_number))

        elif line[0] == 'jlt':
            machine_code.append(operations.jlt(line[1],line_number))

        elif line[0] == 'jgt':
            machine_code.append(operations.jgt(line[1],line_number))

        elif line[0] == 'je':
            machine_code.append(operations.je(line[1],line_number))

        elif line[0] == 'hlt':
            if line_number < len(assembly_code)-1:
                errors.error_i()
                break
            machine_code.append(operations.hlt())
    else:
        continue

    line_number = line_number + 1

for line in machine_code:
    print(line)