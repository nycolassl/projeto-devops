def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


if __name__ == "__main__":
    resultado_soma = somar(10, 5)
    resultado_subtracao = subtrair(10, 5)
    resultado_multiplicacao = multiplicar(10, 5)
    resultado_divisao = dividir(10, 5)

    print(f"Resultado da soma: {resultado_soma}")
    print(f"Resultado da subtração: {resultado_subtracao}")
    print(f"Resultado da multiplicação: {resultado_multiplicacao}")
    print(f"Resultado da divisão: {resultado_divisao}")
