import os
from pathlib import Path

def escanear_pasta_os(pasta_inicial, pasta='', nivel=0):

    caminho = os.path.join(pasta_inicial, pasta)
    if not os.path.isdir(caminho):
        return

    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        print('\t'*nivel, '>>' if not os.path.isfile(os.path.join(caminho,arquivo)) else '>', arquivo)
        escanear_pasta_os(caminho, arquivo, nivel+1)


def escanear_pasta_path(pasta_inicial, pasta='', nivel=0):    
    caminho = Path().joinpath(pasta_inicial, pasta)
    if not caminho.is_dir():
        return
    arquivos = caminho.iterdir()
    for arquivo in arquivos:
        print('\t' * nivel, '>>' if not arquivo.is_file() else '>', arquivo.name)
        escanear_pasta_path(caminho, arquivo.name, nivel + 1)
        

        
path = r''

escanear_pasta_path(path)

