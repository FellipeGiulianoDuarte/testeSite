#gerar os números numa array, salvar no json
import random
import json

def matriz_rand(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(random.randint(1,10))
        matriz.append(linha)
    return matriz

def matriz_para_json():
    A = matriz_rand(10,10)
    print(A)
    dados = open("dados.json", "w")
    json.dump(A, dados, indent = 3)
    dados.close()

matriz_para_json()