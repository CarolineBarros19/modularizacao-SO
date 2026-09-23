# 22) Receber 2 valores inteiros e diferentes. Mostrar em ordem crescente.
 
#Declaração de variáveis
valor1 = 0
valor2 = 0
 
 
def ler_valores():
    global valor1, valor2
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro (diferente do primeiro): "))
 
 
def mostrar_ordem_crescente():
    global valor1, valor2
    if valor1 < valor2:
        print(f"Ordem crescente: {valor1}, {valor2}")
    else:
        print(f"Ordem crescente: {valor2}, {valor1}")
 
 
def main():
    ler_valores()
    mostrar_ordem_crescente()
 
 
if __name__ == "__main__":
    main()