# Objetivos do Exercício:
# Treinar os conceitos básicos de Python, incluindo estruturas de dados, controle de fluxo e funções.
# Treinar bastante if, elif e else.
# Treinar cálculos e lógica condicional.
# Trinar f-strings para formatação de saída.
# Não usar loops, pois ainda não aprendi a usar eles.
### Criar um programa que analisa dados de carros e toma decisões com base em parâmetros simples e relevantes.
### 1 - Comparar valores de carros;
### 2 - Determinar parâmetros simples e relevantes;
### 3 - Analisar dados e especificações;
### 4 - Tomar decisões com base nos dados;

# Módulo datetime para obter o ano atual - Aprendi que é possível invocar o "datetime" inteiro ou apenas parte dele. Vou usar o ano para analisar recolhimentos de impostos.
from datetime import datetime

ano_atual = datetime.now().year

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
        "manutencao": 1,
    },
    {
        "fabricante": "Ford",
        "modelo": "EcoSport",
        "tipo": "Utilitário",
        "ano": ano_atual - 20,
        "kilometragem": 120000,
        "valor": 40000,
        "manutencao": 2,
    },
    {
        "fabricante": "Citroen",
        "modelo": "DS3",
        "tipo": "Hatchback",
        "ano": 2012,
        "kilometragem": 80000,
        "valor": 52000,
        "manutencao": 3,
    },
]


# Definições para tomada de decisão.
kilometragem_ideal = 100000
valor_ideal = 35000
manutencao_ideal = 1

# Apresentação dos Carros
print("------------------------------------------------------------")
print("Carros selecionados para análise, objetivo: Custo-Benefício")
print("------------------------------------------------------------")
print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], f"({Carro[0]['ano']})")
print("Tipo:", Carro[0]["tipo"])
print(f"Kilometragem: {Carro[0]['kilometragem']:,}km".replace(",", "."))
if Carro[0]["manutencao"] == 1:
    print("Manutenção:", "Barata")
elif Carro[0]["manutencao"] == 2:
    print("Manutenção:", "Regular")
else:
    print("Manutenção:", "Caro")
print(f"Valor: R${Carro[0]['valor']:,}".replace(",", "."), "\n")

print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], f"({Carro[1]['ano']})")
print("Tipo:", Carro[1]["tipo"])
print(f"Kilometragem: {Carro[1]['kilometragem']:,}km".replace(",", "."))
if Carro[1]["manutencao"] == 1:
    print("Manutenção:", "Barata")
elif Carro[1]["manutencao"] == 2:
    print("Manutenção:", "Regular")
else:
    print("Manutenção:", "Caro")
print(f"Valor: R${Carro[1]['valor']:,}".replace(",", "."), "\n")

print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], f"({Carro[2]['ano']})")
print("Tipo:", Carro[2]["tipo"])
print(f"Kilometragem: {Carro[2]['kilometragem']:,}km".replace(",", "."))
if Carro[2]["manutencao"] == 1:
    print("Manutenção:", "Barata")
elif Carro[2]["manutencao"] == 2:
    print("Manutenção:", "Regular")
else:
    print("Manutenção:", "Cara")
print(f"Valor: R${Carro[2]['valor']:,}".replace(",", "."), "\n")

# Analise 01 - Valores
print("--------------------------------------------------")
print("01 - Análise por Valor Final (Limite: R$35.000,00)")
print("--------------------------------------------------")
# Opção 1
if Carro[0]["valor"] <= valor_ideal:
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], f"({'+'})")
    print("Tipo:", Carro[0]["tipo"])
    print(f"Valor: R${Carro[0]['valor']:,}".replace(",", "."))
else:
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"])
    print("Tipo:", Carro[0]["tipo"])
    print(f"Valor: R${Carro[0]['valor']:,}".replace(",", "."))
# Analise Opção 1
if Carro[0]["valor"] <= valor_ideal:
    print("Análise: O valor do carro é barato comparado ao orçamento.\n")
else:
    print("Análise: O valor do carro está acima do orçamento.\n")

# Opção 2
if Carro[1]["valor"] <= valor_ideal:
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], f"({'+'})")
    print("Tipo:", Carro[1]["tipo"])
    print(f"Valor: R${Carro[1]['valor']:,}".replace(",", "."))
else:
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"])
    print("Tipo:", Carro[1]["tipo"])
    print(f"Valor: R${Carro[1]['valor']:,}".replace(",", "."))
# Analise Opção 2
if Carro[1]["valor"] <= valor_ideal:
    print("Análise: O valor do carro é barato comparado ao orçamento.\n")
else:
    print("Análise: O valor do carro está acima do orçamento.\n")

# Opção 3
if Carro[2]["valor"] <= valor_ideal:
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], f"({'+'})")
    print("Tipo:", Carro[2]["tipo"])
    print(f"Valor: R${Carro[2]['valor']:,}".replace(",", "."))
else:
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"])
    print("Tipo:", Carro[2]["tipo"])
    print(f"Valor: R${Carro[2]['valor']:,}".replace(",", "."))
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
) or (
    Carro[0]["ano"] + 20 > ano_atual and Carro[0]["kilometragem"] < kilometragem_ideal
):
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], f"({'+'})")
    print(f"Kilometragem: {Carro[0]['kilometragem']:,}km".replace(",", "."))
else:
    print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"])
    print(f"Kilometragem: {Carro[0]['kilometragem']:,}km".replace(",", "."))
# Analise Opção 1
if (
    Carro[0]["manutencao"] <= manutencao_ideal
    and Carro[0]["kilometragem"] < kilometragem_ideal
) or (
    Carro[0]["ano"] + 20 > ano_atual and Carro[0]["kilometragem"] < kilometragem_ideal
):
    print("Análise: O custo de manutenção do carro é regular.\n")
