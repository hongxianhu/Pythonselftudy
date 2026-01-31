import sqlite3

create_table = "CREATE TABLE"
not_null_type = "NOT NULL"
int_type = "INTEGER"
primary_key = "PRIMARY KEY"
text_type = "TEXT"
real_type = "REAL"

drop_table = "DROP TABLE"
dt = drop_table
drop_table_if_exists = "DROP TABLE EXISTS TABLE"
dtie = drop_table_if_exists


def main():
    conn = sqlite3.connect("qw.db")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE Inventory 
                    (ItemID INTEGER PRIMARY KEY NOT NULL,
                    ItemName TEXT,
                    Price REAL)"""
    )
    cur.execue(
        """INSTER INTO Inventory (ItemName,Price)
                    VALUES ('Hammer', 13.22)"""
    )
    conn.commit()
    conn.close()


def connect_db(db_name: str):
    return sqlite3.connect(db_name)


def create_tb(cur, sql_str):
    sql = create_table + f" ({sql_str})"
    cur.execute(sql)


def delete_tb(cur, table_name: str):
    cur.execute(dtie + table_name)

