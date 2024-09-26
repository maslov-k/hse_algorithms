class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, el):
        self.heap.append(el)
        self.__sift_up(len(self.heap) - 1)

    def extract_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        result = self.heap.pop()

        self.__sift_down(0)

        return result

    def size(self):
        return len(self.heap)

    def __sift_up(self, i):
        while i > 0 and self.heap[self.__parent(i)] < self.heap[i]:
            parent = self.__parent(i)
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def __sift_down(self, i):
        max_index = i

        left_child = self.__left_child(i)

        if left_child != -1 and self.heap[left_child] > self.heap[max_index]:
            max_index = left_child

        right_child = self.__right_child(i)

        if right_child != -1 and self.heap[right_child] > self.heap[max_index]:
            max_index = right_child

        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.__sift_down(max_index)

    def __parent(self, i):
        result = (i - 1) // 2
        return result if result >= 0 else -1

    def __left_child(self, i):
        result = i * 2 + 1
        return result if result < len(self.heap) else -1

    def __right_child(self, i):
        result = i * 2 + 2
        return result if result < len(self.heap) else -1


if __name__ == '__main__':
    # _n = int(input())

    heap = MaxHeap()

    heap.insert(5)
    heap.insert(12)
    heap.insert(7)
    heap.insert(2)
    heap.insert(1)
    heap.insert(16)
    heap.insert(0)
    heap.insert(11)
    heap.insert(5)
    heap.insert(3)

    while heap.size() > 0:
        print(heap.extract_max())
