import services.database as db;
import models.Teatro as teatro;

def incluir(teatroid, teatroname, teatrocapacity):
    db.cur.execute('CREATE TABLE IF NOT EXISTS teatro (id text, name text, capacity real)')

    db.cur.execute('INSERT INTO show (id, name, capacity) VALUES (?,?,?)',
        (teatroid, teatroname, teatrocapacity))

    db.con.commit()

def idTeatro():
    if not selecionarTodos() :
        id = 'te-1000'
        return id
    else:
        for i in db.cur.execute('SELECT id text FROM teatro '): 
            lastId = i[0]
        lastId = lastId.split('-')
        idNum = int(lastId[1]) + 1

        return f'te-{idNum}'

def selecionarTodos():
    db.cur.execute('SELECT * FROM teatro ')
    costumerList = []

    for row in db.cur.fetchall():
        costumerList.append(teatro.Teatro(row[0],row[1],row[2]))

    return costumerList