from flask import Flask, renden_template
import sqlite3
app = Flask (__name__)
#conexion con la base de datos
def get_connection():
    conn= sqlite3.connect('database.db')
    conn.row_factory=sqlite3.Row
    return conn