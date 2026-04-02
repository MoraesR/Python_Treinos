print("""                                               
,--.   ,--.                ,--.                
 \  `.'  /,---. ,--,--,  ,-|  | ,--,--. ,---.  
  \     /| .-. :|      \' .-. |' ,-.  |(  .-'  
   \   / \   --.|  ||  |\ `-' |\ '-'  |.-'  `) 
    `-'   `----'`--''--' `---'  `--`--'`----'  
""")

p1 = int(input('Digite o número de venda do abacaxi: '))
p2 = int(input('Digite o número de venda da banana:  '))

print(f'Vendas do Abacaxi: {p1}')
print(f'Vendas do Abacaxi: {p2}')

if p1 > p2:
    print(f'O número de vendas do Abacaxi é maior que o de Banana: {p1} ')
elif p2 > p1:
    print(f'O número de vendas da Banana é maior que o de Abacaxi: {p2} ')
else:
    print("empate")
