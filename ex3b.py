def fatorial(n):
    resultado = 1
    i = 2
    while i <= n:
        resultado *= i
        i += 1
    return resultado


def divisao(a, b):
    return a / b


def main():
    n = int(input("Digite o valor de N: "))

    soma = 1  # primeiro termo da série
    i = 1
    while i <= n:
        fat = fatorial(i)
        soma += divisao(1, fat)
        i += 1

    print(f"1 + 1/1! + ... + 1/{n}! = {soma}")


main()