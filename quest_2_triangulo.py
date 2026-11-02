import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
if a < b + c and b < a + c and c < a + b:
    p=(a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Os valores formam um triângulo.")
    print("A área do triângulo é: ", round(area, 2))
else:
    print("Os valores não formam um triângulo.")
    print("Valores informados:", a, b, c)