minerales_magneticos = ["Magnetita", "Hematita", "Pirita", "Ilmenita", "Cobaltoita"]
minerales_metalicos  = ["Pirita", "Galena", "Hematita", "Bornita", "Calcopirita", "Cobaltoita"]
minerales_no_metalicos = ["Cuarzo", "Calcita", "Fluorita", "Pirita", "Yeso", "Malaquita"]

apartadoA = set(minerales_magneticos) & set(minerales_metalicos)
print(apartadoA)

apartadoB = set(minerales_magneticos) & (set(minerales_magneticos) | set(minerales_no_metalicos))
print(apartadoB)