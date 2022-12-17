from classe import *
from projeto import *

def menu():
    Novela.limparTela()
    print(bcolors.BARRACINZA, "-------- Cadastro de Novela --------", bcolors.END)
    print(bcolors.BARRAVERDE,"1 - Cadastrar Novela", bcolors.END)
    print(bcolors.BARRAROSA,"2 - Editar informações", bcolors.END)
    print(bcolors.BARRAAMARELO,"3 - Excluir Novela", bcolors.END)
    print(bcolors.BARRAMARINHO,"4 - Selecionar Novela", bcolors.END)
    print(bcolors.BARRABRANCO,"5 - Listar Novelas", bcolors.END)
    print(bcolors.BARRAVERMELHO,"6 - Sair", bcolors.END)
    print(bcolors.BARRACINZA,"----------------------------------", bcolors.END)
    opcao = int(input("Digite a opção desejada: "))
    return opcao


while True:
    opcao = menu()

    if opcao == 1:
        novela = Novela.cadastrarNovela()
        criarNovela(novela)
        Novela.exibirMsg("A novela foi cadastrada com sucesso!")
    elif opcao == 2:
        novela = Novela.editarNovela()
        editarNovela(novela)
        Novela.exibirMsg("A novela foi editada com sucesso!")
    elif opcao == 3:
        Novela.limparTela()
        id = Novela.excluirNovela()
        excluirNovela(id)
        Novela.exibirMsg("A novela foi excluída com sucesso!")
    elif opcao == 4:
        id = Novela.selecionarNovela()
        novela = selecionarNovela(id)
        if novela == None:
            Novela.exibirMsg("Novela não encontrada, tente novamente!")
        else:
            Novela.exibirNovela(novela)
            Novela.travarTela()
    elif opcao == 5:
        novela = selecionarTodos()
        Novela.exibirNovelas(novela)
    elif opcao == 6:
        break