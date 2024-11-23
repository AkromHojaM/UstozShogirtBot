import sqlite3




def con():
    return sqlite3.connect("IshJoy")

def create_table():
    try:
        conn = con()
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS UstozShogirt
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        fullName VARCHAR(70),
        phone INTEGER UNIQUE,
        ish VARCHAR(30),
        texnologiya TEXT,
        age INTEGER,
        description TEXT,
        price INTEGER,
        free_time VARCHAR,
        country VARCHAR(30),
        telegram_accaount VARCHAR(50))""")

        conn.commit()
    except sqlite3.Error as e:
        print(f"Failed to create tables {e}")

    finally:conn.close()


def create_table2():
    try:
        conn = con()
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Hodim
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        idora_name VARCHAR(50),
        fullname VARCHAR(70),
        phone INTEGER UNIQUE,
        texnologiya TEXT,
        description TEXT,
        price INTEGER,
        free_time VARCHAR(30),
        ish_vaqti VARCHAR(30),
        country VARCHAR(30),
        telegram_accaount VARCHAR(50))""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Failed to create tables {e}")

    finally:conn.close()

def insert_database(user_id,fullname,phone,ish,texnologiya,age,description,price,free_time,country,telegram_account):
        conn = con()
        cur = conn.cursor()
        cur.execute("INSERT INTO UstozShogirt(user_id,fullName,phone,ish,texnologiya,age,description,price,free_time,country,telegram_accaount) values (?,?,?,?,?,?,?,?,?,?,?)",(user_id,fullname,phone,ish,texnologiya,age,description,price,free_time,country,telegram_account))
        conn.commit()


def insert_database2(user_id,idora_name,fullname,phone,texnologiya,description,price,free_time,ish_vaqti,country,telegram_accaount):
        conn = con()
        cur = conn.cursor()
        cur.execute("INSERT INTO Hodim(user_id,idora_name,fullname,phone,texnologiya,description,price,free_time,ish_vaqti,country,telegram_accaount) values (?,?,?,?,?,?,?,?,?,?,?)",(user_id,idora_name,fullname,phone,texnologiya,description,price,free_time,ish_vaqti,country,telegram_accaount))
        conn.commit()


def select(user_id):
    try:
        conn = con()
        cur = conn.cursor()
        cur.execute("SELECT * FROM UstozShogirt where user_id=?",(user_id,))
        conn.commit()
        return cur.fetchall()
    except Exception as e:
        raise f"Error insert {e}"


def select2():
        conn = con()
        cur = conn.cursor()
        cur.execute("Select * From UstozShogirt")
        conn.commit()
        return cur.fetchall()
con()

create_table()
create_table2()