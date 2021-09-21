from project.com.dao import conDB


class TemplateDAO:
    def insertTemplate(self, templateVO):
        conn = conDB()
        cursor1 = conn.cursor()
        cursor1.execute(
            "insert into templatemaster(templateName,templatePath,template_subCategoryId) VALUES ('" + templateVO.templateName + "','" + templateVO.templatePath + "','" + templateVO.subCategoryId + "')")
        conn.commit()
        cursor1.close()
        conn.close()

    def searchTemplate(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select templateId,templateName,templatePath,subCategoryName from templatemaster INNER JOIN subcategorymaster ON subcategorymaster.subCategoryId = templatemaster.template_subCategoryId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def searchUserTemplate(self, templateVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute(
            "select * from templatemaster where template_subCategoryId='" + templateVO.subCategoryId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def deleteTemplate(self,templateVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from templatemaster where templateId='" + templateVO.templateId +"'")
        conn.commit()
        cursor.close()
        conn.close()

