def escreverNomes(nome,arquivo):
    with arquivo.escreveArquivo() as f:
        f.write(nome)