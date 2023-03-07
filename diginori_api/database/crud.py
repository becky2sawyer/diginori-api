import pandas as pd
import sqlite3
import json


def select(sql, db="sqllite.db") -> list:
    con = sqlite3.connect(db)
    df = pd.read_sql_query(sql, con)
    df_list = json.loads(df.reset_index().to_json(orient='records'))
    con.close()
    return df_list

