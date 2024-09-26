def sift_down(a, i, size):
    max_index = i

    left_child = i * 2 + 1

    if left_child < size and a[left_child] > a[max_index]:
        max_index = left_child

    right_child = i * 2 + 2

    if right_child < size and a[right_child] > a[max_index]:
        max_index = right_child

    if i != max_index:
        a[i], a[max_index] = a[max_index], a[i]
        sift_down(a, max_index, size)


def build_heap(a):
    for i in range(len(a) // 2, -1, -1):
        sift_down(a, i, len(a))


if __name__ == '__main__':
    n = int(input())

    if n > 0:
        arr = list(map(int, input().split()))

        build_heap(arr)

        size_ = len(arr)
        for _i in range(len(arr) - 1):
            arr[0], arr[size_ - 1] = arr[size_ - 1], arr[0]
            size_ -= 1
            sift_down(arr, 0, size_)

        print(*arr)
