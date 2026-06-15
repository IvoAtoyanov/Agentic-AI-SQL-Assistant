import sqlite3
DB='shop.db'

def execute_query(sql):
    conn=sqlite3.connect(DB)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    cols=[d[0] for d in cur.description] if cur.description else []
    conn.close()
    return rows,cols
