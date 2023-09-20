#Variáveis
    #Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem om um valor e não necessariamente devem permanecer com o mesmo durante a execução.

age = 34
name = 'Camila'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

age, name = (34, 'Camila')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

#Alterando os Valores
    #Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável, basta fazer uma atribuição de um novo valor:

age = 34
name = 'Camila'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

age = 29
name = 'Leonardo'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

#Constantes
    #Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.
    #PYTHON NÃO TEM CONSTANTE! Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens, por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
    #Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras MAIÚSCULAS: (MAIUSCULAS = CONSTANTE)!

#Boas Práticas
    #O padrão de nomes deve ser snake_case
    #Escolher nomes sugestivos
    #Nome de constantes todo em maiúsculo