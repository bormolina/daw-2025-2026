nums = []

while True:
    n = int(input("Inserta un num: "))
    
    if n == 0:
        break

    if len(nums) == 0:
        nums.append(n)
    else:
        insertado = False
        for i in range(0, len(nums)+1):
            if i<len(nums) and nums[i] > n:
                nums.insert(i, n)
                insertado = True
                break
        if not insertado:
            nums.append(n)

print(nums)