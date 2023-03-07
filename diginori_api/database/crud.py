import pandas as pd
import sqlite3
import json


def select(sql, db="sqllite.db") -> list:
    con = sqlite3.connect(db)
    df = pd.read_sql_query(sql, con)
    df_list = json.loads(df.reset_index().to_json(orient='records'))
    con.close()
    return df_list


def insert_config(id: int, name: str, config: str, db="sqllite.db") -> bool:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(f"""
        insert into test (id, name, config)
        values ({id}, '{name}', '{config}');
    """)
    con.commit()
    con.close()
    return True


def insert_name_card(name: str, age: int, db="sqllite.db") -> bool:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(f"""
            insert into name_card (name, age)
            values ('{name}', {age});
        """)
    con.commit()
    con.close()
    return True
