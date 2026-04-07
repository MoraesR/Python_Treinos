distancia = float(input("Digite a distância percorrida em km: "))

print("Preço Tabelado de Pedágio: ")

if distancia <= 100:
    valor_pedagio = 10.00
elif distancia <= 200:
    valor_pedagio = 20.0
else:
    valor_pedagio = 30.00


print(f"Para uma distância de {distancia} KM, o valor é: R$ {valor_pedagio:.2f}")