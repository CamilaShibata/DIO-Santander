# [].append

lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) #>>Retorna [1, "Python", [40, 30, 20]]

# [].copy

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista) #>>Retorna [1, "Python", [40, 30, 20]]

# [].count

cores = ["vermelho", "azul", "verde", "azul"]

lista.count("vermelho") #>>Retorna 1
lista.count("azul") #>>Retorna 2
lista.count("verde") #>>Retorna 1

# [].extend (O extend irá adicionar na lista todos os objetos citados, mesmo que seja repetido)

linguagens = ["python", "js", "c"]

print(linguagens) #>>Retorna ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) #>>Retorna ["python", "js", "c", "java", "csharp"]

# [].index (O index se limita a encontrar a primeira ocorrência)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java")   #>>Retorna 3
linguagens.index("python") #>>Retorna 0

# [].pop (Conceito de pilha)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop()  #>>Retorna "csharp"
linguagens.pop()  #>>Retorna "java"
linguagens.pop()  #>>Retorna "c"
linguagens.pop(0) #>>Retorna "python"

# [].remove

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")
print(linguagens) #>>Retorna ["python", "js", "java", "csharp"]

# [].reverse

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()
print(linguagens) #>>Retorna ["csharp", "java", "c", "js", "python"]

# [].sort

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() #>>Retorna ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #>>Retorna ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) #>>Retorna ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #>>Retorna ["python", "csharp", "java", "js", "c"]

# len (O len lê o tamanho das coisas, strings ou listas)

linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens) #>>Retorna 5


# sorted

linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) #>>Retorna ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) #>>Retorna ["python", "csharp", "java", "js", "c"]