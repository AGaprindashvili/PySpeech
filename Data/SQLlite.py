import sqlite3

def create_actions():
    try:
        conn = sqlite3.connect("knowledge.db")
        c = conn.cursor()
        c.execute('''
        CREATE TABLE actions
        (id INTEGER PRIMARY KEY NOT NULL,
        lan INTEGER NOT NULL,
        thing TEXT NOT NULL,
        behavior TEXT NOT NULL,
        created DATETIME NOT NULL,
        enabled BOOLEAN NOT NULL)
        ''')
        c.close()
        conn.close()
        print("Table created successfully")
    except Exception as e:
        print(e)

def insert_actions():
    try:
        conn = sqlite3.connect("knowledge.db")
        c = conn.cursor()
        c.execute('''
        INSERT INTO actions (lan, thing, behavior, created, enabled) VALUES (1, 'thing', 'behavior', datetime('now'), 1)
        ''')
        conn.commit()
        c.close()
        conn.close()
        print("Inserted successfully")
    except Exception as e:
        print(e)

def delete_actions():
    try:
        conn = sqlite3.connect("knowledge.db")
        c = conn.cursor()
        c.execute('''
        DELETE FROM actions
        ''')
        conn.commit()
        c.close()
        conn.close()
        print("Deleted successfully")
    except Exception as e:
        print(e)

def select_actions():
    try:
        conn = sqlite3.connect("knowledge.db")
        c = conn.cursor()
        result = c.execute('''
        SELECT id, lan, thing, behavior, created, enabled FROM actions
        ''').fetchall()
        for row in result:
            print("id: "        + str(row[0]))
            print("lan: "       + str(row[1]))
            print("thing: "     + str(row[2]))
            print("behavior: "  + str(row[3]))
            print("created: "   + str(row[4]))
            print("enabled: "   + str(row[5]))
        c.close()
        conn.close()
    except Exception as e:
        print(e)

#create_actions()
#insert_actions()
#delete_actions()
select_actions()