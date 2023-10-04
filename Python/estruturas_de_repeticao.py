#O que são as estruturas de repetição?
    #São estruturas utlizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.
#Exemplo sem repetição:

# Receba um número do teclado e exiba os 2 números seguintes

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

#Comando for
    #O comando for é usado para percorrer um objeto iterável. Faz sentido usar o for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável. Exemplo:

texto = (input("Informe um texto: "))
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()        #adiciona uma quebra de linha


#For/Else - Exemplo:

texto = (input("Informe um texto: "))
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("Executa no final do laço") 

#Função range
    #Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos range (i,j) será produzido:
    # i, i+1, i+2, i+3, ..., j-1.
    #Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4)) # >>>> Retorna [0, 1, 2, 3]

#Utilizando o range com o for

for numero in range(0,11):
    print(numero, end=" ")

# exibindo a tabuada do 5:
for numero in range(0, 51, 5): #start, stop, step 
    print(numero, end=" ")

#Comando while
    #O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")      


#Break: essa função interrompe o laço de repetição

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

#Continue: essa função é útil quando queremos pular algum objeto específico de uma lista

for numero in range(100):
    if numero == 12:
        continue
    print(numero, end=" ")
