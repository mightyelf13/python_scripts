class CircularQueue:
    def __init__(self, size):
        self.s = size
        self.e = size * [None]
        self.h = 0
        self.t = 0
        self.c = 0

    def enqueue(self, v):
        if self.c == self.s:
            self._r()
        self.e[self.t] = v
        self.t = (self.t + 1) % self.s
        self.c += 1

    def dequeue(self):
        v = self.e[self.h]
        self.h = (self.h + 1) % self.s
        self.c -= 1
        return v

    def count(self):
        return self.c

    def avg(self):
        if self.c == 0:
            return 0
        return sum(val for val in self.e if val is not None) / self.c

    def _r(self):
        ns = 2 * self.s
        na = ns * [None]

        if self.h < self.t:
            na[:self.c] = self.e[self.h:self.t]
        else:
            na[:self.s - self.h] = self.e[self.h:]
            na[self.s - self.h:self.s - self.h + self.t] = self.e[:self.t]

        self.e = na
        self.h = 0
        self.t = self.c
        self.s = ns
        print(f"Resized to {ns} elements")