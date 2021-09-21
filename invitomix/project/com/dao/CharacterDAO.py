from project.com.dao import conDB


class CharacterDAO:
    def insertCharacter(self, characterVO):
        conn = conDB()
        cursor1 = conn.cursor()
        cursor1.execute(
            "insert into charactermaster(characterName,characterPath,character_subCategoryId) VALUES ('" + characterVO.characterName + "','" + characterVO.characterPath + "','" + characterVO.subCategoryId + "')")
        conn.commit()
        cursor1.close()
        conn.close()

    def searchCharacter(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select characterId,subCategoryName,characterName,characterPath from charactermaster INNER JOIN subcategorymaster ON subcategorymaster.subCategoryId = charactermaster.character_subCategoryId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def searchUserCharacter(self,characterVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from charactermaster where character_subCategoryId='" + characterVO.subCategoryId + "'")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def deleteCharacter(self,characterVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from charactermaster where characterId='" + characterVO.characterId +"' ")
        conn.commit()
        cursor.close()
        conn.close()

