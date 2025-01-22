#Heap Sort
#O(nlogn)

#A Heap is a complete binary tree data structure that satisfies the heap property: 
#for every node, the value of its children is greater than or equal to its own value.

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

class Heap:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def parent(self, j):
        return (j - 1) // 2

    def left(self, j):
        return 2 * j + 1

    def right(self, j):
        return 2 * j + 2

    def has_left(self, j):
        return self.left(j) < len(self.data)

    def has_right(self, j):
        return self.right(j) < len(self.data)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        # Insertion
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.upheap(parent)

    def downheap(self, j):
        # Deletion
        if self.has_left(j):
            left = self.left(j)
            small_child = left
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)

    def insert(self, key, value):
        self.data.append(Item(key, value))
        self.upheap(len(self.data) - 1)

    def extract_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        self.swap(0, len(self.data) - 1)
        item = self.data.pop()
        self.downheap(0)
        return item.value  # You can also return item.key if needed

def heap_sort(lst):
    h = Heap()
    for x in lst:
        h.insert(x, x)  # Assuming x is both key and value
    sorted_lst = []
    while not h.is_empty():
        sorted_lst.append(h.extract_min())
    return sorted_lst


#example

print(heap_sort([4,8,9,20,34,78,1,50]))