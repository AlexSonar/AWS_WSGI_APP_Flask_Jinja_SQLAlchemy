import sqlite3
 
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
            print("Ошибка чтения из БД")
        return [{"name": "test"
        , "url": "test"}]