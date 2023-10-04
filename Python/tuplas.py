#Criando tuplas
    #Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que as tuplas são imutáveis, enquanto as listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parênteses. Exemplo:

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#Acesso direto
    #A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero. O mesmo funciona para o índice negativo, começando pelo -1. Exemplo:

frutas = ("maçã", "laranja", "uva", "pêra",)
frutas[0] #>>Retorna "maçã"
frutas[2] #>>Retorna "uva"
frutas[-1] #>>Retorna "pêra"
frutas[-3] #>>Retorna "laranja"

#Métodos
    #Como as tuplas são imutáveis, não são todos os métodos que servem pra elas assim como as listas. Com as tuplas utilizamos somente:
# ().count
# ().index
# len