import sys
import string
import os

fileName = input(
    "Qual o nome do arquivo que você deseja executar?(sem a extensão, ex: .exe/.py) ")
path = os.getcwd()  # + "\Executador"
#path = "D:/Documentos/Projetos/Auto Github Commiter/Code"
print(path)
os.chdir(path)
extenção = input("Qual a extenção do arquivo? ")

if(extenção == "py"):
    os.system("py " + fileName + ".py")
if(extenção == "exe"):
    os.system(fileName + ".exe")
