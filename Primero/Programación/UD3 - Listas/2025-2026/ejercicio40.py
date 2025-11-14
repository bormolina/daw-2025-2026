def convertir_lista_str2int(l: list[str]) -> list[int]:
    l2 = []
    for e in l:
        l2.append(int(e))
    return l2

nums_txt = input("Insertas números separados por ; ")
nums = convertir_lista_str2int(nums_txt.split(";"))
num_min = min(nums)
num_max = max(nums)
num_sum = sum(nums)
num_media = num_sum/len(nums)

print(f"El mínimo es: {num_min}")
print(f"El máximo es: {num_max}")
print(f"La suma es: {num_sum}")
print(f"La media es: {num_media}")

