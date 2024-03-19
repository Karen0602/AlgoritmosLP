a = float(input("Digite um lado do triâgulo: "))
b = float(input("Digite um lado do triâgulo: "))
c = float(input("Digite um lado do triâgulo: "))

if (a +b < c) or (b + c < a) or (c + a < b):
    print("Isso não é um triângulo")
    if (a == b == c):
        print("Esse triângulo é um Equilitáreo")
        if (a == b) or (b == c) or (a == c):
            print("Esse triângulo é um Isósceles")
        else:
            print("Esse triângulo é escaleno")
else:
    print("Isso é um triângulo")

