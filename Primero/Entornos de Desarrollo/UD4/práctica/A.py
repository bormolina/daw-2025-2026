class A:
    def __init__(self, a1: int, a2: str):
        self.a1 = a1
        self.a2 = a2

    def __str__(self):
        v = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{v.get(self.a1, self.a1)}{self.a2}"