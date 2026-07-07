# Existem alguns comandos que eu quero usar no 'Comparador de Carros' para reforçar o aprendizado sobre Loops.

# 1 - '=='(Sinal de igualdade duplo)
# Um = sozinho 'serve para guardar um valor' (ex: valor_ideal = 35000).
# Dois == servem para perguntar 'se é igual' (ex: if Carro[0]["manutencao"] == 1:).

# 2 - 'Len' (O que é?)
# A palavra 'len' vem de 'length' (comprimento/tamanho em inglês).
# É uma função do Python que apenas 'conta quantos itens existem dentro de uma lista'.False

# 3 - 'Índice' (O que é?)
# O índice é apenas o número da posição de um item dentro da lista.
# Na programação, a contagem sempre começa do 0.

# Desafio: Reescrever o índice de carros do projeto 'Comparador de Carros'.

# Usando um loop while para percorrer a lista de carros. Apenas para entender a lógica.
# carros = ["Clio", "EcoSport", "DS3"]

# contador = 0
# while contador < 3:
#     print(carros[contador])
#     contador = contador + 1

# Módulo datetime para obter o ano atual - Aprendi que é possível invocar o "datetime" inteiro ou apenas parte dele. Vou usar o ano para analisar recolhimentos de impostos.
from datetime import datetime

ano_atual = datetime.now().year

# Agora vou reproduzir a apresentação dos carros, conforme o projeto original.
carros = [
    {
        "fabricante": "Renault",
        "modelo": "Clio",
        "tipo": "Sedan",
        "ano": 2003,
        "kilometragem": 150000,
        "valor": 12000,
        "manutencao": 1,git
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

# Apresentação dos carros.
print("------------------------------------------------------------")
print("Carros selecionados para análise, objetivo: Custo-Benefício")
print("------------------------------------------------------------")

# Motor Loop & Criando uma variável de apoio.
contador = 0
while contador < 3:
    carro_atual = carros[contador]

    # Legenda dos níveis de manutenção.
    if carro_atual["manutencao"] == 1:
        nivel_manutencao = "Básico"
    elif carro_atual["manutencao"] == 2:
        nivel_manutencao = "Regular"
    else:
        nivel_manutencao = "Avançado"

    print(
        f"Opção {contador + 1}: {carro_atual['fabricante']} {carro_atual['modelo']} {carro_atual['ano']}"
    )
    print(f"Tipo: {carro_atual['tipo']}")
    print(f"Kilometragem: {carro_atual['kilometragem']:,}km".replace(",", "."))
    print(f"Manutenção: {nivel_manutencao}")
    print(f"Valor: R${carro_atual['valor']:,}".replace(",", ".") + ",00", "\n")
    contador = contador + 1
