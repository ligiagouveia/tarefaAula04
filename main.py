from metodos.cadastrarPessoas import escreverNomes
from metodos.lerPessoas import printarTodasAsPessoas
from arquivos.manipulaArquivos import arquivo
nomes=arquivo("nomes.txt")
while True:
    opcao=0
    try:
        opcao=int(input("1 - Para informar um nome\n2 - Para ver lista\n0 - Para sair\n"))
    except ValueError:
        print("Deve ser informado umas das opçoes informadas")
        continue
    if(opcao==1):
        nome=input("Informe o nome a ser inserido na lista: ")
        escreverNomes(nome+"\n",nomes)
        print("\n"+nome+" cadastrado com sucesso")
    elif(opcao==2):
        printarTodasAsPessoas(nomes)
    elif(opcao==0):
        break
    else:
        print("Opcao incorreta")