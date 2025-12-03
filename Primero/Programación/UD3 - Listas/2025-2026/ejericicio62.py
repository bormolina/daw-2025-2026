mobs_hostiles = ["Zombie", "Skeleton", "Creeper", "Creeper", "Enderman", "Ghast", "Piglin"]
mobs_pacíficos = ["Cow", "Sheep", "Pig", "Villager", "Villager", "Enderman"]
mobs_del_Nether = ["Ghast", "Piglin", "Hoglin", "Blaze", "Enderman"]

# 1) 
mobs_hostiles_b = list(set(mobs_hostiles))
mobs_pacíficos_b = list(set(mobs_pacíficos))
mobs_del_Nether_b = list(set(mobs_del_Nether))

# 2)
lista2 = list(set(mobs_hostiles) - set(mobs_del_Nether))
print(lista2)

# 3)
list3 = list(set(mobs_pacíficos) & set(mobs_del_Nether))
print(list3)

#4
list4 = list(set(mobs_hostiles) & set(mobs_del_Nether) & set(mobs_pacíficos))
print(list4)

#5
list5 = list(set(mobs_hostiles) | set(mobs_del_Nether) | set(mobs_pacíficos))
print(list5)

#6
list6 = list(set(mobs_del_Nether) - set(mobs_hostiles))
print(list6)

#7
print('La lista de los mobs hostiles tiene repetidos' if len(set(mobs_hostiles)) != len(mobs_hostiles) else 'La lista de los mobs hostiles NO tiene repetidos')

print('La lista de los mobs pacíficos tiene repetidos' if len(set(mobs_pacíficos)) != len(mobs_pacíficos) else 'La lista de los mobs pacíficos NO tiene repetidos')

print('La lista de los mobs del Nether tiene repetidos' if len(set(mobs_del_Nether)) != len(mobs_del_Nether) else 'La lista de los mobs del Nether NO tiene repetidos')

#8
list8 = list((set(mobs_pacíficos) | set(mobs_hostiles)) -set(mobs_del_Nether))
print(list8)