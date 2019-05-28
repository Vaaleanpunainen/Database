import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_values(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    # before filling database:
    # cur.execute("INSERT INTO store VALUES ('Wine',50,25)")
    # after filling the first line of database:
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

# after filling the first line of database:
# insert_values("Cofee",250,8)
# then change into:
# insert_values("Water",500,2.5)
# executed two times by mistake

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
