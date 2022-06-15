import services.database as db;

id = 'sh-2002'

id = id.split('-')
print(id[1])


def selecionarNameteste():
    #db.cur.execute('SELECT name FROM show ')
    costumerList = []

    for row in db.cur.execute('SELECT name text FROM show '):
        costumerList.append(row)

    return costumerList

print(selecionarNameteste)