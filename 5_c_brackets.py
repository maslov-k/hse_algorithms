def is_brackets_correct(str):
    brackets = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    stack = []

    for c in str:
        if c in brackets.values():
            stack.append(c)
        elif c in brackets:
            if not stack or stack.pop() != brackets[c]:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    _str = input()

    print('yes' if is_brackets_correct(_str) else 'no')
