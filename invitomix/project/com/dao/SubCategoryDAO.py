from project.com.dao import conDB


class SubCategoryDAO:
    def insertSubCategory(self, subCategoryVO):
        conn = conDB()
        cursor1 = conn.cursor()
        cursor1.execute(
            "insert into subcategorymaster(subCategoryName,subCategoryDescription,subCategory_categoryId) VALUES ('" + subCategoryVO.subCategoryName + "','" + subCategoryVO.subCategoryDescription + "','" + subCategoryVO.subCategory_categoryId + "')")
        conn.commit()
        cursor1.close()
        conn.close()

    def searchSubCategory(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select subCategoryId,categoryName,subCategoryName,subCategoryDescription from subcategorymaster INNER JOIN categorymaster ON categorymaster.categoryId = subcategorymaster.subCategory_categoryId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def searchUserSubCategory(self,subCategoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from subcategorymaster where subCategory_categoryId='" + subCategoryVO.subCategory_categoryId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def deleteSubCategory(self,subCategoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from subcategorymaster where subCategoryId='" + subCategoryVO.subCategoryId +"' ")
        conn.commit()
        cursor.close()
        conn.close()

    def editSubCategory(self,subCategoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from subcategorymaster where subCategoryId='" + subCategoryVO.subCategoryId + "'")
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def updateSubCategory(self,subCategoryVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("update subcategorymaster set subCategoryName = '" + subCategoryVO.subCategoryName + "' , subCategoryDescription = '" + subCategoryVO.subCategoryDescription + "', subCategory_categoryId = '" + subCategoryVO.subCategory_categoryId + "' where subCategoryId='" + subCategoryVO.subCategoryId + "'")
        conn.commit()
        cursor.close()
        conn.close()
