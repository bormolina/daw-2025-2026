from collections import Counter
from A import A

class B:
    def __init__(self, a1: list[A]):
        self.a1 = a1

    def m1(self) -> tuple[int, int]:
        vs = sorted([c.a1 for c in self.a1])
        ps = [c.a2 for c in self.a1]
        cv = Counter(vs)
        cp = Counter(ps)

        es_color = len(cp) == 1
        es_escalera = vs == list(range(vs[0], vs[0] + 5))

        if es_escalera and es_color:
            return (8, max(vs))
        if 4 in cv.values():
            return (7, max(k for k, v in cv.items() if v == 4))
        if sorted(cv.values()) == [2, 3]:
            return (6, max(k for k, v in cv.items() if v == 3))
        if es_color:
            return (5, max(vs))
        if es_escalera:
            return (4, max(vs))
        if 3 in cv.values():
            return (3, max(k for k, v in cv.items() if v == 3))
        if list(cv.values()).count(2) == 2:
            return (2, max(k for k, v in cv.items() if v == 2))
        if 2 in cv.values():
            return (1, max(k for k, v in cv.items() if v == 2))
        return (0, max(vs))
    
    def m2(self) -> str:
        t, _ = self.m1()
        return [
            "Carta alta",
            "Pareja",
            "Doble pareja",
            "Trío",
            "Escalera",
            "Color",
            "Full",
            "Póker",
            "Escalera de color"
        ][t]

    def __str__(self):
        return " ".join(str(c) for c in self.a1)