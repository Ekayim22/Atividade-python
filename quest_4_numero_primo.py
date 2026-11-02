def verificar_se_numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:    
            return False
    return True
for i in range(1, 101):
    if verificar_se_numero_primo(i):
        print(f"{i} verdadeiro.")
    else:
        print(f"{i} falso.")