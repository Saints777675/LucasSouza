# Exercício 2: Somador Interativo até Digitar Zero com While

total = 0

# Pedimos o primeiro número antes de entrar no while
numero = int(input("Digite um número inteiro (ou 0 para parar): "))

# O laço continua ENQUANTO o número for diferente (!=) de zero
while numero != 0:
    total += numero  # Acumula o valor digitado no total
    numero = int(input("Digite outro número inteiro (ou 0 para parar): "))  # Pede o próximo número

# Fora do while (quando o usuário digitar 0 e o laço parar):
print(f"\nSoma total de todos os números digitados: {total}")

