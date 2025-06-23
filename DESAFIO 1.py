#Dado el peso y estatura calcula el IMC y clacifica: bajo, normal, sobrepeso y obesidad

peso = float(input("Ingresa tu peso: "))
estatura = float(input("Ingresa tu estatura: "))
oper = estatura**2
oper1 = peso / oper

if oper1 <= 18.5:
    print("Tu peso es bajo")
elif oper1 <= 24.9:
    print("Tu peso es normal")
elif oper1 >= 25 and oper1 <= 29.9:
    print("Tu peso es sobrepeso")
else:
    print("Tu peso es obesidad")