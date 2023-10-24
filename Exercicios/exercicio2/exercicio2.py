with open('exercicios/exercicio2/foods.csv', 'r') as arquivo:
    dicionario = {}
    conta_linha = 1
    for linha in arquivo:
        if conta_linha > 1:             # ignora a primeira linha do arquivo
            lista = linha.split(';')
            prato = lista[2].replace('\n', '')
            if prato in dicionario:
                dicionario[prato] += 1
            else:
                dicionario[prato] = 1
        conta_linha += 1

maior = 0
prato = ''
for chave, valor in dicionario.items():
    if valor > maior:
        maior = valor
        prato = chave
print(f'{prato}: {maior}')