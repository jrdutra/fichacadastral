import os
from fnmatch import fnmatch
import os.path
import pytesseract as ocr
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from pywinauto import Application

import win32com.client
import win32gui
import win32process
import time

import win32gui
import re

os.system("cls");
pattern = "*.jpg"

# Lê diretorio
arquivo = open('dir.txt', 'r')
root = arquivo.read()
arquivo.close();


# ENTRA NO DIRETORIO E PROCURA POR ARQUIVOS JPG
qt_lida = 0
porcento = 0
nomeprocesso = os.getpid()
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):  # se nome do arquivo do subdir tiver a extensao
            dir = os.path.join(path, name)
            if os.path.isfile(dir+".txt") == 0:  # se nao existir o .txt com texto, cria
                os.system("cls")
                comandoAbrir = "start " + dir
                comandoFechar = "taskkill.exe /IM Microsoft.Photos.exe /F"
                os.system(comandoFechar)
                os.system(comandoAbrir)
                print(dir)
                app = Application().connect(process=int(nomeprocesso))
                app.top_window().set_focus()
                nome = input("NOME>>>")
                img = Image.open(dir)
                draw = ImageDraw.Draw(img)
                texto = nome
                font = ImageFont.truetype("arial-bold.ttf", 36)
                draw.text((50, 50), nome, (0, 0, 0), font=font)
                img.save(dir)



