#Convertendo tipos
    #Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo: Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

#Inteiro para Float:

preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2 #Inteiro para Float através da divisão
print(preco)

#Float para Inteiro:

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

preco = 10
print(preco / 2)
print(preco // 2) #Float para Inteiro através da divisão utilizando duas barras

#Numérico para String:

preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade = {idade} e preço = {preco}"
print(texto)

#String para Numérico:

preco = "10.50"
idade = "28"

print(float(preco))
print(float(idade))