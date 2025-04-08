hora1 = int(input("Digite a primeira hora:"))
minuto1 = int(input("Digite o primeiro minuto:"))
hora2 = int(input("Digite a segunda hora:"))
minuto2 = int(input("Digite o segundo minuto:"))

minuto = minuto1 + minuto2
hora = hora1 + hora2

if minuto >= 60:
    hora += 1
if minuto >= 60:
    minuto -= 60
if hora1 >= 12:
    hora -= 12
if hora2 >= 12:
    hora -= 12
if hora >= 12:
    hora -= 12

print (f"São {hora} horas e {minuto} minutos.")