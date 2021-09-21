from project.com.dao import conDB


class UserDAO:
    def insertUser(self, userVO):
        conn = conDB()

        cursor1 = conn.cursor()

        cursor1.execute("SELECT MAX(loginId) AS loginId FROM loginmaster")

        dict1 = cursor1.fetchone()

        print(dict1)

        userVO.user_loginId = str(dict1['loginId'])


        cursor1.execute(
            "INSERT INTO usermaster(userFirstName,userLastName,userGender,userContact,user_loginId) VALUES ('" + userVO.userFirstName + "','" + userVO.userLastName + "','" + userVO.userGender + "','" + userVO.userContact + "','" + userVO.user_loginId + "')")

        conn.commit()

        cursor1.close()

        conn.close()

    def blockUnblockUser(self, userVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute(
            "update loginmaster set loginStatus = '" + userVO.loginStatus + "' where loginId='" + userVO.user_loginId + "'")
        conn.commit()
        cursor.close()
        conn.close()

    def searchUser(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select userId,userFirstName,userLastName,userGender,userContact,loginUserName,loginStatus,user_loginId from usermaster INNER JOIN loginmaster ON loginmaster.loginId = usermaster.user_loginId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data


