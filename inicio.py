
# hhtp://www.sqlite.org/docs.html

#remove o arquivo com o banco de dados SQLite (caso exista)
import os
os.remove("escola.db") if os.path.exists("escola.db") else None

#importando o módulo de acesso ao SQLite
import sqlite3

#Cria conexão com o banco de dados
conexao=sqlite3.connect("escola.db")

#criando um cursor, ele permite acessar todos os registros de um conjunto de dados
kursor=conexao.cursor()

#Cria uma instrução sql
sql_create = 'create table cursos'\
    '(id integer primary key, '\
    'titulo varchar(100), '\
    'categoria varchar(140))'

#cria a tabela
kursor.execute(sql_create)

#inserindo registros
sql_insert='insert into cursos values (?,?,?)'

#Dados
recset= [(1000, 'Ciencia de dados', 'Data Science'),
          (1001, 'BigData Fundamentos', 'BigData'),
          (1002, 'Python', 'Analise de dados')]

#Inserindo os registros
for rec in recset:
    kursor.execute(sql_insert, rec)

#grava a transação
conexao.commit()

#Criando outra sentença SQL para selecionar registros
sql_select= 'select*from cursos'

#Seleciona todos os registros e recupera os registros
kursor.execute(sql_select)
dados=kursor.fetchall()

#Gerando outros registros
recset=[(1003, 'Gestao de dados MongoBD', 'BigData'),
          (1004, 'R Fundamentos', 'Analise de dados')]

#inserindo registros
for rec in recset:
    kursor.execute(sql_insert, rec)

conexao.commit()

kursor.execute(sql_select)
dados=kursor.fetchall()
#mostra
for linha in dados:
    print('Curso Id: %d, Titulo: %s, Categoria: %s \n' %linha)

conexao.close()
