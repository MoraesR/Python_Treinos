#calculadora de Idade

def calculadora_idade():
    nasc = int(input("digite o ano de nascimento: "))
    ano = int(input("digite o ano atual: "))
    idade = ano - nasc
    print(idade)




def main():
    print("--- Bem-vindo à Calculadora de Idade ---")
    calculadora_idade()

if __name__ == "__main__":
    main()