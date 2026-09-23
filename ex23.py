#23) Receber 3 valores já em ordem crescente e um 4º valor não necessariamente em ordem. Mostrar os 4 números em ordem crescente.
 
#Definição de variáveis
valor1 = 0
valor2 = 0
valor3 = 0
valor4 = 0
lista_ordenada = []
 
 
def ler_valores():
    global valor1, valor2, valor3, valor4
    valor1 = int(input("Digite o 1º valor (ordem crescente): "))
    valor2 = int(input("Digite o 2º valor (ordem crescente): "))
    valor3 = int(input("Digite o 3º valor (ordem crescente): "))
    valor4 = int(input("Digite o 4º valor (qualquer posição): "))
 
 
def inserir_em_ordem():
    global valor1, valor2, valor3, valor4, lista_ordenada
    if valor4 <= valor1:
        lista_ordenada = [valor4, valor1, valor2, valor3]
    elif valor4 <= valor2:
        lista_ordenada = [valor1, valor4, valor2, valor3]
    elif valor4 <= valor3:
        lista_ordenada = [valor1, valor2, valor4, valor3]
    else:
        lista_ordenada = [valor1, valor2, valor3, valor4]
 
 
def mostrar_resultado():
    global lista_ordenada
    print(f"Ordem crescente: {lista_ordenada[0]}, {lista_ordenada[1]}, {lista_ordenada[2]}, {lista_ordenada[3]}")
 
 
def main():
    ler_valores()
    inserir_em_ordem()
    mostrar_resultado()
 
 
if __name__ == "__main__":
    main()