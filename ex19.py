#19) Receba 2 valores reais. Calcule e mostre o maior deles.

num1 = 0.0
num2= 0.0
maior = 0.0
 
 
def ler_valores():
    global num1, num2
    num1 = float(input("Digite o primeiro número real: "))
    num2 = float(input("Digite o segundo número real: "))
 
 
def calcular_maior():
    global num1, num2, maior
    if num1 > num2:
        maior = num1
    else:
        maior = num2
 
 
def mostrar_resultado():
    global maior
    print(f"O maior valor é: {maior}")
 
 
def main():
    ler_valores()
    calcular_maior()
    mostrar_resultado()
 
 
if __name__ == "__main__":
    main()