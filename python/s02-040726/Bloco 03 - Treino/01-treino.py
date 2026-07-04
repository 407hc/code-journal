# Objetivos:
#   1 - Comparar valores de carros;
#   2 - Determinar parâmetros simples e relevantes;
#   3 - Analisar dados e especificações;
#   4 - Tomar decisões com base nos dados;

# Módulo datetime para obter o ano atual - Aprendi que é possível invocar o "datetime" inteiro ou apenas parte dele. Vou usar o ano para analisar recolhimentos de impostos.
from datetime import datetime

ano_atual = datetime.now().year
print(ano_atual)

# A intenção de declarar "Carro" no singular nesse momento foi para facilitar a escrita do código quando for necessário acessar um único carro.
# Aprendi que para declarar uma lista é necessário utilizar o sinal de igual e abrir um colchete seguido de uma chave.
Carro = [
    {
        "fabricante": "Renault",
        "modelo": "Clio",
        "tipo": "Sedan",
        "ano": 2003,
        "kilometragem": 150000,
        "valor": 12000,
        "manutencao": "Barata",
    },
    {
        "fabricante": "Ford",
        "modelo": "EcoSport",
        "tipo": "Utilitário",
        "ano": ano_atual - 20,
        "kilometragem": 120000,
        "valor": 40000,
        "manutencao": "Regular",
    },
    {
        "fabricante": "Citroen",
        "modelo": "DS3",
        "tipo": "Hatchback",
        "ano": 2012,
        "kilometragem": 80000,
        "valor": 52000,
        "manutencao": "Cara",
    },
]


# Definições para tomada de decisão.
kilometragem_ideal = 100000
valor_ideal = 35000
manutencao_ideal = "Regular"

# Apresentação dos Carros
print("------------------------------------------------------------")
print("Carros selecionados para análise, objetivo: Custo-Benefício")
print("------------------------------------------------------------")
print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], Carro[0]["ano"])
print("Tipo:", Carro[0]["tipo"])
print("Kilometragem:", Carro[0]["kilometragem"])
print("Manutenção:", Carro[0]["manutencao"])
print("Valor:", Carro[0]["valor"], "\n")

print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], Carro[1]["ano"])
print("Tipo:", Carro[1]["tipo"])
print("Kilometragem:", Carro[1]["kilometragem"])
print("Manutenção:", Carro[1]["manutencao"])
print("Valor:", Carro[1]["valor"], "\n")

print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], Carro[2]["ano"])
print("Tipo:", Carro[2]["tipo"])
print("Kilometragem:", Carro[2]["kilometragem"])
print("Manutenção:", Carro[2]["manutencao"])
print("Valor:", Carro[2]["valor"], "\n")

# Analise 01 - Valores
print("--------------------------------------------------")
print("01 - Análise por Valor Final (Limite: R$35.000,00)")
print("--------------------------------------------------")
# Opção 1
if Carro[0]["valor"] <= valor_ideal:
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], f"({'+'})")
else:
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"])
print("Tipo:", Carro[0]["tipo"])
print("Valor:", Carro[0]["valor"])
# Analise Opção 1
if Carro[0]["valor"] <= valor_ideal:
    print("Análise: O valor do carro é barato comparado ao orçamento.\n")
else:
    print("Análise: O valor do carro está acima do orçamento.\n")

# Opção 2
if Carro[1]["valor"] <= valor_ideal:
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], f"({'+'})")
else:
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"])
print("Tipo:", Carro[1]["tipo"])
print("Valor:", Carro[1]["valor"])
# Analise Opção 2
if Carro[1]["valor"] <= valor_ideal:
    print("Análise: O valor do carro é barato comparado ao orçamento.\n")
else:
    print("Análise: O valor do carro está acima do orçamento.\n")

# Opção 3
if Carro[2]["valor"] <= valor_ideal:
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], f"({'+'})")
else:
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"])
print("Tipo:", Carro[2]["tipo"])
print("Valor:", Carro[2]["valor"])
# Analise Opção 3
if Carro[2]["valor"] <= valor_ideal:
    print("Análise: O valor do carro é barato comparado ao orçamento.\n")
