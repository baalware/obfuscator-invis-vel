import os
import logging
from pystyle import *
import colorama
from pystyle import Box
from pystyle import Colors, Colorate

baalware = """

██████╗  █████╗  █████╗ ██╗     ██╗    ██╗ █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║     ██║    ██║██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║███████║██║     ██║ █╗ ██║███████║██████╔╝█████╗  
██╔══██╗██╔══██║██╔══██║██║     ██║███╗██║██╔══██║██╔══██╗██╔══╝  
██████╔╝██║  ██║██║  ██║███████╗╚███╔███╔╝██║  ██║██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                     [+] created by baalware   \n                 
"""
os.system("cls")
print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(baalware)))
def modo1(arquivos, string):
    with open(arquivos, encoding='utf-8') as f:
        s = f.read()
    z = []
    for i in s:
        z.append(ord(i))
    pea = []
    for i in z:
        pea.append(string.replace("'", "").replace('"', '')*i)
    arquivo = """#ofuscado by baalware

d={};exec("".join([chr(len(i)) for i in d]))
    """.format(pea)
    arquivo_saida = os.path.join("baalware obfs", os.path.splitext(os.path.basename(arquivos))[0] + "criptografado.py")
    with open(arquivo_saida, "w", encoding='utf-8') as f:
        f.write(arquivo)
        os.system("cls")
    print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(baalware)))
    logging.info("Arquivo criptografado com sucesso como '{}'".format(arquivo_saida))
    print(Center.XCenter("Arquivo criptografado com sucesso como '{}'".format(arquivo_saida)))

while True:
    arquivo = input("\nnome do arquivo que será criptografado: ")
    if arquivo.lower() == 'sair':
        break
    string = ("ㅤ")
    modo1(os.path.join("baalware obfs", arquivo), string)
