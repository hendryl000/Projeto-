
<div align="center">
    <img src="https://user-images.githubusercontent.com/80292331/228837470-aeee2713-f2a0-478c-b26b-6ef1b6855eed.png">

</div><br>
<div align="center">
<h3>Projeto 01</h3><br>
Curso:<br>
Eng.Software
    

<h3>Equipe:</h3>
    
Eduardo Freira<br>
Hendryl<br>
Matheus Beiruth<br>
Deivison Alexandre
    
    
<h3>Disciplina:</h3><br>
   
Estrutura de Dados

<h3>Período:</h3><br>
    
Terceiro Periíodo
    
<h3>Professor:</h3><br>
    
Marcio
</div><br>
<div align = "left">

<h3>#importações e Elementos:</h3><br>
import time<br>
import matplotlib.pyplot as plts<br>

elementos = [[0, 1, 2, 3],[11, 12, 13, 4],[10, 15, 14, 5],[9, 8, 7, 6]]

<h3>#Definir a lista vazia para armazenar os elementos ordenados:</h3><br>
lista_ordenada = []

<h3>#Loop para percorrer todas as linhas da matriz:</h3><br>
for linha in elementos:

<h3>#Adicionar todos os elementos da linha à lista:</h3><br>
    lista_ordenada.extend(linha)

<h3>#Ordenar a lista em ordem crescente:</h3><br>
    lista_ordenada.sort()

<h3>#Imprimir a lista ordenada e sua notação Big'O:</h3><br>
print("Lista ordenada em ordem crescente: ", lista_ordenada)

<h3>#Ordenar a lista em ordem decrescente:</h3><br>
lista_ordenada.reverse()

<h3>#Imprimir a lista ordenada e sua notação Big'O:</h3><br>
print("Lista ordenada em ordem decrescente: ", lista_ordenada)
    
<h3>#grafico:</h3><br>

def fib(lista_ordenada):
    if lista_ordenada <= 1:
        return lista_ordenada
    return fib(lista_ordenada - 1) + fib(lista_ordenada - 2)

<h3># listas para armazenar os valores de n e o tempo de execução:</h3><br>
ns = []
tempos = []

<h3># Valor de lista_ordenada:</h3><br>
for lista_ordenada in range(1, 16):
    start = time.perf_counter()
    result= fib(lista_ordenada)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(lista_ordenada)
    tempos.append(ms)
print(result)
    <h3># cria o gráfico:</h3><br>
plt.plot(ns, tempos)
plt.xlabel('Valor de lista_ordenada')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()

</div>
