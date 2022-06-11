import sqlite3


con = sqlite3.connect('SITB/data/show.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS show (id text, name text, location text, description text)')


def insertInShow(show_id, show_name, show_location, show_description):

    con = sqlite3.connect('SITB/data/show.db')
    cur = con.cursor()

    # Create table if not exist
    cur.execute('CREATE TABLE IF NOT EXISTS show (id text, name text, location text, description text)')

    cur.execute('INSERT INTO show (id, name, location, description) VALUES (?,?,?,?)',
                    (show_id, show_name, show_location, show_description))

    con.commit()


def idShow():
    for row in cur.execute('SELECT * FROM show '): 
        id = row[0]
        id = int(id) + 1
    return f'{id}'


def selecionarTodos():
    costumerList = []
    for i in cur.execute('SELECT * FROM show '):
        costumerList.append(i)

    for j in costumerList:
        costumerList.append(j)

    return costumerList

print(selecionarTodos())