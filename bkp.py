import os
from pathlib import Path
import shutil

def backup(origem, destino, pao=''):
    
    caminho_origem = Path().joinpath(origem, pao)
    caminho_destino = Path().joinpath(destino, pao)
    
    if not caminho_origem.is_dir():
        return
    arquivos = caminho_origem.iterdir()
    for arquivo in arquivos:
        if not caminho_destino.exists():
            caminho_destino.mkdir()
            if not caminho_destino.joinpath(arquivo.name).exists():
                if arquivo.is_file():
                    shutil.copy2(arquivo, caminho_destino.joinpath(arquivo.name))            
        else:
            if arquivo.is_file():
                if not caminho_destino.joinpath(arquivo.name).exists():
                    shutil.copy2(arquivo, caminho_destino.joinpath(arquivo.name))
                else:
                    arq_org = arquivo.stat().st_mtime
                    arq_dst = caminho_destino.joinpath(arquivo.name).stat().st_mtime
                    if arq_org > arq_dst:
                        shutil.copy2(arquivo, caminho_destino.joinpath(arquivo.name))
            
        backup(caminho_origem, caminho_destino, arquivo.name)

        
origem = r''
destino = r''

backup(origem, destino)
