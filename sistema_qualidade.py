# ============================================================
# Sistema de Gestão de Peças, Qualidade e Armazenamento
# Desafio de Automação Digital - UniFECAF
# Disciplina: Algoritmos e Lógica de Programação
# ============================================================

# --- Estruturas de dados (listas que guardam tudo) ---
pecas_aprovadas = []    # Lista de peças aprovadas
pecas_reprovadas = []   # Lista de peças reprovadas (com motivo)
caixas_fechadas = []    # Lista de caixas que já foram fechadas
caixa_atual = []        # Caixa aberta recebendo peças (máx 10)

CAPACIDADE_CAIXA = 10  # Constante: limite de peças por caixa


# --- Funções auxiliares ---

def validar_peso(peso):
    """Verifica se o peso está entre 95g e 105g."""
    return 95 <= peso <= 105


def validar_cor(cor):
    """Verifica se a cor é azul ou verde."""
    return cor.lower() in ["azul", "verde"]


def validar_comprimento(comprimento):
    """Verifica se o comprimento está entre 10cm e 20cm."""
    return 10 <= comprimento <= 20


def avaliar_qualidade(peso, cor, comprimento):
    """
    Avalia a peça com base nos 3 critérios.
    Retorna uma tupla: (aprovada: bool, motivos: list)
    """
    motivos = []

    if not validar_peso(peso):
        motivos.append(f"Peso fora do padrão ({peso}g - esperado: 95g a 105g)")

    if not validar_cor(cor):
        motivos.append(f"Cor inválida ({cor} - esperado: azul ou verde)")

    if not validar_comprimento(comprimento):
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm - esperado: 10cm a 20cm)")

    aprovada = len(motivos) == 0
    return aprovada, motivos


def armazenar_na_caixa(peca):
    """
    Coloca a peça aprovada na caixa atual.
    Se a caixa atingir 10 peças, fecha ela e abre uma nova.
    """
    global caixa_atual

    caixa_atual.append(peca)
    print(f"   ✅ Peça adicionada à caixa atual ({len(caixa_atual)}/{CAPACIDADE_CAIXA})")

    if len(caixa_atual) >= CAPACIDADE_CAIXA:
        numero_caixa = len(caixas_fechadas) + 1
        caixas_fechadas.append({
            "numero": numero_caixa,
            "pecas": list(caixa_atual)  # copia a lista
        })
        caixa_atual = []  # abre nova caixa vazia
        print(f"   📦 Caixa {numero_caixa} FECHADA! Nova caixa aberta.")


def buscar_peca_por_id(id_peca):
    """Procura uma peça pelo ID nas listas de aprovadas e reprovadas."""
    for i, peca in enumerate(pecas_aprovadas):
        if peca["id"] == id_peca:
            return "aprovada", i
    for i, peca in enumerate(pecas_reprovadas):
        if peca["id"] == id_peca:
            return "reprovada", i
    return None, -1


# --- Funções do menu ---

