def fatorial(n):
    resultado = 1
    i = 2
    while i <= n:
        resultado *= i
        i += 1
    return resultado


def main():
    valor = int(input("Digite um valor inteiro: "))
    resultado = fatorial(valor)
    print(f"O fatorial de {valor} é {resultado}")


main()