#Introdução
    #A classe string do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar. Em algumas linguagens manipular as sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

#Maiúscula, Minúscula e Título:

curso = "pYtHon"

print(curso.upper()) #>>Retorna PYTHON
print(curso.lower()) #>>Retorna python
print(curso.title()) #>>Retorna Python

#Eliminando espaços em branco:

curso = "     'Python'  "

print(curso.strip())  #>>Retorna "Python"
print(curso.lstrip()) #>>Retorna "Python  "
print(curso.rstrip()) #>>Retorna "     Python"

#Junções e centralização de strings:

curso = "Python"

print(curso.center(10, "#")) #>>Retorna "##Python##"
print(".".join(curso))       #>>Retorna "P.y.t.h.o.n"