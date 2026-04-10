def contador_char():
    texto = input('insira a palavra que iremos contar: ')

    quantidade = len(texto)
    print(f'{texto} possui {quantidade} caracteres')

def main ():
    print('Vamos contar o número de letras: ')
    contador_char()


if __name__ == '__main__':
    main()