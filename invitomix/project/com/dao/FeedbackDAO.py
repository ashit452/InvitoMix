from project.com.dao import conDB


class FeedbackDAO:
    def insertFeedback(self,feedbackVO):
        conn = conDB()
        cursor = conn.cursor()

        cursor.execute(
            "insert into feedbackmaster(feedbackSubject,feedbackDescription,feedbackRatings,feedbackDate,feedbackTime,feedback_loginId) VALUES ('" + feedbackVO.feedbackSubject + "','" + feedbackVO.feedbackDescription + "','" + feedbackVO.feedbackRatings + "','" + feedbackVO.feedbackDate + "','" + feedbackVO.feedbackTime + "','" + feedbackVO.loginId + "')")

        conn.commit()
        cursor.close()
        conn.close()

    def searchFeedback(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select feedbackId,loginUserName,feedbackSubject,feedbackDescription,feedbackDate,feedbackTime,feedbackRatings from feedbackmaster INNER JOIN loginmaster ON loginmaster.loginId = feedbackmaster.feedback_loginId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def deleteFeedback(self,feedbackVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("delete from feedbackmaster where feedbackId='" + feedbackVO.feedbackId +"'")
        conn.commit()
        cursor.close()
        conn.close()

