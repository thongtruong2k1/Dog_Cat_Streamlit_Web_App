import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def insert_data(conn,obj):
  #obj=(path,detail)
  query=''' INSERT INTO dogcats (path,detail) VALUES(?,?)'''
  c = conn.cursor()
  c.execute(query,obj)
  conn.commit()
  
def update_data(conn,obj):
  #obj=(path,detail,id)
  query = ''' UPDATE dogcats SET path = ? ,detail = ? WHERE id = ?'''
  c = conn.cursor()
  c.execute(query, obj)
  conn.commit()