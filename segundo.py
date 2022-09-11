
import os
os.remove("dsa.db") if os.path.exists("dsa.db") else None
import sqlite3
import random
import time
import datetime

conexao=sqlite3.connect("dsa.db")
kursor=conexao.cursor()

def create_table():
    kursor.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
                    'prod_name TEXT, valor REAL)')

def data_insert():
    kursor.execute("INSERT INTO produtos VALUES(10, '2018-05-02 14:21:11', 'Teclado', 90)")
    conexao.commit()
    kursor.close()
    conexao.close()

def data_insert_variavel():
    new_date =datetime.datetime.now()
    new_prod_name='Monitor'
    new_valor=random.randrange(50,100)
    kursor.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
    conexao.commit()

def leitura_todos_dados():
    kursor.execute("SELECT * FROM PRODUTOS")
    for linha in kursor.fetchall():
        print(linha)

#imprime só os registros dos produtos com valor acima de 87
def leitura_registros():
    kursor.execute("SELECT * FROM PRODUTOS WHERE valor > 87.0")
    for linha in kursor.fetchall():
        print(linha)

def leitura_colunas():
    kursor.execute("SELECT * FROM PRODUTOS")
    for linha in kursor.fetchall():
        print(linha[3])

def atualiza_dados():
    kursor.execute("UPDATE produtos SET valor =87 WHERE valor=99.9")
    conexao.commit()

def remove_dados():
    kursor.execute("DELETE FROM produtos WHERE valor=66.0")
    conexao.commit()
    
#def dados_graficos():
 #   kursor.execute("SELECT id, valor FROM produtos")
  #  ids = []
   # valores=[]
    #dados=kursor.fetchall()
    #for linha in dados:
     #   ids.append(linha[0])
      #  valores.append(linha[1])

create_table()
for i in range(10):
    data_insert_variavel()
    time.sleep(1)

print("\nLeitura de todos os dados: \n")
leitura_todos_dados()
print("\nLeitura de registro: \n")
leitura_registros()
print("\nLeitura de uma coluna: \n")
leitura_colunas()
atualiza_dados()
remove_dados()
print("\nLeitura de todos os dados: \n")
leitura_todos_dados()

#Onde plt=gráfico e bar= de barras
#plt.bar(ids, valores)
#plt.show()
#dados_graficos()

kursor.close ()
conexao.close()