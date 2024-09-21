import random


def partition(a, left, right):
    pivot = random.randrange(left, right)
    a[pivot], a[left] = a[left], a[pivot]

    x = a[left]
    j = left

    for i in range(left + 1, right):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]

    a[left], a[j] = a[j], a[left]

    return j


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


def quick_sort(a, left=0, right=-1):
    if right == -1:
        right = len(a)

    while left < right:
        m = partition(a, left, right)

        if m - left < right - m:
            quick_sort(a, left, m)
            left = m + 1
        else:
            quick_sort(a, m + 1, right)
            right = m


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
