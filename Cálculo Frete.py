# Frete Para Entregas

# 1. Entrada de dados
distancia = float(input("Digite a distância da entrega em km: "))
chovendo = input("Está chovendo no momento? (s/n): ").strip().lower()

# 2. Determina a taxa base
if distancia <= 5:
    taxa_base = 5.00
elif distancia <= 10:
    taxa_base = 8.00
else:
    taxa_base = 10.00

# 3. Aplica o adicional de chuva
if chovendo == 's':
    taxa_final = taxa_base + 2.00
else:
    taxa_final = taxa_base

# 4. Saída do resultado
print(f"O valor final da entrega é: R$ {taxa_final:.2f}")

