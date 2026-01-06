import sqlite3

con = sqlite3.connect("to_do.db")
cur = con.cursor()

#status = 0 [Não feita], 1 [feita]
def initialize_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS task_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            status INTEGER DEFAULT 0 NOT NULL
        )
    """)

def create_task(name, status = 0):
    sql = """ INSERT INTO task_list (name, status) VALUES (?, ?) """
    cur.execute(sql,(name,status))
    con.commit()

    return cur.lastrowid

def show_all_tasks():
    for row in cur.execute("""SELECT id, name, status FROM task_list"""):    
        print(row)
        
def delete_task(id):
    sql = """ DELETE FROM task_list WHERE id = (?) """
    cur.execute(sql,[id])
    con.commit()
    print("A tarefa " + str(id) + " foi deletada")

def change_task_status(id):
    sql = """ UPDATE task_list SET status = 1 WHERE id = (?) """
    cur.execute(sql,[id])
    con.commit()
    print("A tarefa " + str(id) + " foi concluída")
    


