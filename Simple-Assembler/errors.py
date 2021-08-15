#ERRORS

registers = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'FLAGS']

def error_type_Var(line):
    if len(line) != 2:
        return (True, "Wrong syntax used for instructions")

    elif not line[1].replace('_', '').isalnum():
        return (True, "Illegal variable name")

    return (False, None)

def error_type_A(line):
    if len(line) != 4:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAGS':
        return (True, "Illegal use of FLAGSS register")

    elif line[1] not in registers or line[2] not in registers or line[3] not in registers:
        return (True, "Typos in instruction name or register name")

    return (False, None)

def error_type_B(line):
    if len(line) != 3:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAGS':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in registers:
        return (True, "Typos in instruction name or register name")

    elif not line[2].startswith("$"):
        return (True, "Wrong syntax used for instructions")

    return (False, None)

def error_type_C(line):
    if len(line) != 3:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAGS':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in registers or line[2] not in registers:
        return (True, "Typos in instruction name or register name")

    return (False, None)

def error_type_D(line, variables):
    if len(line) != 3:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAGS':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in registers or line[2] not in registers:
        if line[2] not in variables:
            return (True, "Undeclared Variable Used")
        elif line[2] in variables:
            return (False, None)
        return (True, "Typos in instruction name or register name")

    return (False, None)

def error_type_E(line):
    if len(line) != 2:
        return (True, "Wrong syntax used for instructions")

    return (False, None)

def error_type_F(line):
    if len(line) != 1:
        return (True, "Wrong syntax used for instructions")

    return (False, None)