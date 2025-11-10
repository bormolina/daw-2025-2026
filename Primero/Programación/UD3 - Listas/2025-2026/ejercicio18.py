a = int(input("Inserta el inicio: "))
b = int(input("Inserta el final: "))

if a % 2 == 1:
    a += 1

if a % 2 == 0:
    b += 1

# Sin listas
for i in range(a, b, 2):
    print(i)

# Con listas
nums = []
for i in range(a, b, 2):
    nums.append(i)

print(nums)