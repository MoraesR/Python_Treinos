# #Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: 
# A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores 
# inseridos são inválidos e não calcular o total.

# # Escreva um programa que receba o número de dias de três 
# atividades e exiba o tempo total do projeto. Se algum valor 
# for negativo, mostre uma mensagem informando o erro.

HORAS_POR_DIA = 24
MINUTOS_POR_HORA = 60
SEGUNDOS_POR_MINUTO = 60


a = int(input('Informe o número de dias para a atividade A: '))
b = int(input('Informe o número de dias para a atividade B: '))
c = int(input('Informe o número de dias para a atividade C: '))

if a < 0 or b < 0 or c < 0:
    print("Erro: Os valores inseridos são inválidos (número negativo).")
else:
    total = a + b + c
    horas = total * HORAS_POR_DIA
    minutos = horas * MINUTOS_POR_HORA
    segundos = minutos * SEGUNDOS_POR_MINUTO
    print(f'O tempo total do projeto é de {total} dias.\n'
          f'{horas} horas, {minutos} minutos e {segundos} segundos.')