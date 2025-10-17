hora = int(input("Inserta una hora en formato AM/PM: "))
minutos = int(input("Inserta los minutos: "))
periodo = input("Inserta el periodo (AM/PM)")

if periodo == "AM":
    hora24 = hora
elif periodo == "PM":
    hora24 = hora + 12
else:
    print("Periodo no válido")

hora_txt = str(hora)
if hora24 == 24:
    hora_24_txt = "00"
else:
    hora_24_txt = str(hora24)

minutos_txt = str(minutos)

if hora < 10:
    hora_txt = "0"+hora_txt

if hora24 < 10:
    hora_24_txt = "0"+hora_24_txt

if minutos < 10:
    minutos_txt = "0"+str(minutos)

print(f"{hora_txt}:{minutos_txt} {periodo} son las {hora_24_txt}:{minutos_txt}")