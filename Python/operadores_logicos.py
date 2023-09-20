#Operadores Lógicos
    #São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, por exemplo:
        #op_comparacao + op_logico + op_comparacao...N...

saldo = 1000
saque = 200
limite = 100

saldo >= saque #>>>> True
saque <= limite #>>>> False

#Operador E

saldo >= saque and saque <= limite #>>>> False (Se tudo na sentença for verdadeiro, então o resultado é True. Se algo for falso, então o resutado é False)

#Operador OU

saldo >= saque or saque <= limite #>>>> True (Se apenas uma pessoa retorna verdadeira, então a sentença é True)

#Operador de Negação

contatos_emergencia = []

not 1000 > 1500 #>>>> True

not contatos_emergencia #>>>> True

not "saque 1500" #>>>> False

not "" #>>>> True


#Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque #>>>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #>>>> True (É uma boa prática separar as sentenças por parênteses para ficar mais legível)


#Na condição AND, para ser True, tudo tem que ser True
print(True and True) #>>> True
print(True and False) #>>> False
print(False and False) #>>> False

#Na condição OR, Para ser True, apenas uma sentença tem que ser True.
print(True or True) #>>> True
print(True or False) #>>> True
print(False or False) #>>> False