def prefix(values):
    perority = {
        0 : ['*', '/'],
        1 : ['+', '-']
    }
    operators = []
    result = []

    for value in values:
        if value in perority[0]:
            operators.append(value)
        elif value in perority[1]:
            if operators and operators[-1] in perority[0]:
                while operators:
                    result.append(operators.pop())
                operators.append(value)
            else:
                operators.append(value)
        else:
            result.append(value)
   
    if operators:
        while operators:
            result.append(operators.pop())
    return result

print(prefix('1+3*5-8/2'))