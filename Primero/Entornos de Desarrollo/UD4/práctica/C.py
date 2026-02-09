import random
from A import A

class C:
    def __init__(self):
        self.a1 = [A(v, p) for v in range(2, 15) for p in ["♠", "♥", "♦", "♣"]]
        random.shuffle(self.a1)

    def m1(self):
        if not self.a1:
            return None
        return self.a1.pop()

    def m2(self, n: int):
        if len(self.a1) < n:
            return None
        return [self.m1() for _ in range(n)]