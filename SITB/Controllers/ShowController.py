import services.database as db;
import models.Show as show;

def incluir(showid, showname, showdescription):
    db.cur.execute('CREATE TABLE IF NOT EXISTS show (id text, name text, description text)')

    db.cur.execute('INSERT INTO show (id, name, description) VALUES (?,?,?)',
        (showid, showname, showdescription))

    db.con.commit()

def idShow():
    if not selecionarTodos() :
        id = 'sh-1000'
        return id
    else:
        for i in db.cur.execute('SELECT id text FROM show '): 
            lastId = i[0]
        lastId = lastId.split('-')
        idNum = int(lastId[1]) + 1

        return f'sh-{idNum}'

def selecionarTodos():
    db.cur.execute('SELECT * FROM show ')
    costumerList = []

    for row in db.cur.fetchall():
        costumerList.append(show.Show(row[0],row[1],row[2]))

    return costumerList

def selecionarName():
    #db.cur.execute('SELECT name FROM show ')
    costumerList = []

    for row in db.cur.execute('SELECT * FROM show '):
        costumerList.append(row[1])

    return costumerList

def ExcluirShow(id):
    db.cur.execute('DELETE FROM show WHERE id= ?', zip(id))
    db.con.commit()

