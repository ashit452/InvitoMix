from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.DownloadVO import DownloadVO
from project.com.dao.DownloadDAO import DownloadDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession
from project.com.controller.ContentController import userLoadContent


@app.route('/user/insertDownload', methods=['get', 'post'])
def userInsertDownload():
    try:
        if adminLoginSession() == 'user':
            downloadVO = DownloadVO()
            downloadVO.contentId = request.form['contentId']
            print(downloadVO.contentId)
            downloadVO.loginId = session['session_loginId']
            print(downloadVO.loginId)
    
            downloadDAO = DownloadDAO()
    
            downloadDAO.addDownload(downloadVO)
    
            return userLoadContent()
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewDownload')
def adminViewDownload():
    try:
        if adminLoginSession() == 'admin':
            downloadDAO = DownloadDAO()
            data = downloadDAO.searchDownload()
            print(data)
            return render_template("admin/viewDownload.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteDownload')
def adminDeleteDownload():
    try:
        if adminLoginSession() == 'admin':
            downloadVO = DownloadVO()
            downloadVO.downloadId = request.args.get('downloadId')
            downloadDAO = DownloadDAO()
            downloadDAO.deleteDownload(downloadVO)

            return redirect(url_for("adminViewDownload"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

