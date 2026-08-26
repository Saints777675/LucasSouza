# 1. Pergunta a quantidade de itens que o cliente vai pedir
qtd_itens = int(input("Quantos itens o cliente vai pedir? "))

valor_total = 0.0

# 2. Estrutura de repetição para registrar cada item
for i in range(1, qtd_itens + 1):
    print(f"\n--- Item {i} ---")
    nome_item = input("Nome do item: ")
    preco_item = float(input(f"Preço de '{nome_item}': R$ "))
    
    # Soma o preço ao total acumulado
    valor_total += preco_item

print("\n------------------------------")
print(f"Subtotal: R$ {valor_total:.2f}")

# 3. Pergunta se o cliente possui cadastro
cliente_cadastrado = input("O cliente é cadastrado? (s/n): ").strip().lower()

# 4. Aplica o desconto de 10% se for cadastrado
if cliente_cadastrado == 's':
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f"Desconto aplicado (10%): R$ {desconto:.2f}")
    print(f"Valor total com desconto: R$ {valor_final:.2f}")
else:
    valor_final = valor_total
    print("Nenhum desconto aplicado.")
    print(f"Valor total a pagar: R$ {valor_final:.2f}")

print("------------------------------")