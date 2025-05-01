import math

# Funções para cálculos científicos
def potencia(a, b):
    return math.pow(a, b)

def raiz(a):
    return math.sqrt(a)

def seno(a):
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def logaritmo(a):
    return math.log(a)

# Solicitar ao usuário que insira o número para o cálculo científico
num = float(input("Insira o número: "))

# Solicitar ao usuário que insira o operador para o cálculo científico
operador = input("Insira o operador (**, sqrt, sin, cos, tan, log): ")

# Chamar a função correspondente do módulo math
if operador == '**':
    expoente = float(input("Insira o expoente: "))
    resultado = potencia(num, expoente)
elif operador == 'sqrt':
    resultado = raiz(num)
elif operador == 'sin':
    resultado = seno(num)
elif operador == 'cos':
    resultado = cosseno(num)
elif operador == 'tan':
    resultado = tangente(num)
elif operador == 'log':
    resultado = logaritmo(num)
else:
    resultado = "Operador inválido!"

# Exibir o resultado
print("Resultado:", resultado)
