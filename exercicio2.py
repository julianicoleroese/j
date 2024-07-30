def area(lado):
    area = (lado * lado)
    return area

lado = float(input("Digite o primeiro lado: "))
area = area(lado)
print(f"A área do quadrado é {area}")