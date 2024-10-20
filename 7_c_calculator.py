import sys


def calculator_path(operations):
    i = len(operations) - 1

    result = []

    while i != 0:
        result.insert(0, i)

        div_3 = operations[i // 3] if i % 3 == 0 else sys.maxsize
        div_2 = operations[i // 2] if i % 2 == 0 else sys.maxsize
        minus_1 = operations[i - 1]

        if div_3 <= div_2 and div_3 <= minus_1:
            i = i // 3
        elif div_2 <= div_3 and div_2 <= minus_1:
            i = i // 2
        else:
            i = i - 1

    return result


def calculator(n):
    operations = [0, 0]

    for i in range(2, n + 1):
        div_3 = operations[i // 3] if i % 3 == 0 else sys.maxsize
        div_2 = operations[i // 2] if i % 2 == 0 else sys.maxsize
        minus_1 = operations[i - 1]

        operations.append(min(div_3, div_2, minus_1) + 1)

    return operations


def main():
    n = int(input())

    operations = calculator(n)

    print(operations[n])
    print(*calculator_path(operations))


if __name__ == '__main__':
    main()
