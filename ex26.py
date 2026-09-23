#26) Receber 2 números inteiros. Verificar e mostrar se o maior número é múltiplo do menor.
 
#Variáveis
valor1 = 0
valor2 = 0
maior = 0
menor = 0
 
 
def ler_valores():
    global valor1, valor2
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))
 
 
def identificar_maior_menor():
    global valor1, valor2, maior, menor
    if valor1 > valor2:
        maior = valor1
        menor = valor2
    else:
        maior = valor2
        menor = valor1
 
 
def verificar_e_mostrar():
    global maior, menor
    if menor != 0 and maior % menor == 0:
        print(f"{maior} é múltiplo de {menor}.")
    else:
        print(f"{maior} NÃO é múltiplo de {menor}.")
 
 
def main():
    ler_valores()
    identificar_maior_menor()
    verificar_e_mostrar()
 
 
if __name__ == "__main__":
    main()