from project.com.dao import conDB


class SuggestionDAO:
    def insertSuggestion(self, suggestionVO):
        conn = conDB()
        cursor1 = conn.cursor()
        cursor1.execute(
            "insert into suggestionmaster(suggestionSubject,suggestionDescription,suggestionFile,suggestionDate,suggestionTime,suggestion_loginId,suggestionStatus) VALUES ('" + suggestionVO.suggestionSubject + "','" + suggestionVO.suggestionDescription + "','" + suggestionVO.suggestionFile + "','" + suggestionVO.suggestionDate + "','" + suggestionVO.suggestionTime + "','" + suggestionVO.loginId + "','" + suggestionVO.suggestionStatus + "')")
        conn.commit()
        cursor1.close()
        conn.close()

    def searchSuggestion(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select suggestionId,suggestionSubject,loginUserName,suggestionFile,suggestionDescription,suggestionDate,suggestionTime,suggestionReply,suggestionStatus,suggestion_loginId from suggestionmaster INNER JOIN loginmaster ON loginmaster.loginId = suggestionmaster.suggestion_loginId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def deleteSuggestion(self,suggestionVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from suggestionmaster where suggestionId='" + suggestionVO.suggestionId +"' ")
        conn.commit()
        cursor.close()
        conn.close()

    def replySuggestion(self,suggestionVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("select * from suggestionmaster where suggestionId='" + suggestionVO.suggestionId + "'")
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def updateSuggestion(self,suggestionVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("update suggestionmaster set suggestionReply = '" + suggestionVO.suggestionReply + "', suggestionStatus = '" + suggestionVO.suggestionStatus + "' where suggestionId='" + suggestionVO.suggestionId + "'")
        conn.commit()
        cursor.close()
        conn.close()
