def calcArea(base,altura):
    area = (base * altura) / 2
    return area

base = float(input("Digite a base")) 
altura = float(input("Digite a altura"))
area = calcArea(base,altura)
print(f"A área do quadrado é {area}")