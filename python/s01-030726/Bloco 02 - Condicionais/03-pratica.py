# 1. Variávies e Dados.
nome = "Angelo"
idade = 34
peso = 82.0
altura = 1.74
tempo_de_experiencia = 2
vitorias = 12
derrotas = 22
campeonatos = 3
valor_contrato = 45000.0

# 2. Dinâmicas
idade_ideal = 22
peso_ideal = 78.0
altura_ideal = 1.78
experiencia_desejada = 3
vitorias_ideal = 10
campeonatos_ideal = 5
valor_contrato_ideal = 50000.0

# 3. Regras de Negócio
idade_comparada = idade_ideal / idade
peso_comparado = peso_ideal / peso
altura_comparada = altura_ideal / altura
experiencia_desejada = experiencia_desejada / tempo_de_experiencia
vitorias_comparadas = vitorias_ideal / vitorias
campeonatos_comparados = campeonatos_ideal / campeonatos
valor_contrato_comparado = valor_contrato_ideal / valor_contrato

# 4. Resultado
print("Nome:", nome)
print(f"Peso: {((peso_comparado * 100) - 100) * -1:.2f}%")
print(f"Idade: {((idade_comparada * 100) - 100) * -1:.2f}%")
print(f"Altura: {altura_comparada * 100 - 100:.2f}%")
print(f"Experiência: {experiencia_desejada * 100 - 100:.2f}%")
print(f"Vitórias: {((vitorias_comparadas * 100) - 100) * -1:.2f}%")
print(f"Campeonatos: {campeonatos_comparados * 100 - 100:.2f}%")
print(f"Valor do Contrato: {((valor_contrato_comparado * 100) - 100) * -1:.2f}%")

# Estudo sobre condicionais
# 5. Tomada de Decisão (Condicional)
# if valor_contrato <= valor_contrato_ideal:
#   print("Veredito: Contrato Aprovado! Está dentro do orçamento.")
# else:
#   print("Veredito: Contrato Recusado! O jogador está muito caro.")

# 6. Tomada de Decisão Avançada (Conhecendo "and/or")
# if valor_contrato <= valor_contrato_ideal and vitorias_ideal:
#  print("Veredito: Contrato Aprovado! Ótimo custo-benefício!")
# else:
#  print("Veredito: Contrato Recusado! O jogador não atende aos requisitos.")

# 7. Tomada de Decisão (Condicional) com "or"
if valor_contrato <= valor_contrato_ideal or vitorias >= vitorias_ideal:
    print("Veredito: Contrato Aprovado! Ótimo custo-benefício!")
else:
    print("Veredito: Contrato Recusado! O jogador não atende aos requisitos.")
