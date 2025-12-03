nums = []

while True:
    n = int(input('Inserta un número (0 para terminar): '))

    if n == 0:
        break

    nums.append(n)
    print(f'Números introducidos: {nums}')

media = sum(nums) / len(nums)
mayores = [n for n in nums if n > media]
menores = [n for n in nums if n < media]
n_max = max(nums)
n_min = min(nums)
nums.sort()
tam = len(nums)

if tam % 2 == 0:
    mediana = (nums[tam//2] + nums[tam//2+1]) / 2
else:
    mediana = nums[tam//2]

print(f'La media es: {media}')
print(f'Los números mayores que la media son: {mayores}')
print(f'La números menores que la media son: {menores}')
print(f'El máximo es: {n_max}')
print(f'El mínimo es: {n_min}')