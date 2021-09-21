from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.ContentVO import ContentVO
from project.com.dao.ContentDAO import ContentDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession

@app.route('/admin/viewContent')
def adminViewContent():
    try:
        if adminLoginSession() == 'admin':
            contentDAO = ContentDAO()
            data = contentDAO.searchContent()
            print(data)
            return render_template("admin/viewUserContent.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteContent')
def adminDeleteContent():
    try:
        if adminLoginSession() == 'admin':
            contentVO = ContentVO()
            contentVO.contentId = request.args.get('contentId')
            contentDAO = ContentDAO()
            contentDAO.deleteContent(contentVO)

            return redirect(url_for("adminViewContent"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadContent')
def userLoadContent():
    try:
        if adminLoginSession() == 'user':
            contentVO = ContentVO()
            contentVO.loginId = session['session_loginId']
            contentDAO = ContentDAO()
            data = contentDAO.searchUserContent(contentVO)
            print(data)

            return render_template("user/card.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/deleteContent')
def userDeleteContent():
    try:
        if adminLoginSession() == 'user':
            contentVO = ContentVO()
            contentVO.contentId = request.args.get('contentId')
            contentDAO = ContentDAO()
            contentDAO.deleteContent(contentVO)

            return redirect(url_for("userLoadContent"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)
