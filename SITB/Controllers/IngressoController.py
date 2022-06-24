import services.database as db;
import models.Ingresso as ingresso;

def criar():
    db.cur.execute('CREATE TABLE IF NOT EXISTS ingresso (id text, sessao text, informacao text, datetime text)')


def incluir(id, sessao, informacao, datetime):
    db.cur.execute('CREATE TABLE IF NOT EXISTS ingresso (id text, sessao text, informacao text, datetime text)')

    db.cur.execute('INSERT INTO ingresso (id, sessao, informacao, datetime) VALUES (?,?,?,?)',
        (id, sessao, informacao, datetime))

    db.con.commit()

def idShow():
    if not selecionarTodos() :
        id = 'in-1000'
        return id
    else:
        for i in db.cur.execute('SELECT id text FROM ingresso '): 
            lastId = i[0]
        lastId = lastId.split('-')
        idNum = int(lastId[1]) + 1

        return f'in-{idNum}'

def selecionarTodos():
    db.cur.execute('SELECT * FROM ingresso ')
    costumerList = []

    for row in db.cur.fetchall():
        costumerList.append(ingresso.Ingresso(row[0],row[1],row[2],row[3]))

    return costumerList

def informecoes(id):
    a = db.cur.execute("SELECT * FROM sessao WHERE id=? ", [id])
    costumerList = []

    for row in db.cur.fetchall():
        costumerList.append(ingresso.Ingresso(row[1]+'',row[2],row[3],))
    
    return a

def teste(id):

    for row in db.cur.execute("SELECT * FROM show WHERE id=? ", [id]):
        a = row

    return  a

    