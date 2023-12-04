

def evaluate_npi(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    tokens = expression.split()

    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]