def cadastrar_peca():
    """Opção 1: Cadastrar nova peça com entrada do usuário."""
    print("\n--- CADASTRAR NOVA PEÇA ---")

    id_peca = input("   ID da peça: ").strip()

    # Verifica se o ID já existe
    status, _ = buscar_peca_por_id(id_peca)
    if status is not None:
        print(f"   ⚠️  Já existe uma peça com o ID '{id_peca}'.")
        return

    # Lê o peso (com tratamento de erro)
    try:
        peso = float(input("   Peso (g): "))
    except ValueError:
        print("   ⚠️  Peso inválido. Digite um número.")
        return

    cor = input("   Cor: ").strip()

    try:
        comprimento = float(input("   Comprimento (cm): "))
    except ValueError:
        print("   ⚠️  Comprimento inválido. Digite um número.")
        return

    # Avalia a qualidade
    aprovada, motivos = avaliar_qualidade(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if aprovada:
        pecas_aprovadas.append(peca)
        print(f"\n   ✅ Peça '{id_peca}' APROVADA!")
        armazenar_na_caixa(peca)
    else:
        peca["motivos"] = motivos
        pecas_reprovadas.append(peca)
        print(f"\n   ❌ Peça '{id_peca}' REPROVADA!")
        for motivo in motivos:
            print(f"      - {motivo}")


def listar_pecas():
    """Opção 2: Listar peças aprovadas e reprovadas."""
    print("\n--- PEÇAS APROVADAS ---")
    if not pecas_aprovadas:
        print("   Nenhuma peça aprovada.")
    else:
        for peca in pecas_aprovadas:
            print(f"   ID: {peca['id']} | Peso: {peca['peso']}g | "
                  f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")

    print("\n--- PEÇAS REPROVADAS ---")
    if not pecas_reprovadas:
        print("   Nenhuma peça reprovada.")
    else:
        for peca in pecas_reprovadas:
            print(f"   ID: {peca['id']} | Peso: {peca['peso']}g | "
                  f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
            for motivo in peca["motivos"]:
                print(f"      ↳ {motivo}")


def remover_peca():
    """Opção 3: Remover uma peça pelo ID."""
    print("\n--- REMOVER PEÇA ---")
    id_peca = input("   ID da peça a remover: ").strip()

    status, indice = buscar_peca_por_id(id_peca)

    if status is None:
        print(f"   ⚠️  Peça '{id_peca}' não encontrada.")
        return

    if status == "aprovada":
        pecas_aprovadas.pop(indice)
        # Remove também da caixa atual, se estiver lá
        for i, p in enumerate(caixa_atual):
            if p["id"] == id_peca:
                caixa_atual.pop(i)
                break
        print(f"   🗑️  Peça aprovada '{id_peca}' removida com sucesso.")
    else:
        pecas_reprovadas.pop(indice)
        print(f"   🗑️  Peça reprovada '{id_peca}' removida com sucesso.")


def listar_caixas():
    """Opção 4: Listar todas as caixas fechadas."""
    print("\n--- CAIXAS FECHADAS ---")
    if not caixas_fechadas:
        print("   Nenhuma caixa fechada ainda.")
    else:
        for caixa in caixas_fechadas:
            ids = [p["id"] for p in caixa["pecas"]]
            print(f"   📦 Caixa {caixa['numero']}: {len(caixa['pecas'])} peças → {ids}")

    # Mostra a caixa atual também
    if caixa_atual:
        ids_atual = [p["id"] for p in caixa_atual]
        print(f"\n   📂 Caixa atual (aberta): {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças → {ids_atual}")
    else:
        print(f"\n   📂 Caixa atual (aberta): vazia")


def gerar_relatorio():
    """Opção 5: Gerar relatório final consolidado."""
    print("\n" + "=" * 55)
    print("        RELATÓRIO FINAL DE PRODUÇÃO")
    print("=" * 55)

    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_pecas = total_aprovadas + total_reprovadas

    # Conta caixas (fechadas + a atual se tiver peças)
    total_caixas = len(caixas_fechadas)
    if caixa_atual:
        total_caixas += 1  # conta a caixa aberta também

    print(f"\n   Total de peças cadastradas: {total_pecas}")
    print(f"   ✅ Aprovadas: {total_aprovadas}")
    print(f"   ❌ Reprovadas: {total_reprovadas}")
    print(f"\n   📦 Caixas fechadas: {len(caixas_fechadas)}")
    print(f"   📂 Caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças")
    print(f"   📊 Total de caixas utilizadas: {total_caixas}")

    if pecas_reprovadas:
        print("\n   --- Detalhamento das Reprovações ---")
        for peca in pecas_reprovadas:
            print(f"   Peça {peca['id']}:")
            for motivo in peca["motivos"]:
                print(f"      - {motivo}")

    print("\n" + "=" * 55)


# --- Menu principal ---

def menu():
    """Loop principal do menu interativo."""
    while True:
        print("\n╔══════════════════════════════════════════╗")
        print("║   SISTEMA DE CONTROLE DE QUALIDADE       ║")
        print("║   Gestão de Peças e Armazenamento        ║")
        print("╠══════════════════════════════════════════╣")
        print("║  1. Cadastrar nova peça                  ║")
        print("║  2. Listar peças aprovadas/reprovadas    ║")
        print("║  3. Remover peça cadastrada              ║")
        print("║  4. Listar caixas fechadas               ║")
        print("║  5. Gerar relatório final                ║")
        print("║  0. Sair                                 ║")
        print("╚══════════════════════════════════════════╝")

        opcao = input("\n   Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\n   👋 Encerrando o sistema. Até logo!")
            break
        else:
            print("\n   ⚠️  Opção inválida. Tente novamente.")


# --- Ponto de entrada do programa ---
if __name__ == "__main__":
    menu()
