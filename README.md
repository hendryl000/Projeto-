
<div align="center">
    <img src="https://user-images.githubusercontent.com/80292331/228837470-aeee2713-f2a0-478c-b26b-6ef1b6855eed.png"
</div><br>
Projeto 01
    <h3>Equipe:</h3>
    <p color="red">
        Eduardo Freira<br>
        Hendryl<br>
        Matheus Beiruth<br>
        Deivison Alexandre
    </p>
<div align = "left">
#importações e Elementos:<br>
import time<br>
import matplotlib.pyplot as plt<br>

elementos = [[0, 1, 2, 3],[11, 12, 13, 4],[10, 15, 14, 5],[9, 8, 7, 6]]

#Definir a lista vazia para armazenar os elementos ordenados:<br>
lista_ordenada = []

#Loop para percorrer todas as linhas da matriz:<br>
for linha in elementos:

#Adicionar todos os elementos da linha à lista:<br>
    lista_ordenada.extend(linha)

#Ordenar a lista em ordem crescente:<br>
    lista_ordenada.sort()

#Imprimir a lista ordenada e sua notação Big'O:<br>
print("Lista ordenada em ordem crescente: ", lista_ordenada)

#Ordenar a lista em ordem decrescente:<br>
lista_ordenada.reverse()

#Imprimir a lista ordenada e sua notação Big'O:<br>
print("Lista ordenada em ordem decrescente: ", lista_ordenada)
    
#grafico:<br>

def fib(lista_ordenada):
    if lista_ordenada <= 1:
        return lista_ordenada
    return fib(lista_ordenada - 1) + fib(lista_ordenada - 2)

# listas para armazenar os valores de n e o tempo de execução:<br>
ns = []
tempos = []

# Valor de lista_ordenada:<br>
for lista_ordenada in range(1, 16):
    start = time.perf_counter()
    result= fib(lista_ordenada)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(lista_ordenada)
    tempos.append(ms)
print(result)
# cria o gráfico:<br>
plt.plot(ns, tempos)
plt.xlabel('Valor de lista_ordenada')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()

</div>
