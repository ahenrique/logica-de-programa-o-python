from ftplib import FTP
import os

ftp = FTP('')#caminho do FTP
ftp.login(user='', passwd='')#usuario e senha

ftp.cwd(r'/zisell/arquivo')#pasta do FTP


def downloadFile():
    
    filename = ftp.nlst()#lista todos os arquivos do FTP.

    for file in filename:

        if file.endswith('.TXT'):

            #Abre o arquivo no modo escrita e binario
            with open(file, 'wb') as localfile:

                ftp.retrbinary('RETR ' + file, localfile.write, 1024)# Transfere o arquivo

    ftp.quit()#Fecha conexão com o FTP.


def upload(ftp, file):

    os.chdir(r'')#altera o caminho da pasta onde contem os arquivos
    
    ext = os.path.splitext(file)[1]
  
    
    if ext in (".txt", ".TXT"):
        
        ftp.storlines("STOR " + file, open(file,"rb"))
        
        print("Arquivo " + file + " enviado!!!")
        
        ftp.close()
        
        return True
        
    else:

        #ftp.storbinary("STOR " + file, open(file, "rb"), 10240)
        
        print("Arquivo inexistente ou Inválido!!!")
        
        ftp.close()
        
        return False

for raiz, diretorios, arquivos in os.walk(r''):#altera o caminho da pasta onde contem os arquivos

    for arquivo in arquivos:
        
        ftp = ftplib.FTP('')
        ftp.login("")#Usuario e senha
        ftp.cwd ('')#mudar para um diretório específico
        if arquivo.endswith(('.txt', '.TXT')):

            if upload(ftp, arquivo):
                os.remove(os.path.join(raiz,arquivo))
