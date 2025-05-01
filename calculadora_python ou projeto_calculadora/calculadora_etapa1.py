# Solicitar ao usuário que insira o primeiro número
num1 = float(input("Insira o primeiro número: "))

# Solicitar ao usuário que insira o segundo número
num2 = float(input("Insira o segundo número: "))

# Solicitar ao usuário que insira o operador
operador = input("Insira o operador (+, -, *, /): ")

# Realizar o cálculo com base no operador inserido
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero!"
else:
    resultado = "Operador inválido!"

# Exibir o resultado
print("Resultado:", resultado)
