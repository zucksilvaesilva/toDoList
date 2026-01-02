import sqlite3

con = sqlite3.connect("to_do.db")
cur = con.cursor()

#status = 0 [Não feita], 1 [feita]
def initialize_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS task_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            status INTEGER DEFAULT 0
        )
    """)

print("Banco de dados criado com sucesso!")

def create_task():
    cur.execute("""
        INSERT INTO task_list (name, status) VALUES (?, ?)
    """)
    con.commit()
    return 

