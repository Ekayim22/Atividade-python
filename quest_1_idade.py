idade = int(input("qual sua idade em dias: "))
ano = 365
meses = 30
dias = 1
resposta1 = (idade // ano)
resposta2 = (idade % ano // meses)
resposta3 = (idade % ano % meses)
print(f"Você tem {resposta1} anos, {resposta2} meses e {resposta3} dias.")