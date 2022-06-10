import sqlite3


# con = sqlite3.connect('show.db')
# cur = con.cursor()

# Create table 
# cur.execute('CREATE TABLE IF NOT EXISTS show (id text, name text, location text)')

# Insert a row of data

def insertInShow(show_id, show_name, show_location):

    con = sqlite3.connect('show.db')
    cur = con.cursor()

    # Create table
    cur.execute('CREATE TABLE IF NOT EXISTS show (id text, name text, location text)')

    cur.execute('INSERT INTO show (id, name, location) VALUES (?,?,?)',
                    (show_id, show_name, show_location))

    con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

#insertInShow('01','o fantasma da ópera,','teatro da paz')

#for row in cur.execute('SELECT * FROM show '):
        #print(row)

