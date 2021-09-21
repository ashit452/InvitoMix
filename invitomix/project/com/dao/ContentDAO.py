from project.com.dao import conDB


class ContentDAO:
    def insertContent(self,contentVO):
        conn = conDB()
        cursor = conn.cursor()

        cursor.execute(
            "insert into contentmaster(content_categoryId,contentPath,content_loginId) VALUES ('" + str(contentVO.categoryId) + "','" + contentVO.contentPath + "','" + str(contentVO.loginId) + "')")

        conn.commit()
        cursor.close()
        conn.close()

    def searchUserContent(self,contentVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from contentmaster where content_loginId='" + str(contentVO.loginId) + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def searchContent(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select contentId,contentPath,loginUserName,categoryName from contentmaster LEFT JOIN loginmaster ON loginmaster.loginId = contentmaster.content_loginId LEFT JOIN categorymaster ON categorymaster.categoryId = contentmaster.content_categoryId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def deleteContent(self,contentVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from contentmaster where contentId='" + contentVO.contentId +"' ")
        conn.commit()
        cursor.close()
        conn.close()

