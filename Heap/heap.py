class Heap:
    def __init__(self, desc=False) -> None:
        """
        Initialization
        Default: min heap
        """
        self.heap = []
        self.desc = desc

    def size(self):
        return len(self.heap)

    def top(self):
        """
        return the top element in the heap
        """
        if self.size():
            return self.heap[0]
        return None

    def push(self, item):
        """
        push an element into the heap and heapify
        """
        self.heap.append(item)
        self._sift_up(self.size() - 1)

    def pop(self):
        """
        pop the top element in the heap
        """
        item = self.heap[0]
        self._swap(0, self.size() - 1)
        self.heap.pop()
        self._sift_down(0)
        return item

    def _smaller(self, lhs, rhs):
        return lhs > rhs if self.desc else lhs < rhs

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        while index:
            parent = (index - 1) // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        while index * 2 + 1 < self.size():
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size() and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest


# testing
test_list = input()
test_list = test_list.split(" ")
test_list = [int(ele) for ele in test_list]
print(test_list)

heap = Heap()
for ele in test_list:
    heap.push(ele)

while heap.size():
    print(heap.pop())
