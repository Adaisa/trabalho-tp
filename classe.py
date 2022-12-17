import os

class bcolors:
    VERDE = '\033[92m' #GREEN
    AMARELO = '\033[93m' #YELLOW
    VERMELHO = '\033[91m' #RED
    AZUL =   '\033[94m' #AZUL
    CINZA = '\033[90m' #CINZA
    BARRACINZA = '\033[100m' #BARRA CINZA
    BARRAVERMELHO = '\033[101m' #BARRA VERMELHO
    BARRAVERDE = '\033[102m' #BARRA VERDE
    BARRAAMARELO = '\033[103m' #BARRA AMARELO
    BARRAAZUL = '\033[104m' #BARRA AZUL
    BARRAROSA = '\033[105m' #BARRA ROSA
    BARRAMARINHO = '\033[106m' #BARRA MARINHO
    BARRABRANCO = '\033[107m' #BARRA BRANCO
    END = '\033[0m' #END COLOR
    

class Novela:
    def cadastrarNovela():
        Novela.limparTela()
        print(bcolors.BARRAVERDE, "-------- Cadastro de Novelas --------", bcolors.END)
        novela = {}
        novela['nome'] = input('Nome da novela: ')
        novela['atores'] = int(input('Quantidade de atores: '))
        novela['diretor'] = input('Diretor da novela: ')
        novela['genero'] = input('Genero da novela: ')
        novela['classificacao'] = input('Classificacao: ')
        
        return  novela


    def editarNovela():
        Novela.limparTela()
        print(bcolors.BARRABRANCO, "-------- Edição da Novela --------", bcolors.END)
        novela = {}
        novela['id'] = int(input('ID da novela: '))
        novela['nome'] = input('Nome: ')
        novela['atores'] = int(input('Quantidade de atores: '))
        novela['diretor'] = input('Diretor da novela: ')
        novela['genero'] = input('Genero da novela: ')
        novela['classificacao'] = int(input('Classificação da novela: '))
        
        return  novela


    def excluirNovela():
        print(bcolors.BARRAVERMELHO, "-------- Exclusão de Novela --------", bcolors.END)
        Novela.limparTela()
        id = int(input('ID da novela: '))
        return id


    def selecionarNovela():
        Novela.limparTela()
        print(bcolors.BARRACINZA, "-------- Seleção de Novela --------", bcolors.END)
        id = int(input('ID da novela: '))
        return id


    def exibirNovela(novela):
        print(bcolors.BARRAVERDE, "-------- Novelas --------", bcolors.END)
        print(f"ID: {novela['id']}")
        print(f"Nome da novela:    {novela['nome']}")
        print(f"Quantidade de atores:    {novela['atores']}")
        print(f"Diretor da novela:    {novela['diretor']}")
        print(f"Genero da novela:  {novela['genero']}")
        print(f"Classificação da novela:   {novela['classificacao']}")
             
             
    def exibirNovelas(novelas):
        Novela.limparTela()
        print(bcolors.BARRAVERDE, "---------------- Novelas ----------------", bcolors.END)
        for novela in novelas:
            Novela.exibirNovela(novela)
        Novela.travarTela()


    def limparTela():
        os.system('clear' if os.name == 'posix' else 'cls')


    def travarTela():
        input('Pressione ENTER para continuar...')


    def exibirMsg(msg):
        print(msg)
        Novela.travarTela()