#O que são os operadores aritméticos?
    #Os operadores aritméticos executam operações matemáticas, como audição, subtração com operandos.

#adição
print(1 + 1)

#subtração
print(10 - 2)

#multiplicação
print(4 * 3)

#divisão
print(12 / 3)

#divisão inteira
print(12 // 2)

#módulo
print(10 % 3) #módulo é o mesmo que o resto da divisão

#exponenciação
print(2 ** 3)

#Precedência dos Operadores
    #Na matemática existe um regra que indica quais operações devem ser executadas primeiro. Isso é útil pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser diferente:
    # x = 10-5*2 (x é igual a 10 ou a 0?)
    #A definição indica a seguinte ordem como a correta: 
        #Parêntesis
        #Expoêntes
        #Multiplicações e divisões (da esquerda para a direita)
        #Somas e subtrações (da esquerda para a direita)

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 10 + 5 * 4 #utilizando a precedência dos operadores
print(x)

x = (10 + 5) * 4 #utilizando a precedência dos operadores com parênteses o resultado será outro
print(x)