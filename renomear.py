import os
from fnmatch import fnmatch
import os.path
import pytesseract as ocr
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


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
                nome = input("NOME>>>")
                img = Image.open(dir)
                draw = ImageDraw.Draw(img)
                texto = nome
                font = ImageFont.truetype("arial-bold.ttf", 36)
                draw.text((50, 50), nome, (0, 0, 0), font=font)
                img.save(dir)
                os.system("PAUSE");
                os.system("cls");

