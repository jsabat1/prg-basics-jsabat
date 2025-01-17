class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4

    def m2(self, a, b):
        return self.m1() == C(a, b).m1()

    def m3(self, a, b):
        distance = ((self.x - a) ** 2 + (self.y - b) ** 2) ** 0.5
        return distance > 5

# Example usage
p = C(2, 3)
print(p.m1())  # 1
print(p.m2(7, 4))  # True
print(p.m2(-3, 1))  # False
print(p.m3(8, 5))  # True
print(p.m3(4, 7))  # False

p1 = C(0, 5)
print(p1.m1())  # 0
print(p1.m2(4, 7))  # False
print(p1.m2(-7, 0))  # True
