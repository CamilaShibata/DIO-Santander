#Métodos da classe dict

# {}.clear

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766"}
}

contatos.clear()
print(contatos) #>>Retorna {}

# {}.copy

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome":"Gui"}

print(contatos["guilherme@gmail.com"]) #>>Retorna {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(copia["guilherme@gmail.com"])    #>>Retorna {'nome': 'Gui'}

# {}.fromkeys

print(dict.fromkeys(["nome", "telefone"]))          #>>Retorna {'nome': None, 'telefone': None}
print(dict.fromkeys(["nome", "telefone"], "vazio")) #>>Retorna {'nome': 'vazio', 'telefone': 'vazio'}

# {}.get (Pede pra buscar uma chave e se não encontra, pode fornecer um argumento para trazer no lugar)

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

print(contatos["chave"]) #>>Retorna KeyError: 'chave'

contatos.get("chave") #>>Retorna None
contatos.get("chave", {}) #>>Retorna {}
contatos.get("guilherme@gmail.com", {}) #>>Retorna "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}

# {}.items

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

contatos.items() #>>Retorna dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

# {}.keys

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

print(contatos.keys()) #>>Retorna dict_keys(['guilherme@gmail.com'])

# {}.pop

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

contatos.pop("guilherme@gmail.com") #>>Retorna {'nome': 'Guilherme', 'telefone': '3333-2221'}
contatos.pop("guilherme@gmail.com", {}) #>>Retorna {}

# {}.popitem (Retira os itens sequencialmente, se estiver vazio retorna un KeyError)

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

contatos.popitem() #>>Retorna ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
contatos.popitem() #>>Retorna KeyError

# {}.setdefault (Se o valor não estiver atribuído a chave, ele adiciona o novo valor, se não, nada é alterado e retorna o padrão que já estava)

contato = {'nome':'Guilherme', 'telefone':'3333-2221'}

contato.setdefault("nome", "Giovanna") #>>Retorna 'Guilherme'
contato #>>Retorna {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) #>>Retorna 28
contato #>>Retorna {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

# {}.update

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

contatos.update({"guilherme@gmail.com":{"nome":"Gui"}})
contatos #>>Retorna {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3322-8181"}})
contatos #>>Retorna {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

# {}.values

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766"}
}

contatos.values() #>>Retorna dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])

# in

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766"}
}

"guilherme@gmail.com" in contatos #>>Retorna True
"megui@gmail.com" in contatos #>>Retorna False
"idade" in contatos["guilherme@gmail.com"] #>>Retorna False
"telefone" in contatos["giovanna@gmail.com"] #>>Retorna True

# del

contatos = {
    "guilherme@gmail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766"}
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

contatos #>>Retorna {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}