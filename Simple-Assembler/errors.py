#ERRORS

def error_type_Var(line):
    if len(line) != 2:
        return (True, "Wrong syntax used for instructions")

    elif not line[1].replace('_', '').isalnum():
        return (True, "Illegal variable name")

    return (False, None)

def error_type_A(line):
    if len(line) != 4:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAG' or line[2] == 'FLAG' or line[3] == 'FLAG':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6'] or line[2] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6'] or line[3] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']:
        return (True, "Typos in instruction name or register name")

    return (False, None)

def error_type_B(line):
    if len(line) != 3:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAG':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']:
        return (True, "Typos in instruction name or register name")

    elif not line[2].startswith("$"):
        return (True, "Wrong syntax used for instructions")

    return (False, None)

def error_type_C(line):
    if len(line) != 3:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAG' or line[2] == 'FLAG':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6'] or line[2] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']:
        return (True, "Typos in instruction name or register name")

    return (False, None)

def error_type_D(line):
    if len(line) != 3:
        return (True, "Wrong syntax used for instructions")

    elif line[1] == 'FLAG':
        return (True, "Illegal use of FLAGS register")

    elif line[1] not in ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6']:
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

def error_type_Halt(arr):
    count = 0
    for i in arr:
        if i[0] == "hlt":
            count += 1

    if count == 0:
        return (True, "Missing hlt instruction")

    elif count == 1:
        for i in range(len(arr)-1, 0, -1):
            if arr[i] != [] and arr[i][0] != "hlt":
                return (True, "hlt not being used as the last instruction")
            elif arr[i] != [] and arr[i][0] == "hlt":
                return (False, None)

    else:
        return(True, "More than one hlt instruction")

