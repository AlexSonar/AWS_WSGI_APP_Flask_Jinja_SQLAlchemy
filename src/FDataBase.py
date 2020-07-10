import sqlite3
import time
import math
 
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
 
    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            # print("test_1", str(res))  <sqlite3.Row object at 0x7f3eb7e9e9f0>, <sqlite3.Row object at 0x7f3eb7e9e7f0>
            if res: return res
        except:
            print("Eror readind from DB")
        return []  
        # return [{"name": "test"
        # , "url": "test"}]
    

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Eror insert to DB "+str(e))
            return False
 
        return True