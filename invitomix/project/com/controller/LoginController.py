import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template, session, redirect, request, url_for

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO

@app.route('/user/loadlogin')
def loadLogin():
    return render_template("admin/login.html")


@app.route("/login", methods=['get', 'post'])
def adminlogin():
    loginUserName = request.form['loginUserName']
    loginPassword = request.form['loginPassword']

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.loginUserName = loginUserName
    loginVO.loginPassword = loginPassword

    loginDict = loginDAO.validateLogin(loginVO)

    lenLoginDict = len(loginDict)
    print(loginDict)

    for row1 in loginDict:
        if row1['loginStatus'] == 'blocked':
            msg = 'you are BLOCKED by admin'

            return render_template('admin/login.html', error=msg)

    if lenLoginDict == 0:

        msg = 'Username Or Password is Incorrect !'

        return render_template('admin/login.html', error=msg)

    else:

        for row1 in loginDict:

            loginId = row1['loginId']

            loginUserName = row1['loginUserName']

            loginRole = row1['loginRole']

            print(loginRole)

            session['session_loginId'] = loginId

            session['session_loginUserName'] = loginUserName

            session['session_loginRole'] = loginRole

            if loginRole == 'admin':
                return redirect(url_for('adminLoadDashboard'))
            if loginRole == 'user':
                return redirect(url_for('userLoadDashboard'))

@app.route("/loadForgetPassword", methods=['GET'])
def loadForgetPassword():
    return render_template('admin/forgetPassword.html')


@app.route("/getForgetPassword", methods=['post'])
def getForgetPassword():
    loginUserName = request.form['loginUserName']

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.loginUserName = loginUserName

    loginDict = loginDAO.checkUserName(loginVO)

    print(loginDict)

    lenDict1 = len(loginDict)

    if lenDict1 == 0:

        return render_template('admin/forgetPassword.html')


    else:

        for row1 in loginDict:
            loginId = row1['loginId']

            print(loginId)

            loginUserName = row1['loginUserName']

            print(loginUserName)

            session['sessionLoginId'] = loginId

            session['sessionloginEmail'] = loginUserName

            sender = "invitomixdonotreply@gmail.com"

            receiver = loginUserName

            msg = MIMEMultipart()

            msg['From'] = sender

            msg['To'] = receiver

            msg['Subject'] = "INVITOMIX OTP"

            otp = random.randint(1000, 9999)

            session['sessionotp'] = str(otp)

            message = str(otp)

            print(message)

            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender, "56invitomix89")

            text = msg.as_string()

            server.sendmail(sender, receiver, text)

            server.quit()

            return render_template('admin/OTP.html')


@app.route('/getOTP', methods=['post'])
def getOTP():
    print("in get otp")

    sessionotp = session['sessionotp']

    userotp = request.form['otp']

    print("sessionotp=", sessionotp)

    print("userotp=", userotp)

    if sessionotp == userotp:

        print("if true for otp")

        loginEmail = session['sessionloginEmail']

        return render_template('admin/updatePassword.html')

    else:

        return render_template('admin/forgetPassword.html')


@app.route('/updatePassword', methods=['post'])
def updatePassword():
    loginId = session['sessionLoginId']

    loginPassword = request.form['loginPassword']

    print(loginId)

    print(loginPassword)

    if loginId != 0 and loginPassword != '':

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginPassword = loginPassword
        loginVO.loginId = loginId

        loginDAO.updatePassword(loginVO)

        return render_template('admin/Login.html')

    else:

        return redirect(url_for('loadForgetPassword'))


@app.route("/admin/logout", methods=['GET'])
def logout():
    return redirect(url_for('load'))


@app.route('/user/loadIndex', methods=['GET'])
def userLoadDashboard():
    try:
        if adminLoginSession() == 'user':
            login = session['session_loginId']
            loginVO = LoginVO()
            loginVO.loginId = str(login)
            loginDAO = LoginDAO()
            data = loginDAO.showUserName(loginVO)
            print(data)
            return render_template('user/index.html', key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/loadIndex')
def adminLoadDashboard():
    try:
        if adminLoginSession() == 'admin':
            return render_template("admin/index.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadContact')
def userLoadContact():
    try:
        if adminLoginSession() == 'user':
            return render_template("user/contact.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/user/loadAbout')
def userLoadAbout():
    try:
        if adminLoginSession() == 'user':
            return render_template("user/about.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/loginSession')
def adminLoginSession():
    if 'session_loginId' and 'session_loginRole' in session:

        if session['session_loginRole'] == 'admin':

            return 'admin'

        elif session['session_loginRole'] == 'user':

            return 'user'

        print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")

    else:

        print("<<<<<<<<<<<<<<<<False>>>>>>>>>>>>>>>>>>>>")

        return False


@app.route("/admin/logoutSession", methods=['GET'])
def adminLogoutSession():
    session.clear()
    return redirect(url_for('loadLogin'))
