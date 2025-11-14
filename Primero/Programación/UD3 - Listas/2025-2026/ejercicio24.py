nums = []

while True:
    n = int(input("Inserta un núm: "))

    if n == 0:
        break
    
    nums.append(n)

while len(nums) > 0:
    print(nums.pop())

# con recursividad
"""
def reverso(nums: list[int]):
    if len(nums) == 0:
        return
    else:
        print(nums.pop())
        return reverso(nums)
    
reverso(nums)
"""