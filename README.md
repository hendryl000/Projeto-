
<div align="center">
    <img src="https://user-images.githubusercontent.com/80292331/230384765-4b382974-9ff3-4610-b2fd-0563f2c776e3.png">

</div><br>
<div align="left">
<h3>Projeto 01</h3>
<h3>Curso:</h3>Eng.Software
    
<h3>Equipe:</h3>   
Eduardo Freira,<br>
Hendryl,<br>
Matheus Beiruth,<br>
Deivison Alexandre,<br>
Matheus Sousa 
     
<h3>Disciplina:</h3>Estrutura de Dados

<h3>Período:</h3>Terceiro Período
    
<h3>Professor:</h3>Marcio
</div><br>
<div align = "left">
<h3>Introdução</h3>
O código em Python apresenta duas tarefas distintas: ordenação de uma matriz e a execução da função Fibonacci para diferentes valores de entrada.

A ordenação de uma matriz é um problema comum na ciência da computação, e existem várias técnicas para solucioná-lo. Nesse caso, o código utiliza a técnica de percorrer cada linha da matriz, adicionar todos os elementos da linha a uma lista e, em seguida, ordenar essa lista em ordem crescente e decrescente usando as funções sort() e reverse(), respectivamente.

Já a função Fibonacci é um problema matemático clássico que consiste em determinar o n-ésimo termo de uma sequência numérica. A sequência é definida como a soma dos dois termos anteriores, sendo que os dois primeiros termos são 0 e 1. O código utiliza uma função recursiva para calcular o n-ésimo termo da sequência Fibonacci.

Além disso, o código armazena os valores de tempo de execução da função Fibonacci para diferentes valores de entrada e plota um gráfico que mostra a relação entre o tamanho da entrada e o tempo de execução. Essa técnica é comumente utilizada para analisar a complexidade temporal de algoritmos, e pode ser útil para avaliar o desempenho de diferentes soluções para o mesmo problema.
</div><br>
<div align = "left">
    <h3>Codigo / Explicação</h3>
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
<img src="https://user-images.githubusercontent.com/80292331/230398581-23075d84-38e7-4e45-9570-c0b919d84e4f.png">
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
