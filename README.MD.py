import time
import matplotlib.pyplot as plt

elementos = [[0, 1, 2, 3],[11, 12, 13, 4],[10, 15, 14, 5],[9, 8, 7, 6]]

#Definir a lista vazia para armazenar os elementos ordenados
lista_ordenada = []

#Loop para percorrer todas as linhas da matriz
for linha in elementos:

#Adicionar todos os elementos da linha à lista
    lista_ordenada.extend(linha)

#Ordenar a lista em ordem crescente
    lista_ordenada.sort()

#Imprimir a lista ordenada e sua notação Big'O
print("Lista ordenada em ordem crescente: ", lista_ordenada)

#Ordenar a lista em ordem decrescente
lista_ordenada.reverse()

#Imprimir a lista ordenada e sua notação Big'O
print("Lista ordenada em ordem decrescente: ", lista_ordenada)

def fib(lista_ordenada):
    if lista_ordenada <= 1:
        return lista_ordenada
    return fib(lista_ordenada - 1) + fib(lista_ordenada - 2)

# listas para armazenar os valores de n e o tempo de execução
ns = []
tempos = []

# testa a função para vários valores de n
for lista_ordenada in range(1, 16):
    start = time.perf_counter()
    result= fib(lista_ordenada)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(lista_ordenada)
    tempos.append(ms)
print(result)
# cria o gráfico
plt.plot(ns, tempos)
plt.xlabel('Valor de lista_ordenada')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()

