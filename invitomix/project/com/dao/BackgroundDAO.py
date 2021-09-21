from project.com.dao import conDB


class BackgroundDAO:
    def insertBackground(self, backgroundVO):
        conn = conDB()
        cursor1 = conn.cursor()
        cursor1.execute(
            "insert into backgroundmaster(backgroundName,backgroundPath,background_subCategoryId) VALUES ('" + backgroundVO.backgroundName + "','" + backgroundVO.backgroundPath + "','" + backgroundVO.subCategoryId + "')")
        conn.commit()
        cursor1.close()
        conn.close()

    def searchBackground(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select backgroundId,subCategoryName,backgroundName,backgroundPath from backgroundmaster INNER JOIN subcategorymaster ON subcategorymaster.subCategoryId = backgroundmaster.background_subCategoryId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def searchUserBackground(self,backgroundVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from backgroundmaster where background_subCategoryId='" + backgroundVO.subCategoryId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def deleteBackground(self,backgroundVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from backgroundmaster where backgroundId='" + backgroundVO.backgroundId +"' ")
        conn.commit()
        cursor.close()
        conn.close()

