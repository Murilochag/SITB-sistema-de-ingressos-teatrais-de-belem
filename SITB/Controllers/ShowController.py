import services.database as db;
import models.Show as show;

def incluir(showname, showlocation, showdescription):
    db.cur.execute('CREATE TABLE IF NOT EXISTS show (name text, location text, description text)')

    db.cur.execute('INSERT INTO show (name, location, description) VALUES (?,?,?)',
        (showname, showlocation, showdescription))

    db.con.commit()

def idShow():
    for i in db.cur.execute('SELECT * FROM show '): 
        id = i[0]
        id = int(id) + 1
    return f'{id}'

def selecionarTodos():
    db.cur.execute('SELECT * FROM show ')
    costumerList = []

    for row in db.cur.fetchall():
        costumerList.append(show.Show(row[0],row[1],row[2]))

    return costumerList