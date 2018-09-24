import os
from fnmatch import fnmatch
import os.path
import pytesseract as ocr
from PIL import Image


os.system("cls");
pattern = "*.jpg"

# Lê diretorio
arquivo = open('dir.txt', 'r')
root = arquivo.read()
arquivo.close();


# ENTRA NO DIRETORIO E PROCURA POR ARQUIVOS JPG
qt_lida = 0
porcento = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):  # se nome do arquivo do subdir tiver a extensao
            dir = os.path.join(path, name)
            if os.path.isfile(dir+".txt") == 0:  # se nao existir o .txt com texto, cria
                comandoAbrir = "start " + dir
                comandoFechar = "taskkill.exe /IM Microsoft.Photos.exe /F"
                os.system(comandoFechar)
                os.system(comandoAbrir)
                print(dir)
                os.system("PAUSE");
                os.system("cls");

