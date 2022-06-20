import services.database as db;
import models.Sessao as sessao;

def criar():
    db.cur.execute('CREATE TABLE IF NOT EXISTS sessao (id text, name text, capacity real)')


def incluir(id, teatro, show , data, hora):
    db.cur.execute('CREATE TABLE IF NOT EXISTS sessao (id text, teatro text, show text, data text, hora text)')

    db.cur.execute('INSERT INTO sessao (id, teatro, show , data, hora) VALUES (?,?,?,?,?)',
        (id, teatro, show , data, hora))

    db.con.commit()

def idTeatro():
    if not selecionarTodos() :
        id = 'ss-1000'
        return id
    else:
        for i in db.cur.execute('SELECT id text sessao teatro '): 
            lastId = i[0]
        lastId = lastId.split('-')
        idNum = int(lastId[1]) + 1

        return f'ss-{idNum}'

def selecionarTodos():
    db.cur.execute('SELECT * FROM sessao ')
    costumerList = []

    for row in db.cur.fetchall():
        costumerList.append(sessao.Sessao(row[0],row[1],row[2],row[3],row[4]))

    return costumerList

def selecionarId():
    idList = []
    for row in db.cur.execute('SELECT * FROM show '):
        idList.append(row[0])

def ExcluirSessao(id):
    db.cur.execute("DELETE FROM teatro WHERE id=? ", [id])
    db.con.commit()