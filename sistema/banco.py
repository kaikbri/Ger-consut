import sqlite3
from pathlib import Path

ARQUIVO = Path(__file__).with_name("consultas.db")


def conectar():
    con = sqlite3.connect(ARQUIVO)
    con.execute(
        "CREATE TABLE IF NOT EXISTS consultas ("
        "sus TEXT PRIMARY KEY, paciente TEXT, medico TEXT, "
        "data TEXT, hora TEXT, observacoes TEXT)"
    )
    con.commit()
    return con


def listar(con):
    return con.execute(
        "SELECT sus,paciente,medico,data,hora,observacoes FROM consultas "
        "ORDER BY substr(data,7,4),substr(data,4,2),substr(data,1,2),hora"
    ).fetchall()


def inserir(con, dados):
    con.execute(
        "INSERT INTO consultas (sus,paciente,medico,data,hora,observacoes) "
        "VALUES (?,?,?,?,?,?)",
        dados,
    )
    con.commit()