else:
    print("Análise: O custo de manutenção do carro é cara.\n")

# Opção 2
if (
    Carro[1]["manutencao"] <= manutencao_ideal
    and Carro[1]["kilometragem"] < kilometragem_ideal
) or (
    Carro[1]["ano"] + 20 > ano_atual and Carro[1]["kilometragem"] < kilometragem_ideal
):
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], f"({'+'})")
    print(f"Kilometragem: {Carro[1]['kilometragem']:,}km".replace(",", "."))
else:
    print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"])
    print(f"Kilometragem: {Carro[1]['kilometragem']:,}km".replace(",", "."))
# Analise Opção 2
if (
    Carro[1]["manutencao"] <= manutencao_ideal
    and Carro[1]["kilometragem"] < kilometragem_ideal
) or (
    Carro[1]["ano"] + 20 > ano_atual and Carro[1]["kilometragem"] < kilometragem_ideal
):
    print("Análise: O custo de manutenção do carro é regular.\n")
else:
    print("Análise: O custo de manutenção do carro é cara.\n")

# Opção 3
#
if (
    Carro[2]["manutencao"] <= manutencao_ideal
    and Carro[2]["kilometragem"] < kilometragem_ideal
) or (
    Carro[2]["ano"] + 20 > ano_atual and Carro[2]["kilometragem"] < kilometragem_ideal
):
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], f"({'+'})")
    print(f"Kilometragem: {Carro[2]['kilometragem']:,}km".replace(",", "."))
else:
    print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"])
    print(f"Kilometragem: {Carro[2]['kilometragem']:,}km".replace(",", "."))

# Analise Opção 3
if (
    Carro[2]["manutencao"] <= manutencao_ideal
    and Carro[2]["kilometragem"] < kilometragem_ideal
) or (
    Carro[2]["ano"] + 20 > ano_atual and Carro[2]["kilometragem"] < kilometragem_ideal
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
    print(f"Kilometragem: {Carro[0]['kilometragem']:,}km".replace(",", "."))
elif Carro[0]["ano"] + 20 == ano_atual:
    print(
        "Opção 1:",
        Carro[0]["fabricante"],
        Carro[0]["modelo"],
        f"({Carro[0]['ano']})",
        f"({'+'})",
    )
    print(f"Kilometragem: {Carro[0]['kilometragem']:,}km".replace(",", "."))
else:
    print(
        "Opção 1:",
        Carro[0]["fabricante"],
        Carro[0]["modelo"],
        f"({Carro[0]['ano']})",
    )
    print(f"Kilometragem: {Carro[0]['kilometragem']:,}km".replace(",", "."))

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
    print(f"Kilometragem: {Carro[1]['kilometragem']:,}km".replace(",", "."))
elif Carro[1]["ano"] + 20 == ano_atual:
    print(
        "Opção 2:",
        Carro[1]["fabricante"],
        Carro[1]["modelo"],
        f"({Carro[1]['ano']})",
        f"({'+'})",
    )
    print(f"Kilometragem: {Carro[1]['kilometragem']:,}km".replace(",", "."))
else:
    print(
        "Opção 2:",
        Carro[1]["fabricante"],
        Carro[1]["modelo"],
        f"({Carro[1]['ano']})",
    )
    print(f"Kilometragem: {Carro[1]['kilometragem']:,}km".replace(",", "."))

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
    print(f"Kilometragem: {Carro[2]['kilometragem']:,}km".replace(",", "."))
elif Carro[2]["ano"] + 20 == ano_atual:
    print(
        "Opção 3:",
        Carro[2]["fabricante"],
        Carro[2]["modelo"],
        f"({Carro[2]['ano']})",
        f"({'+'})",
    )
    print(f"Kilometragem: {Carro[2]['kilometragem']:,}km".replace(",", "."))
else:
    print(
        "Opção 3:",
        Carro[2]["fabricante"],
        Carro[2]["modelo"],
        f"({Carro[2]['ano']})",
    )
    print(f"Kilometragem: {Carro[2]['kilometragem']:,}km".replace(",", "."))

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
print("Opção 1:", Carro[0]["fabricante"], Carro[0]["modelo"], f"({Carro[0]['ano']})")

# Análise Opção 1
if (Carro[0]["valor"] <= valor_ideal and Carro[0]["ano"] + 20 < ano_atual) or (
    Carro[0]["ano"] + 20 >= ano_atual
    and Carro[0]["manutencao"] <= manutencao_ideal
    and Carro[0]["kilometragem"] < kilometragem_ideal
):
    print("É a melhor escolha.\n")
else:
    print("Não Compensa.\n")


# Opção 2
print("Opção 2:", Carro[1]["fabricante"], Carro[1]["modelo"], f"({Carro[1]['ano']})")

# Análise Opção 2
if (Carro[1]["valor"] <= valor_ideal and Carro[1]["ano"] + 20 < ano_atual) or (
    Carro[1]["ano"] + 20 >= ano_atual
    and Carro[1]["manutencao"] <= manutencao_ideal
    and Carro[1]["kilometragem"] < kilometragem_ideal
):
    print("É a melhor escolha.\n")
else:
    print("Não Compensa.\n")

# Opção 3
print("Opção 3:", Carro[2]["fabricante"], Carro[2]["modelo"], f"({Carro[2]['ano']})")

# Análise Opção 3
if (Carro[2]["valor"] <= valor_ideal and Carro[2]["ano"] + 20 < ano_atual) or (
    Carro[2]["ano"] + 20 >= ano_atual
    and Carro[2]["manutencao"] <= manutencao_ideal
    and Carro[2]["kilometragem"] < kilometragem_ideal
):
    print("É a melhor escolha.\n")
else:
    print("Não Compensa.\n")
