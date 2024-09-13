from functions import *

# Codigo responsavel por vizualizar o menu do codigo.
while True:
    os.system("cls")
    print("/-------------------------/")
    print("|[1] - Visualizar Tarefas |")
    print("|[2] - Criar Tarefas      |")
    print("|[3] - Editar Tarefas     |")
    print("|[4] - Excluir Tarefas    |")
    print("|[5] - Sair               |")
    print("|-------------------------/")
    menu = int(input("--> "))

#Codigos responsaveis por importar "os DEF" do arquivo "functions.py"
    if menu == 1:
        visualizar()

    if menu == 2:
        criar()

    if menu == 3:
        editar()

    if menu == 4:
        excluir()

    if menu == 5:
        time.sleep(1)
        break