else:
    print("Análise: O valor do carro está acima do orçamento.\n")

# Análise 02 - Custo de Manutenção
print("---------------------------------------------------------------------")
print("02 - Análise por Custo de Manutenção ao Longo Prazo (Limite: Regular)")
print("---------------------------------------------------------------------")

# Opção 1
if (
    Carro[0]["manutencao"] <= manutencao_ideal
    and Carro[0]["kilometragem"] < kilometragem_ideal
):
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], f"({'+'})")
    print("Kilometragem:", Carro[0]["kilometragem"])
else:
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"])
print("Kilometragem:", Carro[0]["kilometragem"])
# Analise Opção 1
if (
    Carro[0]["manutencao"] <= manutencao_ideal
    and Carro[0]["kilometragem"] < kilometragem_ideal
):
    print("Análise: O custo de manutenção do carro é regular.\n")
else:
    print("Análise: O custo de manutenção do carro é cara.\n")

# Opção 2
if (
    Carro[1]["manutencao"] <= manutencao_ideal
    and Carro[1]["kilometragem"] < kilometragem_ideal
):
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], f"({'+'})")
    print("Kilometragem:", Carro[1]["kilometragem"])
else:
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"])
print("Kilometragem:", Carro[1]["kilometragem"])
# Analise Opção 2
if (
    Carro[1]["manutencao"] <= manutencao_ideal
    and Carro[1]["kilometragem"] < kilometragem_ideal
):
    print("Análise: O custo de manutenção do carro é regular.\n")
else:
    print("Análise: O custo de manutenção do carro é cara.\n")

# Opção 3
if (
    Carro[2]["manutencao"] <= manutencao_ideal
    and Carro[2]["kilometragem"] < kilometragem_ideal
):
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], f"({'+'})")
    print("Kilometragem:", Carro[2]["kilometragem"])
else:
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"])
print("Kilometragem:", Carro[2]["kilometragem"])
# Analise Opção 3
if (
    Carro[2]["manutencao"] <= manutencao_ideal
    and Carro[2]["kilometragem"] < kilometragem_ideal
):
    print("Análise: O custo de manutenção do carro é regular.\n")
else:
    print("Análise: O custo de manutenção do carro é cara.\n")

# Análise 03 - Ano de Fabricação e gastos com impostos (IPVA)
print("------------------------------------------------------------")
print("03 - Análise por Recolhimento de Impostos para o próximo ano")
print("------------------------------------------------------------")

# Opção 1
if Carro[0]["ano"] + 20 < ano_atual:
    print(
        "Opção 1:",
        Carro[0]["fabricante"],
        Carro[0]["modelo"],
        f"({Carro[0]['ano']})",
        f"({'+'})",
    )
    print("Kilometragem:", Carro[0]["kilometragem"])
elif Carro[0]["ano"] + 20 == ano_atual:
    print(
        "Opção 1:",
        Carro[0]["fabricante"],
        Carro[0]["modelo"],
        f"({Carro[0]['ano']})",
        f"({'+'})",
    )
    print("Kilometragem:", Carro[0]["kilometragem"])
else:
    print(
        "Opção 1:",
        Carro[0]["fabricante"],
        Carro[0]["modelo"],
        f"({Carro[0]['ano']})",
    )
    print("Kilometragem:", Carro[0]["kilometragem"])

# Analise Opção 1
if Carro[0]["ano"] + 20 < ano_atual:
    print("Análise: Essa opção não recolhe mais impostos.\n")
elif Carro[0]["ano"] + 20 == ano_atual:
    print("Análise: Essa opção não recolherá impostos no próximo ano.\n")
else:
    print("Análise: Essa opção terá recolhimento previsto para os próximos anos.\n")

