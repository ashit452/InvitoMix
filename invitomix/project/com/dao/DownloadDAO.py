from project.com.dao import conDB


class DownloadDAO:
    def addDownload(self, downloadVO):
        conn = conDB()
        cursor = conn.cursor()

        cursor.execute(
            "insert into downloadmaster(download_contentId,download_loginId) VALUES ('" + str(downloadVO.contentId) + "','" + str(downloadVO.loginId) + "')")

        conn.commit()
        cursor.close()
        conn.close()

    def searchDownload(self):
        conn = conDB()
        cursor1 = conn.cursor()

        cursor1.execute("select downloadId,contentPath,loginUserName from downloadmaster LEFT JOIN loginmaster ON loginmaster.loginId = downloadmaster.download_loginId LEFT JOIN contentmaster ON contentmaster.contentId = downloadmaster.download_contentId")

        data = cursor1.fetchall()
        cursor1.close()
        conn.close()
        return data

    def deleteDownload(self,downloadVO):
        conn = conDB()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM downloadmaster WHERE downloadId='" + downloadVO.downloadId + "' ")
        conn.commit()
        cursor.close()
        conn.close()

