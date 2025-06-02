vetor_animal = ["Cachorro", "Gato", "Cobra"]
vetor_trimestre = ["Trimestre 1", "Trimestre 2", "Trimestre 3", "Trimestre 4"]

consultas = [
    [0, 0, 0, 0],  # Cachorro
    [0, 0, 0, 0],  # Gato
    [0, 0, 0, 0]   # Cobra
]

faturamento = [
    [0, 0, 0, 0],  # Cachorro
    [0, 0, 0, 0],  # Gato
    [0, 0, 0, 0]   # Cobra
]

integrantes = ["Gabryel Modesto", "Luiz Lucas", "Luiz Otávio"]

def consultasAnimais():
    try:
        print('Escolha o animal para cadastrar consulta:')
        for i, animal in enumerate(vetor_animal, 1):
            print(f"{i} - {animal}")
        numerosAnimais = int(input())

        if numerosAnimais not in [1, 2, 3]:
            print('Número inválido!')
            return

        print('Informe o número do trimestre (1 a 4):')
        trimestre = int(input())
        if trimestre < 1 or trimestre > 4:
            print("Trimestre inválido!")
            return

        quantidade = int(input('Informe a quantidade de consultas: '))
        if quantidade < 0:
            print("Quantidade não pode ser negativa!")
            return

        consultas[numerosAnimais - 1][trimestre - 1] += quantidade
        print("Consulta cadastrada com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")

def cadastrarFaturamento():
    try:
        print('Escolha o animal para cadastrar faturamento:')
        for i, animal in enumerate(vetor_animal, 1):
            print(f"{i} - {animal}")
        numerosAnimais = int(input())

        if numerosAnimais not in [1, 2, 3]:
            print('Número inválido!')
            return

        print('Informe o número do trimestre (1 a 4):')
        trimestre = int(input())
        if trimestre < 1 or trimestre > 4:
            print("Trimestre inválido!")
            return

        valor = float(input('Informe o valor do faturamento: '))
        if valor < 0:
            print("Valor não pode ser negativo!")
            return

        faturamento[numerosAnimais - 1][trimestre - 1] += valor
        print("Faturamento cadastrado com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")

def exibirConsultas():
    print("\n=== Consultas Cadastradas ===")
    for i, animal in enumerate(vetor_animal):
        print(f"{animal}:")
        for j, trimestre in enumerate(vetor_trimestre):
            print(f"  {trimestre}: {consultas[i][j]} consultas")

def buscarConsultas():
    try:
        print("Escolha o animal:")
        for i, animal in enumerate(vetor_animal, 1):
            print(f"{i} - {animal}")
        animal = int(input("Digite o número do animal: ")) - 1
        if animal < 0 or animal >= len(vetor_animal):
            print("Animal inválido.")
            return

        print("Informe o número do trimestre (1 a 4):")
        trimestre = int(input()) - 1
        if trimestre < 0 or trimestre >= len(vetor_trimestre):
            print("Trimestre inválido")
            return

        qtd_consultas = consultas[animal][trimestre]
        valor_faturado = faturamento[animal][trimestre]

        print("=============================================================")
        print(f'\n{vetor_animal[animal]} - {vetor_trimestre[trimestre]}')
        print(f'Consultas realizadas: {qtd_consultas}')
        print(f'Faturamento: R${valor_faturado:.2f}')
        print("=============================================================")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")

def editarConsultaFaturamento():
    try:
        print("Escolha o animal para atualizar:")
        for i, animal in enumerate(vetor_animal, 1):
            print(f"{i} - {animal}")
        animal = int(input()) - 1
        if animal < 0 or animal >= len(vetor_animal):
            print("Animal inválido.")
            return

        print("Informe o número do trimestre para atualizar (1 a 4):")
        trimestre = int(input()) - 1
        if trimestre < 0 or trimestre >= len(vetor_trimestre):
            print("Trimestre inválido.")
            return

        print("Digite a nova quantidade de consultas:")
        nova_consulta = int(input())
        if nova_consulta < 0:
            print("Quantidade não pode ser negativa.")
            return

        print("Digite o novo valor de faturamento:")
        novo_faturamento = float(input())
        if novo_faturamento < 0:
            print("Valor não pode ser negativo.")
            return

        consultas[animal][trimestre] = nova_consulta
        faturamento[animal][trimestre] = novo_faturamento

        print("Dados atualizados com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")

def relatorioFaturamento():
    print("\n=== Relatório de Faturamento ===")
    for i, animal in enumerate(vetor_animal):
        total = sum(faturamento[i])
        print(f"{animal}: Total faturado no ano: R${total:.2f}")
        for j, trim in enumerate(vetor_trimestre):
            print(f"  {trim}: R${faturamento[i][j]:.2f}")

def mostrarDesenvolvedores():
    print("\n--- Desenvolvedores ---")
    for nome in integrantes:
        print(nome)
    print("----------------------\n")

def menu():
    while True:
        try:
            escolhaNumero = int(input(
                f'\nOlá! Seja bem-vindo(a). Escolha o número que deseja para ajudarmos: \n'
                f'1 - Cadastrar Consulta\n' 
                f'2 - Cadastrar Faturamento\n'
                f'3 - Exibir consultas\n' 
                f'4 - Buscar consultas\n'
                f'5 - Editar Consulta/Faturamento\n'
                f'6 - Relatório de Faturamento\n'
                f'7 - Conheça os Desenvolvedores\n'
                f'8 - Sair\n'
            ))

            match escolhaNumero:
                case 1:
                    consultasAnimais()
                case 2:
                    cadastrarFaturamento()
                case 3:
                    exibirConsultas()
                case 4:
                    buscarConsultas()
                case 5:
                    editarConsultaFaturamento()
                case 6:
                    relatorioFaturamento()
                case 7:
                    mostrarDesenvolvedores()
                case 8:
                    print("Programa encerrado. Até mais!")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    menu()
