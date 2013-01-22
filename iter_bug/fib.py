class fib(object):
    def __init__(self):
        self.last_1 = 1
        self.last_2 = 1

    def __iter__(self):
        return self

    def next(self):
        next_fib = self.last_1 + self.last_2
        self.last_1, self.last_2 = self.last_2, next_fib
        return next_fib

