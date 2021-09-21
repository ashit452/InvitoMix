from project.com.dao import conDB


class CategoryDAO:
    def insertCategory(self,categoryVO):
        conn = conDB()
        cursor = conn.cursor()

        cursor.execute(
            "insert into categorymaster(categoryName,categoryDescription) VALUES ('" + categoryVO.categoryName + "','" + categoryVO.categoryDescription + "')")

        conn.commit()
        cursor.close()
        conn.close()

    def searchCategory(self):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from categorymaster")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data



    def deleteCategory(self,categoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from categorymaster where categoryId='"+categoryVO.categoryId +"'")
        conn.commit()
        cursor.close()
        conn.close()

    def editCategory(self,categoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from categorymaster where categoryId='" + categoryVO.categoryId + "'")
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def updateCategory(self,categoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("update categorymaster set categoryName = '" + categoryVO.categoryName + "', categoryDescription = '" + categoryVO.categoryDescription + "' where categoryId='" + categoryVO.categoryId + "'")
        conn.commit()
        cursor.close()
        conn.close()
