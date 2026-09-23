#21)Receber 4 notas bimestrais, calcular a média aritmética e mostrar a situação do aluno.
 
# Definição de variáveis
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
media = 0.0
 
 
def ler_notas():
    global nota1, nota2, nota3, nota4
    nota1 = float(input("Digite a nota do 1º bimestre: "))
    nota2 = float(input("Digite a nota do 2º bimestre: "))
    nota3 = float(input("Digite a nota do 3º bimestre: "))
    nota4 = float(input("Digite a nota do 4º bimestre: "))
 
 
def calcular_media():
    global nota1, nota2, nota3, nota4, media
    media = (nota1 + nota2 + nota3 + nota4) / 4
 
 
def mostrar_resultado():
    global media
    print(f"A média do aluno é: {media}")
    if media >= 6.0:
        print("APROVADO")
    elif media >= 3.0:
        print("EXAME")
    else:
        print("RETIDO")
 
 
def main():
    ler_notas()
    calcular_media()
    mostrar_resultado()
 
 
if __name__ == "__main__":
    main()