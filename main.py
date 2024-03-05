import numpy as np
from numpy import linalg
from numpy.linalg import det

#Funções
def permutaLinha(sistema, linhaNova, linhaTrocada):
    sistema[[linhaTrocada, linhaNova]] = sistema[[linhaNova, linhaTrocada]]

def simplificaLinha(linha, x):#Primeiro termo não-nulo
    if linha[x] != 0:
        linha /= linha[x]

def resolveSistema(sistema, ordem):

    #Escalonando a matriz
    #Se existir algum 1x, coloca a linha como a primeira
    for i in range(ordem):
        if sistema[i, 0] == 1:
            permutaLinha(sistema, i, 0)

    #Transforma o termo 1 da primeira linha em 1
    simplificaLinha(sistema[0], 0)

    #zerando de cima pra baixo
    for k in range(ordem):
        simplificaLinha(sistema[k], k)
        for i in range(k, ordem):
            if i > k:
                sistema[i] -= sistema[k] * sistema[i, k]

    #zerando de baixo pra cima
    for k in reversed(range(ordem)):
        simplificaLinha(sistema[k], k)
        for i in reversed(range(ordem)):
            if i < k:
                sistema[i] -= sistema[k] * sistema[i, k]


    #printando o resultado
    res = np.zeros((ordem))

    for i in range(ordem):
        for j in range(ordem + 1):
            if j == ordem:
                res[i] = sistema[i, j]

    return res

#Início do Programa
print(20*"-", "RESOLVE SISTEMAS", 20*"-")

N = int(input("\nÉ um sistema de ordem: "))

#criando as matrizes
sis = np.zeros((N, N + 1))
sisDet = np.zeros((N, N))

#Lendo as matrizes
print("Digite os coeficientes 1 a 1, e depois o resultado da equação: ")

for i in range(N):
    for j in range(N + 1):
        if j < N:
            sis[i, j] = float(input(f'X{j + 1}: '))
            sisDet[i, j] = sis[i, j]
        if j == N:
            sis[i, j] = float(input("Resultado: "))

#Printando a matriz lida
print(f'A matriz dos coeficientes é:')
print(sis)

#Resolvendo o sistema
print("\n\tRESULTADO\n")

if(det(sisDet) != 0):
    print("S =",resolveSistema(sis, N))
else: print("Sistema SDI ou SI")
