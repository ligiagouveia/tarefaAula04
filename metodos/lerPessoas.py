def printarTodasAsPessoas(arquivo):
    with arquivo.lerArquivo() as f:
        print(f.read())
    