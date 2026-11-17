
import sqlite3

# Banco de dados ficticio para testes de seguranca
conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    usuario TEXT,
    senha TEXT
)
""")

cursor.execute(
    "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
    ("admin", "senha123")
)
conexao.commit()

# Login propositalmente vulneravel
usuario = input("Usuario: ")
senha = input("Senha: ")

query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"

cursor.execute(query, (usuario, senha))
resultado = cursor.fetchone()

if resultado:
    print("Login realizado com sucesso!")
else:
    print("Usuario ou senha incorretos.")

conexao.close()
