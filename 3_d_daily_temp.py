def daily_temp(temps):
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            cold_i = stack[-1]
            result[cold_i] = i - cold_i
            stack.pop()

        stack.append(i)

    return result


if __name__ == '__main__':
    _n = int(input())
    _temps = list(map(int, input().split()))

    print(*daily_temp(_temps))
