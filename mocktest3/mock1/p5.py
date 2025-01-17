class C:
    def __init__(self, initial_value):
        self.value = initial_value

    def m1(self):
        return self.value

    def m2(self):
        self.value += 1

    def m3(self):
        self.value -= 1

    def m4(self, n):
        self.value += n

    def __str__(self):
        return str(self.value)
