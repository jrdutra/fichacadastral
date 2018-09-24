import os
from fnmatch import fnmatch
import os.path
import pytesseract as ocr
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


os.system("cls");
pattern = "*.jpg"
nome = input("NOME DA SEQUENCIA>>>")

# Lê diretorio
arquivo = open('dir.txt', 'r')
root = arquivo.read()
arquivo.close();


# ENTRA NO DIRETORIO E PROCURA POR ARQUIVOS JPG
qt_lida = 0
porcento = 0
i = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):  # se nome do arquivo do subdir tiver a extensao
            dir = os.path.join(path, name)
            if os.path.isfile(dir+".txt") == 0:  # se nao existir o .txt com texto, cria
                i += 1
                comando = "ren \"" + dir + "\" " + str(nome) + str(i) + ".jpg"
                os.system(comando)
                print(comando)

