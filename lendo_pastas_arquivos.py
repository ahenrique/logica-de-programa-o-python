import os

def escanear_pasta(pasta_inicial, pasta='', nivel=0):

    caminho = os.path.join(pasta_inicial, pasta)
    if not os.path.isdir(caminho):
        return

    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        print('\t'*nivel, '>>' if not os.path.isfile(os.path.join(caminho,arquivo)) else '>', arquivo)
        escanear_pasta(caminho, arquivo, nivel+1)

        
path = r''

escanear_pasta(path)

