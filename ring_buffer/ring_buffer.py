class RingBuffer:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.position = 0
        self.list = []

    def append(self, item):
        if len(self.list) < self.capacity:

            self.list.append(item)

        else:

            self.list.pop(self.position)
            self.list.insert(self.position, item)
            self.position += 1
            if self.position == self.capacity:
                self.position = 0

    def get(self):
        return self.list


buffer = RingBuffer(3)

buffer.get()   # should return []


print(buffer.get())


buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
# buffer.append('g')
# buffer.append('l')
# buffer.append('m')
# buffer.append('n')

print(buffer.get())
