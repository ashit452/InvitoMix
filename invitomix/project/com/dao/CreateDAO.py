from project.com.dao import conDB


class CreateDAO:

    def searchCreateBackground(self, createVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute(
            "select * from backgroundmaster where backgroundId ='" + createVO.backgroundId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def searchCreateCharacter(self, createVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute(
            "select * from charactermaster where characterId ='" + createVO.characterId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def searchCreateTemplate(self, createVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute(
            "select * from templatemaster where templateId ='" + createVO.templateId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

