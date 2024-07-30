def circulo(raio):
    area = pi * (raio * raio)
    return area

raio = float(input("Digite o raio do círculo: "))
pi = 3.14
area = circulo(raio)
print(f"A área do círculo com raio {area}")


