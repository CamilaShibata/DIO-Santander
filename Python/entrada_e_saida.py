#Lendo valores com a função input:
    #A função built in input é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

nome = input("Informe o seu nome: ")

#Exibindo valores com a função print:
    #A função built in print é utilizada quando queremos exibir dados na saída padrão (tela). Ea recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

nome = "Camila"
sobrenome = "Shibata"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

#Exemplo com as duas funções:

nome = input("Informe o seu nome: ")
print("O nome informado é",nome)