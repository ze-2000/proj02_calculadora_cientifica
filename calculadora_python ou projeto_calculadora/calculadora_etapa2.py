# Definir funções para adição, subtração, multiplicação e divisão
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

# Solicitar ao usuário que insira o primeiro número
num1 = float(input("Insira o primeiro número: "))

# Solicitar ao usuário que insira o segundo número
num2 = float(input("Insira o segundo número: "))

# Solicitar ao usuário que insira o operador
operador = input("Insira o operador (+, -, *, /): ")

# Chamar a função correspondente com base no operador inserido
if operador == '+':
    resultado = adicao(num1, num2)
elif operador == '-':
    resultado = subtracao(num1, num2)
elif operador == '*':
    resultado = multiplicacao(num1, num2)
elif operador == '/':
    resultado = divisao(num1, num2)
else:
    resultado = "Operador inválido!"

# Exibir o resultado
print("Resultado:", resultado)
