import pymysql


def conDB():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass=pymysql.cursors.DictCursor
    )
