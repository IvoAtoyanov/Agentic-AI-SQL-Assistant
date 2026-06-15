import sqlite3

DB="shop.db"


def execute_query(sql):

    conn=sqlite3.connect(DB)

    cur=conn.cursor()

    cur.execute(sql)

    rows=cur.fetchall()

    columns=[]

    if cur.description:

        columns=[

        d[0]

        for d

        in cur.description

        ]

    conn.close()

    return rows,columns
