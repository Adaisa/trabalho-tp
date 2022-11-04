
import json
 

nome_arquivo = "novela.json"

class bcolors:
    VERDE = '\033[92m' #GREEN
    AMARELO = '\033[93m' #YELLOW
    VERMELHO = '\033[91m' #RED
    AZUL =   '\033[94m' #AZUL
    CINZA = '\033[90m' #CINZA
    BARRAVERMELHO = '\033[101m' #BARRA VERMELHO
    BARRAVERDE = '\033[102m' #BARRAVERDE
    BARRAAMARELO = '\033[103m' #BARRA AMARELO
    BARRAAZUL = '\033[104m' #BARRA AZUL
    BARRAROSA = '\033[105m' #BARRA ROSA
    BARRAMARINHO = '\033[106m' #BARRAMARINHO
    END = '\033[0m' #END COLOR
    

def menu():
    
    print(10 * '-=-')
    print(bcolors.BARRAVERDE,'1 - Cadastrar novela', bcolors.END)
    print(bcolors.BARRAAZUL,'2 - Ver novela', bcolors.END)
    print(bcolors.BARRAROSA,'3 - Deletar novela ', bcolors.END)
    print(bcolors.BARRAAMARELO,'4 - Selecionar novela por nome ', bcolors.END)
    print(bcolors.BARRAMARINHO,'5 - Alterar novela ', bcolors.END)
    print(bcolors.BARRAVERMELHO,'6 - Sair', bcolors.END)
    print(10 * '-=-')      
    return int(input('Escolha uma opção: '))
                              

def cadastrarNovela():
    novela2 = lerNovela()
    dicio = {}
    
    dicio['nome'] = str(input("Nome da novela: "))
    dicio['quantAtor'] = int(input("Quantos atores tem a novela ?: "))
    dicio['diretor'] = str(input("Nome do diretor: "))
    dicio['genero'] = str(input("Qual o genero da novela: "))
    dicio['classificacao'] = int(input("Qual a classificação da novela: "))

    novela2.append(dicio)
    print(novela2)
    salvarArquivo(novela2)

def lerNovela() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)


def salvarArquivo(dicio: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(dicio, indent=4)
    arq.write(data)
    arq.close()

def mostrarNovela():
    print(10 * '-#-')
    novela = lerNovela()
    for i in range(len(novela)) :
        print(f'O nome da novela cadastrada é: {novela[i]["nome"]}')
        print(f'A quantidade de atores são: {novela[i]["quantAtor"]}') 
        print(f'O diretor da novela é: {novela[i]["diretor"]}')
        print(f'O gênero da novela é {novela[i]["genero"]}')
        print(f'A classificação é para maiores de: {novela[i]["classificacao"]}')
        print(10 * '-#-')

def deletarNovela():
    a = lerNovela()
    pede = input("Insira o nome da novela: ")
    for i in a:
        if i['nome'] == pede:
            b = a.index(i)
            a.pop(b)
    print(f"{bcolors.VERMELHO}*-*-*-* Apagando a novela selecionada *-*-*-* {bcolors.END}")
    salvarArquivo(a)

def selecionarPorNome():
    chamar = lerNovela()
    pedir_nome = str(input("Insira o nome da novela que deseja selecionar: "))
    for i in chamar:
        if i['nome'] == pedir_nome:
            print(i)
            return "Nome encontrado !"     
    print("Nome inválido !")   

def alterarNovela():
    lista = lerNovela()
    pedir = str(input("Nome da novela: "))
    for i in lista:
        if i["nome"] == pedir:
            a1 = input("Você deseja alterar o nome? (S/N): ")
            if a1 == "S":
                i["nome"] = input("Insira um novo nome: ")
    salvarArquivo(lista)