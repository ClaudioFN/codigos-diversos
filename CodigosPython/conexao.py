import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

# CRIAR TABELA
def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    conexao.commit()
    
# INCLUIR REGISTROS
def incluir_registros(conexao, cusor, nome, email):
    data = ('JFK', 'jfk@shoot.com')
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', data)
    conexao.commit()
    
def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id = ?', data)
    conexao.commit()
    
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES(?, ?)', dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id, ))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
cliente = recuperar_cliente(cursor, 2)
print(cliente)
#dados = [
#    ('RAPADURA1', 'rapadura1@gmail.com'),
#    ('RAPADURA2', 'rapadura2@gmail.com'),
#    ('RAPADURA3', 'rapadura3@gmail.com'),
#]
#inserir_muitos(conexao, cursor, dados)