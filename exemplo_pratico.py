import numpy as np


def main():
    # PRODUTOS:
    # Linha 1 = Trufa Tradicional
    # Linha 2 = Barra 70%

    # COLUNAS:
    # Coluna 1 = Dia 1
    # Coluna 2 = Dia 2
    # Coluna 3 = Dia 3

    # --- DADOS INICIAIS ---

    vendas_manha = np.array([
        [10, 12, 15],
        [6, 8, 10]
    ])

    vendas_tarde = np.array([
        [2, 1, 0],
        [1, 2, 1]
    ])

    devolucoes = np.array([
        [1, 0, 2],
        [0, 1, 0]
    ])

    # Preços dos produtos
    # Trufa = R$ 15,00
    # Barra 70% = R$ 25,00

    precos = np.array([
        [15],
        [25]
    ])

    # --- 1. SOMA DE MATRIZES ---

    # Soma as vendas da manhã com as vendas da tarde.
    # As duas matrizes possuem a mesma dimensão (2x3).

    total_vendas = vendas_manha + vendas_tarde

    # --- 2. SUBTRAÇÃO DE MATRIZES ---

    # Subtrai as devoluções do total de vendas.
    # Assim descobrimos quantos produtos realmente foram vendidos.

    vendas_liquidas = total_vendas - devolucoes

    # --- 3. MULTIPLICAÇÃO POR ESCALAR ---

    # Aplicamos um reajuste de 20% nos preços.
    # 100% + 20% = 120% = 1.2

    fator_reajuste = 1.2

    precos_reajustados = precos * fator_reajuste

    # --- 4. MULTIPLICAÇÃO DE MATRIZES ---

    # Multiplicamos os preços (2x1) pela quantidade vendida (2x3).
    # Para isso, precisamos transpor a matriz de preços:
    # (1x2) @ (2x3) = (1x3).

    faturamento_diario = precos_reajustados.T @ vendas_liquidas

    # --- RESULTADOS ---

    print("=" * 56)
    print("RELATÓRIO DE VENDAS".center(56))
    print("=" * 56)

    # 1. Total de vendas
    print("\n1. TOTAL DE VENDAS (manhã + tarde)")
    print("-" * 56)
    print(f"{'Produto':<20}{'Dia 1':>10}{'Dia 2':>10}{'Dia 3':>10}")
    print(f"{'Trufa Tradicional':<20}{total_vendas[0][0]:>10}{total_vendas[0][1]:>10}{total_vendas[0][2]:>10}")
    print(f"{'Barra 70%':<20}{total_vendas[1][0]:>10}{total_vendas[1][1]:>10}{total_vendas[1][2]:>10}")

    # 2. Vendas líquidas
    print("\n2. VENDAS LÍQUIDAS (total - devoluções)")
    print("-" * 56)
    print(f"{'Produto':<20}{'Dia 1':>10}{'Dia 2':>10}{'Dia 3':>10}")
    print(f"{'Trufa Tradicional':<20}{vendas_liquidas[0][0]:>10}{vendas_liquidas[0][1]:>10}{vendas_liquidas[0][2]:>10}")
    print(f"{'Barra 70%':<20}{vendas_liquidas[1][0]:>10}{vendas_liquidas[1][1]:>10}{vendas_liquidas[1][2]:>10}")

    # 3. Preços reajustados
    print("\n3. PREÇOS REAJUSTADOS (+20%)")
    print("-" * 56)
    print(f"{'Produto':<20}{'Preço antigo':>18}{'Preço novo':>18}")
    print(f"{'Trufa Tradicional':<20}{'R$ ' + format(precos[0][0], '.2f'):>18}{'R$ ' + format(precos_reajustados[0][0], '.2f'):>18}")
    print(f"{'Barra 70%':<20}{'R$ ' + format(precos[1][0], '.2f'):>18}{'R$ ' + format(precos_reajustados[1][0], '.2f'):>18}")

    # 4. Faturamento por dia
    print("\n4. FATURAMENTO POR DIA")
    print("-" * 56)
    print(f"{'':<20}{'Dia 1':>12}{'Dia 2':>12}{'Dia 3':>12}")
    print(f"{'Faturamento':<20}"
          f"{'R$ ' + format(faturamento_diario[0][0], '.2f'):>12}"
          f"{'R$ ' + format(faturamento_diario[0][1], '.2f'):>12}"
          f"{'R$ ' + format(faturamento_diario[0][2], '.2f'):>12}")

    print("\n" + "=" * 56)
    print(f"FATURAMENTO TOTAL: R$ {faturamento_diario.sum():.2f}".center(56))
    print("=" * 56)


if __name__ == "__main__":
    main()