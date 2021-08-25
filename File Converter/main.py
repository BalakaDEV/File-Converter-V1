#Modificar Formato de Arquivos
import os
import sys
import os.path

#Reiniciar aplicação
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#Diretorio + Verificação
direct = input("Coloque o diretório dos arquivos: ")
if os.path.isdir(f"{direct}"):
    print("Diretório Validado")
else:
    print("O diretório não existe!")
    restart_program() 

formato = input("Informe o formato do arquivo atual (.txt, .mp4, .png, .jpg...) ")    

#Verificação do arquivo + nome
old = input("Coloque o nome do arquivo atual: ")
if(os.path.exists(f"{direct}/{old}{formato}")):
    print("Arquivo validado") 
else:
    print("Arquivo não encontrado")
    restart_program()


formato2 = input("Informe o formato do arquivo novo (.txt, .mp4, .png, .jpg...) ")       

#Novo nome
new = input("Coloque o nome do arquivo novo: ")
if os.path.exists(f"{direct}/{new}{formato2}"):
    print("O arquivo já existe tente outro nome")
    restart_program() 

old_file = os.path.join(f"{direct}", f"{old}{formato}") #Nome do arquivo atual
new_file = os.path.join(f"{direct}", f"{new}{formato2}") #Nome para o arquivo novo
os.rename(old_file, new_file)
print("Mudanças realizadas")

input()