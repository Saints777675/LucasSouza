import os
import time

# Base de dados simulada de lojas comerciais e funcionários
usuarios = {
    "admin": {
        "senha": "123",
        "nome": "Carlos Eduardo",
        "cargo": "Gerente Geral",
        "loja": "Loja 01 - Matriz (Centro)"
    },
    "vendedor1": {
        "senha": "abc",
        "nome": "Mariana Souza",
        "cargo": "Operador de Caixa / Vendas",
        "loja": "Loja 02 - Shopping Sul"
    }
}

lojas_disponiveis = [
    "Loja 01 - Matriz (Centro)",
    "Loja 02 - Shopping Sul",
    "Loja 03 - Boulevard Norte"
]


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione [Enter] para continuar...")


def cabecalho(titulo):
    limpar_tela()
    print("=" * 50)
    print(f"{titulo.center(50)}")
    print("=" * 50)
    print()


def menu_principal():
    while True:
        cabecalho("SISTEMA COMERCIAL - REDE DE LOJAS")
        print("1. Fazer Login")
        print("2. Cadastrar Novo Colaborador")
        print("3. Ver Lojas da Rede")
        print("4. Encerrar Sistema")
        print()

        opcao = input("Escolha uma opção (1-4): ").strip()

        match opcao:
            case "1":
                fazer_login()
            case "2":
                cadastrar_usuario()
            case "3":
                listar_lojas()
            case "4":
                cabecalho("ENCERRANDO SISTEMA")
                print("Obrigado por utilizar o sistema comercial. Até logo!")
                break
            case _:
                print("\n[!] Opção inválida. Tente novamente.")
                pausar()


def fazer_login():
    cabecalho("LOGIN DE ACESSO")
    tentativas = 3

    while tentativas > 0:
        login = input("Usuário / Matrícula: ").strip().lower()
        senha = input("Senha: ").strip()

        if login in usuarios and usuarios[login]["senha"] == senha:
            colaborador = usuarios[login]
            print("\n[✓] Autenticação realizada com sucesso!")
            print(f"Bem-vindo(a), {colaborador['nome']}!")
            time.sleep(1.5)
            painel_loja(login, colaborador)
            return
        else:
            tentativas -= 1
            print(f"\n[X] Usuário ou senha incorretos!")
            if tentativas > 0:
                print(f"Você ainda tem {tentativas} tentativa(s).\n")
            else:
                print("\n[!] Limite de tentativas atingido. Acesso bloqueado temporariamente.")
                pausar()


def cadastrar_usuario():
    cabecalho("CADASTRO DE NOVO COLABORADOR")
    
    usuario = input("Digite o nome de usuário (login): ").strip().lower()
    if not usuario:
        print("\n[!] Usuário não pode ser vazio.")
        pausar()
        return

    if usuario in usuarios:
        print("\n[!] Este usuário já existe no sistema.")
        pausar()
        return

    senha = input("Crie uma senha: ").strip()
    if not senha:
        print("\n[!] A senha não pode ser vazia.")
        pausar()
        return

    nome = input("Nome completo do colaborador: ").strip()

    print("\nCargos disponíveis:")
    print("1. Vendedor / Caixa")
    print("2. Supervisor de Estoque")
    print("3. Gerente de Loja")
    cargo_opcao = input("Escolha o cargo (1-3): ").strip()

    cargos = {
        "1": "Vendedor / Caixa",
        "2": "Supervisor de Estoque",
        "3": "Gerente de Loja"
    }
    cargo = cargos.get(cargo_opcao, "Vendedor / Caixa")

    print("\nEscolha a unidade da loja:")
    for indice, loja in enumerate(lojas_disponiveis, start=1):
        print(f"{indice}. {loja}")
    
    try:
        loja_escolha = int(input(f"Selecione a loja (1-{len(lojas_disponiveis)}): "))
        if 1 <= loja_escolha <= len(lojas_disponiveis):
            loja_selecionada = lojas_disponiveis[loja_escolha - 1]
        else:
            loja_selecionada = lojas_disponiveis[0]
    except ValueError:
        loja_selecionada = lojas_disponiveis[0]

    usuarios[usuario] = {
        "senha": senha,
        "nome": nome if nome else usuario.capitalize(),
        "cargo": cargo,
        "loja": loja_selecionada
    }

    print(f"\n[✓] Colaborador '{usuario}' cadastrado com sucesso na {loja_selecionada}!")
    pausar()


def listar_lojas():
    cabecalho("UNIDADES DA REDE COMERCIAL")
    for i, loja in enumerate(lojas_disponiveis, start=1):
        # Contagem de colaboradores alocados nesta unidade
        colaboradores = [u["nome"] for u in usuarios.values() if u["loja"] == loja]
        print(f"{i}. {loja}")
        print(f"   Equipe cadastrada: {len(colaboradores)} colaborador(es)")
        if colaboradores:
            print(f"   Membros: {', '.join(colaboradores)}")
        print("-" * 40)
    pausar()


def painel_loja(usuario, dados):
    while True:
        cabecalho(f"PAINEL DA UNIDADE: {dados['loja']}")
        print(f"Colaborador: {dados['nome']} | Cargo: {dados['cargo']}\n")
        print("1. Consultar Dados do Perfil")
        print("2. Registrar Venda (PDV Rápido)")
        print("3. Relatório Gerencial (Apenas Gerência)")
        print("4. Fazer Logout")
        print()

        opcao = input("Opção: ").strip()

        match opcao:
            case "1":
                cabecalho("MEU PERFIL")
                print(f"Nome:    {dados['nome']}")
                print(f"Login:   {usuario}")
                print(f"Cargo:   {dados['cargo']}")
                print(f"Unidade: {dados['loja']}")
                pausar()
            case "2":
                cabecalho("REGISTRO DE VENDA")
                try:
                    valor = float(input("Digite o valor da venda (R$): "))
                    print(f"\n[✓] Venda de R$ {valor:.2f} registrada com sucesso na unidade {dados['loja']}!")
                except ValueError:
                    print("\n[!] Valor inválido digitado.")
                pausar()
            case "3":
                cabecalho("RELATÓRIO GERENCIAL")
                if "Gerente" in dados["cargo"]:
                    print("Status da Rede: Todas as lojas operando normalmente.")
                    print(f"Total de colaboradores no sistema: {len(usuarios)}")
                    print(f"Total de lojas cadastradas: {len(lojas_disponiveis)}")
                else:
                    print("[!] Acesso negado: Este recurso requer perfil de Gerente.")
                pausar()
            case "4":
                print("\nFazendo logout...")
                time.sleep(1)
                break
            case _:
                print("\n[!] Opção inválida.")
                pausar()


if __name__ == "__main__":
    menu_principal()

