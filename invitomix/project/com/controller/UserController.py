from project import app
from flask import request, render_template,redirect,url_for
from project.com.vo.UserVO import UserVO
from project.com.dao.UserDAO import UserDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from getpass import getpass

@app.route('/user/loadhome')
def userLoadhome():
    return render_template("user/index.html")

@app.route('/')
def adminLoad():
    return render_template("admin/login.html")

@app.route('/user/loadRegister')
def userLoadRegister():
    return render_template("admin/register.html")

@app.route('/admin/insertUser', methods=['post'])
def adminInsertUser():
    loginVO = LoginVO()
    loginVO.loginUserName = request.form['userName']
    loginVO.loginPassword = request.form['password']
    loginVO.loginRole = "user"
    loginVO.loginStatus = "active"
    confirmPassword = request.form['confirmPassword']
    if loginVO.loginPassword == confirmPassword:
        loginDAO = LoginDAO()
        loginDAO.insertLogin(loginVO)

        userVO = UserVO()
        userVO.userFirstName = request.form['firstName']
        userVO.userLastName = request.form['lastName']
        userVO.userGender = request.form['userGender']
        userVO.userContact = request.form['userContact']

        userDAO = UserDAO()
        userDAO.insertUser(userVO)

        return render_template("admin/login.html")
    else:
        msg = 'Enter password and confirmpassword same!!'

        return render_template('admin/register.html', error=msg)


@app.route('/admin/viewUser')
def adminViewUser():
    userDAO = UserDAO()
    data = userDAO.searchUser()

    return render_template("admin/viewUser.html", key=data)


@app.route('/admin/blockUser', methods=['get', 'post'])
def adminBlockUser():
    userVO = UserVO()
    userVO.user_loginId = request.args.get('loginid')
    print(userVO.user_loginId)
    userVO.loginStatus = "blocked"
    print(userVO.loginStatus)
    userDAO = UserDAO()

    userDAO.blockUnblockUser(userVO)

    return redirect(url_for("adminViewUser"))

@app.route('/admin/unblockUser', methods=['get', 'post'])
def adminUnblockUser():
    userVO = UserVO()
    userVO.user_loginId = request.args.get('loginid')
    print(userVO.user_loginId)
    userVO.loginStatus = "active"
    print(userVO.loginStatus)
    userDAO = UserDAO()

    userDAO.blockUnblockUser(userVO)

    return redirect(url_for("adminViewUser"))






