class PriorityQueue:
    def __init__(self, container=None):
        if container is None:
            self.container = []
        else:
            self.container = container
            self._heapify()

    def _heapify(self):
        n = len(self.container)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i, n)

    def _sift_down(self, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and self.container[left] > self.container[largest]:
            largest = left
        if right < n and self.container[right] > self.container[largest]:
            largest = right
        if largest != i:
            self.container[i], self.container[largest] = self.container[largest], self.container[i]
            self._sift_down(largest, n)

    def is_empty(self):
        return len(self.container) == 0

    def count(self):
        return len(self.container)

    def push(self, item):
        self.container.append(item)
        self._sift_up(len(self.container) - 1)
        self.container = sorted(self.container, reverse = True)
        

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.container[parent] < self.container[i]:
            self.container[i], self.container[parent] = self.container[parent], self.container[i]
            i = parent
            parent = (i - 1) // 2

    def pop(self):
        if len(self.container) == 0:
            raise IndexError("pop from empty priority queue")
        item = self.container[0]
        last_item = self.container.pop()
        if len(self.container) > 0:
            self.container = sorted(self.container, reverse = True)
            self.container[0] = last_item
            self._sift_down(0, len(self.container))
        return item

    def peek(self):
        if len(self.container) == 0:
            raise IndexError("peek from empty priority queue")
        return self.container[0]
    
    
    def print_all(self):
           for item in self.container:
               print(item)    
    