#Done By
#Vishwesh Vhavle, 2020156
#Dev Thakkar, 2020052
#Sahil Deshpande, 2020114

import operations.py
import errors.py

#OPCODES for reference
# add 00000 | sub 00001 | mov $Imm 00010 | mov 00011 | ld 00100 | st 00101 
# mul 00110 | div 00111 | rs 01000 | ls 01001 | xor 01010 | or 01011 | and 01100
# not 01101 | cmp 01110 | jmp 01111 | jlt 10000 | jgt 10001 | je 10010 | hlt 10011 

#FLAGS
bool V = false

#Empty string for output
output = ""


#We take input in various lines and store individual lines in a array
while True:
    operation = input()

    if operation == 'hlt':
      break




