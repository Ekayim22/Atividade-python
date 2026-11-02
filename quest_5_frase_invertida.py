def letras_invertidas(frase):
    palavras = frase.split()
    palavras_invertidas = [''.join(reversed(palavra)) for palavra in palavras]
    return ' '.join(palavras_invertidas)
print(letras_invertidas(input("Digite uma frase: ")))