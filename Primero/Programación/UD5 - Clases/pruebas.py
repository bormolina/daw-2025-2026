nums = [2, 8, -1, 3, -3, -5, 9]

negativos = [x for x in nums if x < 0]
primero = negativos[0] if negativos else None

for x in nums:
    if x < 0:
        primero = x
        break

primero = next((x for x in nums if x < 0), None)
print(primero)

