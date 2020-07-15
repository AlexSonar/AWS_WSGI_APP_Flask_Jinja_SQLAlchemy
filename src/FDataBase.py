import sqlite3
import time
import math
import re
from flask import url_for
 
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
    

    def addPost(self, title, text, url):
        try:

            # checking for uniqueness
            self.__cur.execute("SELECT COUNT() as `count` FROM posts WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("This url already exists")
                return False

            # data/images images_html
            base = url_for('static', filename=('data/images/'+url))
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
                          "\\g<tag>"+base+"/\\g<url>>",
                          text)

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, tm, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Eror insert to DB "+str(e))
            return False
 
        return True


    # def getPost(self, postId):
    # self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {postId} LIMIT 1")
    def getPost(self, alias_post):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE url LIKE '{alias_post}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД "+str(e))
 
        return (False, False)   



    def getPostsAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text, url FROM posts ORDER BY time DESC  LIMIT 7")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД "+str(e))
 
        return []