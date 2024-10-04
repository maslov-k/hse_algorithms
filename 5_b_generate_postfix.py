PRIORITIES = {
    '+': 0,
    '-': 1,
    '*': 2,
    '/': 3
}


def generate_postfix(infix_str):
    symbols = infix_str.split()

    result = []
    stack = []

    i = 0
    while i < len(symbols):
        sym = symbols[i]

        if sym.isdigit():
            result.append(sym)
        elif sym == '(':
            stack.append(sym)
        elif sym == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        elif sym in PRIORITIES:
            while stack and PRIORITIES[stack[-1]] > PRIORITIES[sym]:
                result.append(stack.pop())

            stack.append(sym)

        i += 1

    while stack:
        result.append(stack.pop())

    return ' '.join(result)


if __name__ == '__main__':
    _infix_str = input()

    print(generate_postfix(_infix_str))
