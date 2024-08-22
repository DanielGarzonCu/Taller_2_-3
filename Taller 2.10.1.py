def multiplos_de_tres(lista: list) -> list:
    """
    Filtra y retorna los números de la lista que son múltiplos de 3.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    list: Una lista con los números de la lista original que son múltiplos de 3.
    """
    # Utiliza una comprensión de listas para filtrar los números que son múltiplos de 3
    return [multiplo for multiplo in lista if multiplo % 3 == 0]

if __name__ == "__main__":
    # Solicita al usuario que ingrese números para formar una lista
    print("Ingrese los números de la lista. Para terminar, ingrese 'fin'.")
    lista = []

    while True:
        entrada = input("Ingresar número: ")
        if entrada.lower() == "fin":  # Verifica si el usuario desea finalizar la entrada
            break
        try:
            # Convierte la entrada a float y la agrega a la lista
            lista.append(float(entrada))
        except ValueError:
            # Maneja entradas no válidas que no se pueden convertir a float
            print("Por favor, ingrese un número válido o 'fin' para terminar.")
    
    # Llama a la función para obtener los múltiplos de 3 y almacena el resultado
    resultado_multiplos = multiplos_de_tres(lista)
    
    # Imprime los números que son múltiplos de 3
    print(f"Los números múltiplos de 3 de la lista son: {resultado_multiplos}")