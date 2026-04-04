"""Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de
 clientes para gerar relatórios mensais. 
 Para isso, ela precisa escrever um programa
  que percorra a lista de nomes e exiba cada cliente."""


# clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
# for cliente in clientes:
#     print(cliente)


# 1. Começamos com a lista atual (ou uma lista vazia [])
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

print("--- Sistema de Cadastro de Clientes ---")
print("Digite o nome do cliente ou 'sair' para encerrar.\n")

# 2. Criamos um loop que roda enquanto a condição for verdadeira
while True:
    novo_nome = input("Nome do novo cliente: ").strip().capitalize()

    # 3. Condição de paragem: se o usuário digitar 'sair'
    if novo_nome.lower() == 'sair':
        break 
    
    # 4. Adicionamos o nome à lista usando o método .append()
    if novo_nome != "":
        clientes.append(novo_nome)
        print(f"✅ {novo_nome} adicionado com sucesso!")
    else:
        print("⚠️ Erro: O nome não pode estar vazio.")

# 5. Exibimos o relatório final usando o 'for' que aprendemos antes
print("\n--- Relatório Final de Clientes ---")
for cliente in clientes:
    print(f"- {cliente}")