class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if not str(n).isdigit():
            raise ValueError

        if self.size + n > self.capacity:
            raise ValueError

        self.size += n

    def withdraw(self, n):
        if not str(n).isdigit():
            raise ValueError

        if self.size - n < 0:
            raise ValueError

        self.size -= n

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        if not str(capacity).isdigit():
            raise ValueError

        self._capacity = capacity

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size
    @size.setter
    def size(self, size):
        if not str(size).isdigit() or size > self.capacity:
            raise ValueError

        self._size = size
