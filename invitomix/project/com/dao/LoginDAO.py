from project.com.dao import conDB


class LoginDAO:
    def insertLogin(self, loginVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute(
            "insert into loginmaster(loginUserName,loginPassword,loginRole,loginStatus) values ('" + loginVO.loginUserName + "','" + loginVO.loginPassword + "','" + loginVO.loginRole + "','" + loginVO.loginStatus + "')")

        conn.commit()

        cursor1.close()

        conn.close()

    def validateLogin(self, loginVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute(
            "SELECT * FROM loginmaster WHERE loginUserName='" + loginVO.loginUserName + "' AND loginPassword='" + loginVO.loginPassword + "'")

        dict1 = cursor1.fetchall()

        cursor1.close()

        conn.close()

        return dict1

    def checkUserName(self, loginVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute(
            "SELECT * FROM loginmaster WHERE loginUserName='" + loginVO.loginUserName + "' ")

        dict1 = cursor1.fetchall()

        cursor1.close()

        conn.close()

        return dict1

    def showUserName(self, loginVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute(
            "SELECT * FROM usermaster WHERE user_loginId='" + loginVO.loginId + "' ")

        dict1 = cursor1.fetchall()

        cursor1.close()

        conn.close()

        return dict1

    def updatePassword(self, loginVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute(
            "update loginmaster set loginPassword='{}' where loginId='{}'".format(loginVO.loginPassword,
                                                                                  loginVO.loginId))

        conn.commit()

        cursor1.close()

        conn.close()

    def checkUserEmail(self, loginVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute(
            "SELECT * FROM loginmaster WHERE loginId='" + str(loginVO.loginId) + "' ")

        dict1 = cursor1.fetchall()

        cursor1.close()

        conn.close()

        return dict1

