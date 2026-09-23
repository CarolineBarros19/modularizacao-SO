#Exercício 18) Receber 2 valores inteiros e calcular a diferença entre o maior e o menor valor.
#Declaração de variáveis
valor1 = 0
valor2 = 0
resultado = 0
 
 
def ler_valores():
    global valor1, valor2
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))
 
 
def calcular_diferenca():
    global valor1, valor2, resultado
    if valor1 > valor2:
        resultado = valor1 - valor2
    else:
        resultado = valor2 - valor1
 
 
def mostrar_resultado():
    global resultado
    print(f"A diferença entre o maior e o menor valor é: {resultado}")
 
 
def main():
    ler_valores()
    calcular_diferenca()
    mostrar_resultado()
 
 
if __name__ == "__main__":
    main()