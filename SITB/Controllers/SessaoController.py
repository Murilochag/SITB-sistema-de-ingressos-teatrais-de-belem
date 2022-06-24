import services.database as db;
import models.Sessao as sessao;

def criar():
    db.cur.execute('CREATE TABLE IF NOT EXISTS sessao (id text, teatro text, show text, data text, hora text)')


def incluir(id, teatro, show , data, hora):
    db.cur.execute('CREATE TABLE IF NOT EXISTS sessao (id text, teatro text, show text, data text, hora text)')

    db.cur.execute('INSERT INTO sessao (id, teatro, show , data, hora) VALUES (?,?,?,?,?)',
        (str(id), str(teatro), str(show) , str(data), str(hora)))

    db.con.commit()

def idSessao():
    if not selecionarTodos() :
        id = 'ss-1000'
        return id
    else:
        for i in db.cur.execute('SELECT id FROM sessao'): 
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
    for row in db.cur.execute('SELECT * FROM sessao '):
        idList.append(row[0])

def ExcluirSessao(id):
    db.cur.execute("DELETE FROM sessao WHERE id=? ", [id])
    db.con.commit()

def getSessao():
    sessList = []
    for row in db.cur.execute('SELECT * FROM sessao '):
        sessList.append(row[0] +'; '+ row[1]+'; '+row[2] +'; '+ row[3]+'; '+row[4])
    return sessList




# get informções:
def getId(id):
    idarr = id.split(',')
    returnId = idarr[0]
    return str(returnId)

def getTestroById(id):
    id = getId(id)
    for row in db.cur.execute("SELECT * FROM sessao WHERE id=? ", [id]):
        a = row[1]
        return  str(a)

def getShowById(id):
    id = getId(id)
    for row in db.cur.execute("SELECT * FROM sessao WHERE id=? ", [id]):
        a = row[2]
        return  str(a)

def getDataById(id):
    id = getId(id)
    for row in db.cur.execute("SELECT * FROM sessao WHERE id=? ", [id]):
        teatro = row[3]
        return  str(teatro)

def getHoraById(id):
    id = getId(id)
    for row in db.cur.execute("SELECT * FROM sessao WHERE id=? ", [id]):
        teatro = row[4]
        return  str(teatro)
