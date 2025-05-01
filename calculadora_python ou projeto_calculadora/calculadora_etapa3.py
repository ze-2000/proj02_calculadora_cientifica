# Funções para operações básicas
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# Verificar se os números inseridos são válidos
try:
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
except ValueError:
    print("Erro: Entrada inválida! Por favor, insira números válidos.")
    exit()

# Verificar se o operador inserido é válido
operador = input("Insira o operador (+, -, *, /): ")
if operador not in ['+', '-', '*', '/']:
    print("Erro: Operador inválido!")
    exit()

# Realizar o cálculo com base no operador inserido
if operador == '+':
    resultado = adicao(num1, num2)
elif operador == '-':
    resultado = subtracao(num1, num2)
elif operador == '*':
    resultado = multiplicacao(num1, num2)
elif operador == '/':
    resultado = divisao(num1, num2)

# Exibir o resultado
print("Resultado:", resultado)
