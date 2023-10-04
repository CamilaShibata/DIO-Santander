#O que são funções?
    #Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros. Esses parâmetros pode ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada. Exemplo:

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")      

#Retornando valores
    #Para retornar um valor, utilizamos a palavra reservada return. Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor. Exemplo:

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34])
retorna_antecessor_sucessor(10)    

#Argumentos nomeados
    #Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor. Exemplo:

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#Existem 3 maneiras de chamar a função:

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") #apenas definindo os valores
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") #atribuindo os valores aos argumentos
salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1234"}) #atribuindo os valores às chaves

#Args e kwargs
    #Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente. Exemplo:

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso} \n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de agosto de 2022",      #primeiro argumento data_extenso
    "Zen of Python",                         #segundo argumento *args
    "Beautiful is better than ugly.",        #segundo argumento *args
    autor="Tim Peters",                      #terceiro argumento *kwargs
    ano=1999)                                #terceiro argumento *kwargs