from json_storage import *
from classe import *

def criarNovela(novela: dict) -> dict:
    novelas = lerJson()
    novela['id'] = gerarId()
    novelas.append(novela)
    gravarJson(novelas)


def editarNovela(novela: dict) -> None:
    novelas = lerJson()
    for i, data in enumerate(novelas):
        if data['id'] == novela['id']:
            novelas[i] = novela
            
    gravarJson(novelas)


def excluirNovela(id: int) -> None:
    novelas = lerJson()
    for novela in novelas:
        if novela['id'] == id:
            novelas.remove(novela)
            
    gravarJson(novelas)


def selecionarNovela(id: int) -> dict | None:
    novelas = lerJson()
    for novela in novelas:
        if novela['id'] == id:
            return novela
    return None


def selecionarTodos() -> list:
    return lerJson()

def gerarId() -> int:
    novelas = lerJson()
    if len(novelas) == 0:
        return 1
    return novelas[-1]['id'] + 1