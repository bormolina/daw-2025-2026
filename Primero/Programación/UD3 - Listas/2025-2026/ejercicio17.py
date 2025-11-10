nums = []
sumatoria = 0

while True:
    n = int(input("Inserta un número: "))

    if n == 0:
        break
    else:
        nums.append(n)
        sumatoria += n

media = sumatoria / len(nums)
print(f"La media es {media}")

for n in nums:
    if n > media:
        print(f"{n} es mayor que la media")