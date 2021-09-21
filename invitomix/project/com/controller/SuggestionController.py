import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.SuggestionVO import SuggestionVO
from project.com.dao.SuggestionDAO import SuggestionDAO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession,userLoadDashboard

from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'project/static/adminResources/dataset/suggestion/'

'''app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER'''

@app.route('/user/loadSuggestion')
def userLoadSuggestion():
    try:
        if adminLoginSession() == 'user':
            return render_template("user/postSuggestion.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/insertSuggestion', methods=['get', 'post'])
def userInsertSuggestion():
    try:
        if adminLoginSession() == 'user':
            suggestionVO = SuggestionVO()

            file = request.files['suggestionFile']
            print(file)

            suggestionFilename = secure_filename(file.filename)
            print(suggestionFilename)

            suggestionFilepath = os.path.join(UPLOAD_FOLDER)
            print(suggestionFilepath)

            file.save(os.path.join(suggestionFilepath, suggestionFilename))

            suggestionVO.suggestionSubject = request.form['suggestionSubject']

            suggestionVO.suggestionDescription = request.form['suggestionDescription']

            suggestionVO.suggestionFile = suggestionFilepath.replace("project", "..")+suggestionFilename

            suggestionVO.suggestionDate = str(datetime.date.today())

            suggestionVO.suggestionTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
            print(suggestionVO.suggestionTime)
            suggestionVO.loginId = str(session['session_loginId'])
            print(suggestionVO.loginId)

            suggestionVO.suggestionStatus = "pending"

            suggestionDAO = SuggestionDAO()
            suggestionDAO.insertSuggestion(suggestionVO)
            if suggestionVO.loginId is not None:
                msg = "Suggestion sent sucessfully"
                return render_template("user/postSuggestion.html",key=msg)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/replySuggestion', methods=['get', 'post'])
def adminReplySuggestion():
    try:
        if adminLoginSession() == 'admin':
            suggestionVO = SuggestionVO()
            suggestionVO.suggestionId = request.args.get('suggestionId')
            suggestionVO.loginId = request.args.get('loginId')
            print(suggestionVO.suggestionId)

            suggestionDAO = SuggestionDAO()

            data = suggestionDAO.replySuggestion(suggestionVO)


            print(data)
            return render_template('admin/replySuggestion.html', key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/updateSuggestion', methods=['get', 'post'])
def adminUpdateSuggestion():
    try:
        if adminLoginSession() == 'admin':
            suggestionVO = SuggestionVO()
            suggestionVO.suggestionReply = request.form['suggestionReply']
            suggestionVO.suggestionStatus = "replied"
            suggestionVO.suggestionId = request.form['suggestionId']

            print(suggestionVO.suggestionStatus)
            print(suggestionVO.suggestionReply)
            suggestionDAO = SuggestionDAO()
            suggestionDAO.updateSuggestion(suggestionVO)

            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginVO.loginId = request.form['suggestion_loginId']

            dict = loginDAO.checkUserEmail(loginVO)

            for row1 in dict:
                session['login_UserEmail'] = row1['loginUserName']

            print(session['login_UserEmail'])

            session['suggestion_reply'] = request.form['suggestionReply']

            sender = "invitomixdonotreply@gmail.com"

            receiver = session['login_UserEmail']

            msg = MIMEMultipart()

            msg['From'] = sender

            msg['To'] = receiver

            msg['Subject'] = "Suggestion Reply"

            message = session['suggestion_reply']

            print(message)

            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender, "56invitomix89")

            text = msg.as_string()

            server.sendmail(sender, receiver, text)

            server.quit()

            return redirect(url_for("adminViewSuggestion"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewSuggestion')
def adminViewSuggestion():
    try:
        if adminLoginSession() == 'admin':
            suggestionDAO = SuggestionDAO()
            data=suggestionDAO.searchSuggestion()

            return render_template("admin/viewSuggestion.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteSuggestion')
def adminDeleteSuggestion():
    try:
        if adminLoginSession() == 'admin':
            suggestionVO = SuggestionVO()
            suggestionVO.suggestionId = request.args.get('suggestionId')
            suggestionDAO = SuggestionDAO()
            suggestionDAO.deleteSuggestion(suggestionVO)

            return redirect(url_for("adminViewSuggestion"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

