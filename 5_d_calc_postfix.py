def calc_operation(a, b, operation):
    result = 0

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        result = a / b

    return result


def calc_postfix(symbols):
    stack = []

    for sym in symbols:
        if sym.isdigit():
            stack.append(int(sym))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(calc_operation(a, b, sym))

    return None if len(stack) == 0 else stack.pop()


if __name__ == '__main__':
    _symbols = input().split()

    print(calc_postfix(_symbols))
