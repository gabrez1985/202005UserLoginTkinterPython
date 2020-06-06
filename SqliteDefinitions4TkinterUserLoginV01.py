import sqlite3
import datetime


# CREATE TABLE se debe poner con 3 " al comienzo y 3 " al final,
# si no existe el archivo lo crea
# slqlite data types: text, real, integer, boolean, blop (files, images, etc.)

# --------------- DEFINICIONES USERSPASSWORD TABLE ---------------
def createuserspasswordtable():
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE userspassword (
        username TEXT PRIMARY KEY,
        userpassword TEXT
        )""")
    conn.commit()
    conn.close()


# Entre las comillas se pone el comando SQL, despues se separa con coma
# todas las variables y se ponen entre corchetes,
# y todo el comando de Python se pone entre parentesis
def insertnewuserpassword(user, password):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("INSERT INTO userspassword VALUES (:value1,:value2)",
              {
                'value1': user,
                'value2': password,
              })
    conn.commit()
    conn.close()


def updateuserinfo(user, password):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("""UPDATE userspassword
    SET username = :value1, userpassword = :value2
    WHERE username = :value1""",
              {
                'value1': user,
                'value2': password
              })
    conn.commit()
    conn.close()


def queryuserpassword(user):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("SELECT userpassword FROM userspassword WHERE username=:value1", {'value1': user})
    password = c.fetchall()[0][0]
    conn.commit()
    conn.close()
    return password


# --------------- DEFINICIONES USERSFILES TABLE ---------------
def createusersfilestable():
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE usersfiles (
        username TEXT,
        userfilename TEXT,
        userfiledetails TEXT,
        PRIMARY KEY (username, userfilename)
        )""")
    conn.commit()
    conn.close()


def insertusernewfile(user, filename, filedetails):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("INSERT INTO usersfiles VALUES (:value1,:value2,:value3)",
              {
                'value1': user,
                'value2': filename,
                'value3': filedetails
              })
    conn.commit()
    conn.close()


def updateuserfile(user, filename, filedetails):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("""UPDATE usersfiles
    SET userfiledetails = :value3
    WHERE username = :value1 AND userfilename = :value2 """,
              {
                'value1': user,
                'value2': filename,
                'value3': filedetails
              })
    conn.commit()
    conn.close()


def deleteuserfile(user, filename):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("""DELETE FROM usersfiles
    WHERE username=:value1 AND userfilename=:value2""", {'value1': user, 'value2': filename})
    conn.commit()
    conn.close()


def queryuserfiles(user):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("SELECT userfilename FROM usersfiles WHERE username=:value1", {'value1': user})
    userfiles = c.fetchall()
    conn.commit()
    conn.close()
    return userfiles


def queryuserfiledetails(user, filename):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("SELECT userfiledetails FROM usersfiles WHERE username=:value1 AND userfilename=:value2",
              {
                'value1': user, 'value2': filename
              })
    userfiles = c.fetchall()
    conn.commit()
    conn.close()
    return userfiles


# --------------- DEFINICIONES USERSLOGINTIMES TABLE ---------------
# cuando ID se define como INTERGER y PRIMARY KEY Python y sqlite3
# lo reconocen como AUTO INCREMENT
def createuserslogintimestable():
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE userslogintimes (
        ID INTEGER PRIMARY KEY,
        username TEXT,
        eventype TEXT,
        eventdetails TEXT,
        timedate TEXT
        )""")
    conn.commit()
    conn.close()


# no se debe pasar el ID ya que este es un correlativo y se debe generar solo
def insertusernewtimelog(user, eventtype, eventdetails):
    currentdatetime = datetime.datetime.today()
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("INSERT INTO userslogintimes (username, eventype, eventdetails, timedate) VALUES (:value1,:value2,:value3,:value4)",
              {
                'value1': user,
                'value2': eventtype,
                'value3': eventdetails,
                'value4': currentdatetime
              })
    conn.commit()
    conn.close()


def queryuserhistoriclogs(user):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM userslogintimes WHERE username=:value1",
              {
                'value1': user
              })
    userhistoriclogs = c.fetchall()
    conn.commit()
    conn.close()
    return userhistoriclogs


# --------------- TABLAS EN BASE DE DATOS E INFO TABLAS ---------------
def databasetables():
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablasinfo = c.fetchall()
    conn.commit()
    conn.close()
    return(tablasinfo)


# para mantener como variable el nombre de la tabla se puede pasar el query
# ya armado con la variable dentro, en c.execute()
def querycompletetable(tablename):
    conn = sqlite3.connect('UserDataBase.db')
    c = conn.cursor()
    query = "SELECT * FROM " + tablename
    c.execute(query)
    tableinfo = c.fetchall()
    conn.commit()
    conn.close()
    return tableinfo