# Opção 2
if Carro[1]["ano"] + 20 < ano_atual:
    print(
        "Opção 2:",
        Carro[1]["fabricante"],
        Carro[1]["modelo"],
        f"({Carro[1]['ano']})",
        f"({'+'})",
    )
    print("Kilometragem:", Carro[1]["kilometragem"])
elif Carro[1]["ano"] + 20 == ano_atual:
    print(
        "Opção 2:",
        Carro[1]["fabricante"],
        Carro[1]["modelo"],
        f"({Carro[1]['ano']})",
        f"({'+'})",
    )
    print("Kilometragem:", Carro[1]["kilometragem"])
else:
    print(
        "Opção 1:",
        Carro[0]["fabricante"],
        Carro[0]["modelo"],
        f"({Carro[0]['ano']})",
    )
    print("Kilometragem:", Carro[1]["kilometragem"])

# Analise Opção 2
if Carro[1]["ano"] + 20 < ano_atual:
    print("Análise: Essa opção não recolhe mais impostos.\n")
elif Carro[1]["ano"] + 20 == ano_atual:
    print("Análise: Essa opção não recolherá impostos no próximo ano.\n")
else:
    print("Análise: Essa opção terá recolhimento previsto para os próximos anos.\n")

# Opção 3
if Carro[2]["ano"] + 20 < ano_atual:
    print(
        "Opção 3:",
        Carro[2]["fabricante"],
        Carro[2]["modelo"],
        f"({Carro[2]['ano']})",
        f"({'+'})",
    )
    print("Kilometragem:", Carro[2]["kilometragem"])
elif Carro[2]["ano"] + 20 == ano_atual:
    print(
        "Opção 3:",
        Carro[2]["fabricante"],
        Carro[2]["modelo"],
        f"({Carro[2]['ano']})",
        f"({'+'})",
    )
    print("Kilometragem:", Carro[2]["kilometragem"])
else:
    print(
        "Opção 3:",
        Carro[2]["fabricante"],
        Carro[2]["modelo"],
        f"({Carro[2]['ano']})",
    )
    print("Kilometragem:", Carro[2]["kilometragem"])

# Analise Opção 3
if Carro[2]["ano"] + 20 < ano_atual:
    print("Análise: Essa opção não recolhe mais impostos.\n")
elif Carro[2]["ano"] + 20 == ano_atual:
    print("Análise: Essa opção não recolherá impostos no próximo ano.\n")
else:
    print("Análise: Essa opção terá recolhimento previsto para os próximos anos.\n")

# Análise 04 - Considerações Finais
print("-------------------------------------------")
print("Análise Final por Custo-Benefício (Pontos).")
print("-------------------------------------------")

# Opção 1
print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], Carro[0]["ano"])

# Análise Opção 1
if (
    Carro[0]["valor"] <= valor_ideal
    and Carro[0]["ano"] + 20 < ano_atual
    or Carro[0]["ano"] + 20 == ano_atual
    and Carro[0]["manutencao"] <= manutencao_ideal
    and Carro[0]["kilometragem"] < kilometragem_ideal
):
    print("É a melhor escolha.\n")
else:
    print("Não Compensa.\n")


# Opção 2
print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], Carro[1]["ano"])

# Análise Opção 2
if (
    Carro[1]["valor"] <= valor_ideal
    and Carro[1]["ano"] + 20 < ano_atual
    or Carro[1]["ano"] + 20 == ano_atual
    and Carro[1]["manutencao"] <= manutencao_ideal
    and Carro[1]["kilometragem"] < kilometragem_ideal
):
    print("É a melhor escolha.\n")
else:
    print("Não Compensa.\n")

# Opção 3
print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], Carro[2]["ano"])

# Análise Opção 3
if (
    Carro[2]["valor"] <= valor_ideal
    and Carro[2]["ano"] + 20 < ano_atual
    or Carro[2]["ano"] + 20 == ano_atual
    and Carro[2]["manutencao"] <= manutencao_ideal
    and Carro[2]["kilometragem"] < kilometragem_ideal
):
    print("É a melhor escolha.\n")
else:
    print("Não Compensa.\n")
