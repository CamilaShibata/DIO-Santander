#Criando listas
    #Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor list, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação. Exemplos:

frutas = ["laranja", "maçã", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

#Acesso direto
    #A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero. Exemplo:

frutas = ["maçã", "laranja", "uva", "pêra"]
frutas[0] #>> Retorna "maçã"
frutas[2] #>> Retorna "uva"  

#Índices negativos
    #Sequências suportam indexação negativa. A contagem começa em -1. Exemplo:

frutas = ["maçã", "laranja", "uva", "pêra"]
frutas[-1] #>> Retorna "pêra"
frutas[-3] #>> Retorna "laranja"   

#Listas aninhadas
    #Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna. Exemplo:

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]    

matriz[0]      #>>Retorna [, "a", 2]
matriz[0][0]   #>>Retorna 1
matriz[0][-1]  #>>Retorna 2
matriz[-1][-1] #>>Retorna "c"

#Fatiamento
    #Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso. Exemplo:

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]     #>>Retorna ["t", "h", "o", "n"]
lista[:2]     #>>Retorna ["p", "y"]
lista[1:3]    #>>Retorna ["y", "t"]
lista[0:3:2]  #>>Retorna ["p", "t"]
lista[::]     #>>Retorna ["p", "y", "t", "h", "o", "n"]
lista[::-1]   #>>Retorna ["n", "o", "h", "t", "y", "p"]

#Iterar listas
    #A forma mais comum para percorrer os dados de uma lista é utilizando o comando for. Exemplo:

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

#Função enumerate
    #Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate. Exemplo:

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}") 

#Compreensão de listas
    #A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista exigente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

#Filtro versão 1:

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#Filtro versão 2:

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Modificando valores versão 1:

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

#Modificando valores versão 2:

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)