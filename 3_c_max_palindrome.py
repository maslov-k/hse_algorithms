import random


def partition3(a, left, right):
    pivot = random.randrange(left, right)

    a[pivot], a[left] = a[left], a[pivot]

    x = a[left]
    j = left

    for i in range(left + 1, right):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]

    a[left], a[j] = a[j], a[left]

    k = j

    for i in range(j + 1, right):
        if a[i] == x:
            k += 1
            a[k], a[i] = a[i], a[k]

    return [j, k]


def quick_sort3(a, left=0, right=-1):
    if right == -1:
        right = len(a)

    while left < right:
        m1, m2 = partition3(a, left, right)

        if m1 - left < right - m2:
            quick_sort3(a, left, m1)
            left = m2 + 1
        else:
            quick_sort3(a, m2 + 1, right)
            right = m1


def max_palindrome(sorted_chars):
    result = []

    once_chars = []

    while len(sorted_chars) > 0:
        c = sorted_chars.pop()

        if len(sorted_chars) > 0 and c == sorted_chars[-1]:
            result.insert(0, c)
            result.append(sorted_chars.pop())
        else:
            once_chars.append(c)

    if len(result) % 2 == 0 and len(once_chars) > 0:
        result.insert(len(result) // 2, once_chars[-1])

    return "".join(result)


if __name__ == '__main__':
    _n = int(input())
    _chars = list(input())

    quick_sort3(_chars)

    print(max_palindrome(_chars))
