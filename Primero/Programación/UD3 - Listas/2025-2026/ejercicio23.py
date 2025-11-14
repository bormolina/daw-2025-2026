nums = []

while True:
    n = int(input("Inserta un número: "))

    if n >= 0:
        nums.append(n)
    else:
        nums.remove(n*-1)
    
    print(nums)