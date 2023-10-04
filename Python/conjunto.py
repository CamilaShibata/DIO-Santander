#Criando sets
    #Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável. Importante lembrar que o set não garante a ordem de saída dos objetos. Exemplos:

set([1, 2, 3, 1, 3, 4]) #>>Retorna {1, 2, 3, 4}
set("abacaxi") #>>Retorna {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) #>>Retorna {"gol", "celta", "palio"}

#Acessando os dados
    #Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista. Exemplo:

numero = {1, 2, 3, 2}

numeros = list(numero)
print(numeros[0]) #>>Retorna 1

#Iterar conjuntos
    #A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for. Exemplo:

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#Função enumerate
    #Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate. Exemplo:

carros = {"gol", "celta", "palio"}    

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Métodos da classe set

# {}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b)) #>>Retorna {1, 2, 3, 4}

# {}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b)) #>>Retorna {2, 3}

# {}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) #>>Retorna {1}
print(conjunto_b.difference(conjunto_a)) #>>Retorna {4}

# {}.symmetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) #>>Retorna {1, 4}

# {}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) #>>Retorna True
print(conjunto_b.issubset(conjunto_a)) #>>Retorna False

# {}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b)) #>>Retorna False
print(conjunto_b.issuperset(conjunto_a)) #>>Retorna True

# {}.isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) #>>Retorna True
print(conjunto_a.isdisjoint(conjunto_c)) #>>Retorna False

# {}.add

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio) #>>Retorna {1, 42, 25, 23}

# {}.clear

sorteio = {1, 23}
sorteio.clear()

print(sorteio) #>>Retorna {}

# {}.copy

sorteio = {1, 23}
sorteio.copy()

print(sorteio) #>>Retorna {1, 23}

# {}.discard

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(5)

print(numeros) #>>Retorna {0, 2, 3, 4, 6, 7, 8, 9}

# {}.pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.pop() #>> Tirou número 0
numeros.pop() #>> Tirou número 1

print(numeros) #>>Retorna {2, 3, 4, 5, 6, 7, 8, 9}

# {}.remove (A diferença entre o remove e o discard é que se colocar para remover um elemento que não existe no conjunto, ele aponta um erro. O discard não tem esse problema.)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.remove(0) #>> Tirou número 0

print(numeros) #>>Retorna {1, 2, 3, 4, 5, 6, 7, 8, 9}

# len

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print (len(numeros)) #>>Retorna 10

# in

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  #>>Retorna True
print(10 in numeros) #>>Retorna False
