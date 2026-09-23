#20) Receber A, B e C de uma equação do 2º grau (AX² + BX + C = 0). Verificar a existência de raízes reais e, se existirem, calculá-las e mostrá-las.
 
import math
 
#Declaração de variáveis
a = 0.0
b = 0.0
c = 0.0
delta = 0.0
x1 = 0.0
x2 = 0.0
 
 
def ler_coeficientes():
    global a, b, c
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))
 
 
def calcular_delta():
    global a, b, c, delta
    delta = (b ** 2) - (4 * a * c)
 
 
def calcular_e_mostrar_raizes():
    global a, b, delta, x1, x2
    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui raízes reais.")
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
 
 
def main():
    ler_coeficientes()
    calcular_delta()
    calcular_e_mostrar_raizes()
 
 
if __name__ == "__main__":
    main()