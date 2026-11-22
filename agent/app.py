import sqlite3
import pandas
from contextlib import closing


def fazer_login(usuario, senha):
    query = (
        "SELECT 1 FROM usuarios "
        "WHERE username = ? AND password = ? "
        "LIMIT 1"
    )

    with closing(sqlite3.connect("banco_de_dados.db")) as conexao:
        resultado = conexao.execute(query, (usuario, senha)).fetchone()

    if resultado:
        return "Acesso Permitido!"
    return "Acesso Negado."