def quicksort(array):
    if len(array) < 2:
        return array  # Caso-base: arrays com 0 ou 1 elemento já estão "ordenados"
    else:
        pivo = array[0]  # Escolha do pivô (usando o primeiro elemento como exemplo)
        menores = [i for i in array[1:] if i <= pivo]  # Subarray de elementos menores ou iguais
        maiores = [i for i in array[1:] if i > pivo]   # Subarray de elementos maiores
        return quicksort(menores) + [pivo] + quicksort(maiores)


if __name__ == "__main__":
    exemplo_array = [10, 5, 2, 3, 45, 234, 1, 2]
    print(f"Array original: {exemplo_array}")
    print(f"Array ordenado: {quicksort(exemplo_array)}")