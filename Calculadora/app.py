def soma(primeiro_numero, segundo_numero):
    return float(primeiro_numero) + float(segundo_numero)


def subtracao(primeiro_numero, segundo_numero):
    return float(primeiro_numero) - float(segundo_numero)


def multiplicacao(primeiro_numero, segundo_numero):
    return float(primeiro_numero) * float(segundo_numero)


def divisao(primeiro_numero, segundo_numero):
    return float(primeiro_numero) / float(segundo_numero)


primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")
operador = input("Digite a operador (+ - * /): ")
resultado = 0

if operador in '+-*/':
    if operador == '+':
        resultado = soma(primeiro_numero, segundo_numero)

    elif operador == '-':
        resultado = subtracao(primeiro_numero, segundo_numero)

    elif operador == '*':
        resultado = multiplicacao(primeiro_numero, segundo_numero)

    elif operador == '/':
        resultado = divisao(primeiro_numero, segundo_numero)

    print(f'{primeiro_numero} {operador} {segundo_numero} = {resultado}')

else:
    print(f'Operação {operador} inválida')
