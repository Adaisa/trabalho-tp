
from questao07 import *

while True:
    opcao = menu()
    if opcao == 1:
        cadastrarNovela()

    elif opcao == 2:
        mostrarNovela()

    elif opcao == 3:
        deletarNovela()

    elif opcao == 4:
        selecionarPorNome()
    
    elif opcao == 5:
        alterarNovela()
         
    elif opcao == 6:
        break