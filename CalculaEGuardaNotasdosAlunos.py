import json

ARQUIVO = "alunos.json"

def carregar_dados():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(alunos):
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)
        
alunos = carregar_dados()

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    
    notas = []
    
    for i in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1} do aluno: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
                
    aluno =  {
        "nome": nome,
        "notas": notas
    }
    
    alunos.append(aluno)
    salvar_dados(alunos)
    print(f"aluno {nome} adicionado e salvo no arquivo com sucesso!")
    
def calcular_media(notas):
    return sum(notas) / len(notas)

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        status = "Aprovado" if media >= 7 else "Reprovado"
        
        print(f"Nome: {aluno['nome']}") 
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {media:.2f}, Status: {status}")
        print(f"status: {status}")
        print("-" * 30)
        
def menu():
    while True:
        print("-" * 30) 
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Sair")
        print("-" * 30)
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar_aluno()
        elif escolha == "2":
            listar_alunos()
        elif escolha == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
menu()