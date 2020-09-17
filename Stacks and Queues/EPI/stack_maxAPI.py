
# Stack with a max API

"""
brutforce
Create a stack using OOP and another variable to store max

"""
"""
# Time complexity is O(n) 
class Stack:
    def __init__(self):
        self.stack = []
        self.maximum = 0 #float("-inf")

    def push(self, element):
        self.stack.append(element)
        self.maximum = max(self.maximum, element)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        self.stack.pop()
        self.maximum = max(self.stack)

    def maxi(self):
        return self.maximum

"""

# Another method with extra stack storing object of (max, count)
class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._elements = []
        self._cached_max_with_counts = []

    def empty(self):
        return len(self._elements) == 0

    def max(self):
        if self.empty():
            raise IndexError("empty stack")
        return self._cached_max_with_counts[-1].max

    def pop(self):
        if self.empty():
            raise IndexError("empty stack")
        pop_element = self._elements.pop()
        current_max = self._cached_max_with_counts[-1].max
        if current_max == pop_element:
            if self._cached_max_with_counts[-1].count > 1:
                self._cached_max_with_counts[-1].count -= 1
            else:
                self._cached_max_with_counts.pop()

        return pop_element

    def push(self, x):
        if self.empty():
            self._elements.append(x)
            self._cached_max_with_counts.append(self.MaxWithCount(x, 1))
        else:
            self._elements.append(x)
            if x == self.max():
                self._cached_max_with_counts[-1].count += 1
            if x > self.max():
                self._cached_max_with_counts.append(self.MaxWithCount(x, 1))

    def print_stacks(self):
        print(self._elements)
        print(self._cached_max_with_counts)

def main():
    s1 = Stack()
    #print(s1.max())
    s1.push(1)
    s1.push(5)
    s1.push(4)
    s1.push(7)
    print(s1.max())
    s1.pop()
    print(s1.max())
    s1.push(6)
    print(s1.max())
    s1.print_stacks()

main()