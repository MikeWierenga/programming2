class Demo:
    def __init__(self):
        self.data = [0, 1, 1, 2, 3, 5, 8]
        self.pointer = -1
 
    
    def __next__(self):
        self.pointer += 1
        if self.pointer == len(self.data):
            raise StopIteration
        return self.data[self.pointer]
    
d = Demo()
for x in range(5):
    print(next(d))




