import sqlite3

# open the connection
con = sqlite3.connect('flights.db')

cursor = con.cursor()


command1 = """CREATE TABLE IF NOT EXISTS
Flight_record(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, Flight_number TEXT,departure TEXT,destination TEXT,date TEXT,seat_number TEXT)"""

cursor.execute(command1)
con.commit()

def Count():
    cursor.execute("SELECT COUNT(*) FROM Flight_record")
    result = cursor.fetchone()  
    return result[0]

def input(nam,flight,dep,des,dae,seat):
    cursor.execute("INSERT INTO Flight_record(name,Flight_number,departure,destination,date,seat_number) VALUES (?,?,?,?,?,?)",(nam,flight,dep,des,dae,seat))
    con.commit()
    
def db_table():
    cursor.execute("SELECT * FROM Flight_record")
    out = cursor.fetchall()
    return out

def delete(index):
    cursor.execute("DELETE FROM Flight_record where id = ?",(index,))
    con.commit()
    

def delete_all():
    cursor.execute("DELETE FROM Flight_record")
    con.commit()
    
def update(index):
    # id is the id number that is associated to it by the system
    cursor.execute("SELECT * FROM Flight_record WHERE id = ?",(index,))
    o = cursor.fetchone()
    return o

def save_update(index,nam,flight,dep,des,dae,seat):
    cursor.execute("UPDATE Flight_record SET name= ?,Flight_number= ? ,departure= ? ,destination= ? ,date= ? ,seat_number= ? WHERE id = ?",(nam,flight,dep,des,dae,seat,index))
    con.commit()
