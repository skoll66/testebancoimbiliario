import sqlite3

tb_name = 'propriedade'
tb_name_jogador = 'jogador'

def UpdateJogador(id,saldo):
    try:
        conn = sqlite3.connect('prop_banco.db')
        cursor = conn.cursor()
        sqlUpdate = "UPDATE {} SET saldo = {} WHERE id = {};".format(tb_name_jogador,saldo,id)
        cursor.execute(sqlUpdate)
        conn.commit()
        conn.close()
    except Exception as err:
        print (err)

def UpdateJogadorpos(id,posicaofim):
    try:
        conn = sqlite3.connect('prop_banco.db')
        cursor = conn.cursor()
        sqlUpdate = "UPDATE {} SET pos ={} WHERE id = {};".format(tb_name_jogador,posicaofim,id)
        cursor.execute(sqlUpdate)
        conn.commit()
        conn.close()
    except Exception as err:
        print (err)

def UpdatePropriedade(idPro,idJogador,dono):
    try:
        conn = sqlite3.connect('prop_banco.db')
        cursor = conn.cursor()
        sqlUpdate = "UPDATE {} SET jogador = {}, dono ={} WHERE id = {};".format(tb_name,idJogador,dono,idPro)
        cursor.execute(sqlUpdate)
        conn.commit()
        conn.close()
    except Exception as err:
        print (err)

def UpdatePropriedadedevolvida(idJogador,dono):
    try:
        conn = sqlite3.connect('prop_banco.db')
        cursor = conn.cursor()
        sqlUpdate = "UPDATE {} SET dono = {} WHERE jogador = {};".format(tb_name,dono,idJogador)
        cursor.execute(sqlUpdate)
        conn.commit()
        conn.close()
    except Exception as err:
        print (err)

def selectProp(id):
    conn = sqlite3.connect('prop_banco.db')
    cursor = conn.cursor()
    try:
        sql = 'SELECT * FROM propriedade where id = {}  ORDER BY id'.format(id)
        e = cursor.execute(sql)
        dados = e.fetchall()
        conn.close()
        return dados
    except Exception as err:
        print (err)
def selectJogador(Nome):
    conn = sqlite3.connect('prop_banco.db')
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM jogador where Nome = '{}'".format(Nome)
        e = cursor.execute(sql)
        dados = e.fetchall()
        conn.close()
        return dados
    except Exception as err:
        print (err)
def selectLocador(id):
    conn = sqlite3.connect('prop_banco.db')
    cursor = conn.cursor()
    try:
        sql = "SELECT * FROM jogador where id = '{}'".format(id)
        e = cursor.execute(sql)
        dados = e.fetchall()
        conn.close()
        return dados
    except Exception as err:
        print (err)

def insertProp(dicProp):
    try:
        conn = sqlite3.connect('prop_banco.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO propriedade (Nome, Valor,Aluguel, dono) VALUES ('{}',{},{} ,{})""".format(dicProp["Nome"], dicProp["Valor"],dicProp["Aluguel"], dicProp["dono"]))
            conn.commit()
        except sqlite3.Error as e:
            if 'no such table: propriedade' in str(e):
                sqlCreate = ("""CREATE TABLE {} (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Nome TEXT NOT NULL,
                        Valor INTEGER,
                        Aluguel INTEGER,
                        jogador INTEGER, 
                        dono booleano    ); """).format(tb_name)
                cursor.execute(sqlCreate)
                cursor.execute("""INSERT INTO propriedade (Nome,Valor,Aluguel,dono) VALUES ('{}',{} ,{},{})""".format(dicProp["Nome"], dicProp["Valor"], dicProp["Aluguel"],dicProp["dono"]))
                conn.commit()

        conn.close()
    except Exception as err:
        print (err)
def insertJogador(dicjogador):

    conn = sqlite3.connect('prop_banco.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO jogador (Nome, pos,saldo) VALUES ('{}',{} ,{})""".format(dicjogador["Nome"], dicjogador["pos"], dicjogador["Saldo"]))
        conn.commit()
    except sqlite3.Error as e:
        if 'no such table: jogador' in str(e):
            sqlCreate = ("""CREATE TABLE {} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    pos INTEGER,
                    saldo INTEGER); """).format(tb_name_jogador)
            cursor.execute(sqlCreate)
            cursor.execute("""INSERT INTO jogador (Nome, pos,saldo) VALUES ('{}',{} ,{})""".format(dicjogador["Nome"], dicjogador["pos"], dicjogador["Saldo"]))
            conn.commit()

    conn.close()
def deleteJogador(id):
    try:
        conn = sqlite3.connect('prop_banco.db')
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM jogador WHERE id = {}""".format(id))
        conn.commit()
    except Exception as err:
        print(err)


def delete():
    conn = sqlite3.connect('prop_banco.db')
    cursor = conn.cursor()
    cursor.execute("""drop table propriedade""")
    conn.commit()
    cursor.execute("""drop table jogador""")
    conn.close()
