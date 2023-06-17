meu_dicionario = {'A': 10, 'B': 5, 'C': 15, 'D': 3}

chaves_ordenadas = sorted(meu_dicionario, key=meu_dicionario.get)

for chave in chaves_ordenadas:
    print(chave, meu_dicionario[chave])
