"""Este é o primeiro parágrafo do meu texto.
Aqui tem informações importantes.
Este é o segundo parágrafo.
Mais conteúdo para ser comentado.
Terceiro parágrafo finalizando."""


"""temperatura = float(input('Digite a temperatura atual da sala: '))

if temperatura > 25:
    print('ALERTA: A temperatura ultrapassou 25°C! Acionar resfriamento.')
else:
    print('A temperatura está dentro do limite permitido.')"""

temperaturaLimite = 25

temperatura = float(input('Digite a temperatura atual da sala: '))

if temperatura > temperaturaLimite:
    print('ALERTA: A temperatura ultrapassou 25°C! Acionar resfriamento.')
else:
    print('A temperatura está dentro do limite permitido.')
