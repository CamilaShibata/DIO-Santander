#Criando dicionários
    #Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separadas por vírgulas. Exemplo:

pessoa = {"nome":"Guilherme", "idade":28} #Atribuindo valores à variável pessoa, por método comum.

pessoa = dict(nome="Guilherme", idade=28) #Atribuindo valores à variável pessoal, pelo método dict.

pessoa["telefone"] = "3333-1234" #Atribuindo uma nova chave à uma variável já existente.

#Acesso aos dados
    #Os dados são acessados e modificados através da chave. Exemplo:

pessoa = {"nome":"Guilherme", "idade":28, "telefone":"3333-1234"}

#Acessando e imprimindo os dados: 
print(pessoa["nome"])       #>>Retorna Guilherme
print(pessoa["idade"])      #>>Retorna 28
print(pessoa["telefone"])   #>>Retorna 3333-1234

#Atribuindo novos valores e modificando os existentes:
pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "9988-1781"

print(pessoa) #>>Retorna {'nome': 'Maria', 'idade': 18, 'telefone': '9988-1781'}

#Dicionários aninhados
    #Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números). Exemplo:

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766"}
}

print(contatos["giovanna@gmail.com"]["telefone"]) #>>Retorna 3443-2121

#Iterar dicionários
    #A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for. Exemplo:

#for chave in contatos:
   # print(chave, contatos[chave]) >>>Essa não é a maneira mais recomendada para iterar e sim a de baixo.

for chave, valor in contatos.items():
    print(chave, valor)