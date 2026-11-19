class DynamicArray:
    
    # O(n) - n = capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity


    # O(1)
    def get(self, i: int) -> int:
        # assumes i is always valid
        if i >= self.size:
            return -1
        return self.arr[i]

    # O(1)
    def set(self, i: int, n: int) -> None:
        # assumes i is always valid
        self.arr[i] = n

    # O(1), avg to O(n), worst
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    # O(1) - Soft delete
    def popback(self) -> int:
        if self.size == 0:
            raise "problem"

        self.size -= 1
        return self.arr[self.size]  # Mental note: Size is 1-indexed, but arrays are not.
                                    # Returning the decremented value is the correct "last value"
 
    # O(n) - n = capacity
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # O(1)
    def getSize(self) -> int:
        return self.size
        
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity
