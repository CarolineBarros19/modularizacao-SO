#24) Receber um valor inteiro. Verificar e mostrar se é divisível por 2 e por 3.

#Declaração de variáveis
valor = 0
 
 
def ler_valor():
    global valor
    valor = int(input("Digite um valor inteiro: "))
 
 
def verificar_e_mostrar():
    global valor
    divisivel_por_2 = (valor % 2 == 0)
    divisivel_por_3 = (valor % 3 == 0)
 
    if divisivel_por_2 and divisivel_por_3:
        print(f"{valor} é divisível por 2 e por 3.")
    elif divisivel_por_2:
        print(f"{valor} é divisível apenas por 2.")
    elif divisivel_por_3:
        print(f"{valor} é divisível apenas por 3.")
    else:
        print(f"{valor} não é divisível nem por 2 nem por 3.")
 
 
def main():
    ler_valor()
    verificar_e_mostrar()
 
 
if __name__ == "__main__":
    main()