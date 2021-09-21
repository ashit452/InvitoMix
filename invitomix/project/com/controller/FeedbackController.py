import datetime
from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.FeedbackVO import FeedbackVO
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession,userLoadDashboard


@app.route('/user/loadFeedback')
def userLoadFeedback():
    try:
        if adminLoginSession() == 'user':
            return render_template("user/postFeedback.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/insertFeedback', methods=['get', 'post'])
def userInsertFeedback():
    try:
        if adminLoginSession() == 'user':
            feedbackVO = FeedbackVO()
            feedbackVO.feedbackSubject = request.form['feedbackSubject']
            print(feedbackVO.feedbackSubject)
            feedbackVO.feedbackDescription = request.form['feedbackDescription']
            print(feedbackVO.feedbackDescription)
            feedbackVO.feedbackRatings = request.form['rate']
            print(feedbackVO.feedbackRatings)
            feedbackVO.feedbackDate = str(datetime.date.today())
            print(feedbackVO.feedbackDate)
            feedbackVO.feedbackTime = str(datetime.datetime.now().strftime("%H:%M:%S"))
            print(feedbackVO.feedbackTime)
            feedbackVO.loginId = str(session['session_loginId'])
            print(feedbackVO.loginId)

            feedbackDAO = FeedbackDAO()
            feedbackDAO.insertFeedback(feedbackVO)
            if feedbackVO.loginId is not None:
                msg = "Feedback sent sucessfully"

            return render_template("user/postFeedback.html",key = msg)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewFeedback')
def adminViewFeedback():
    try:
        if adminLoginSession() == 'admin':
            feedbackDAO = FeedbackDAO()
            data=feedbackDAO.searchFeedback()

            return render_template("admin/viewFeedback.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteFeedback')
def adminDeleteFeedback():
    try:
        if adminLoginSession() == 'admin':
            feedbackVO = FeedbackVO()
            feedbackVO.feedbackId = request.args.get('feedbackId')
            feedbackDAO = FeedbackDAO()
            feedbackDAO.deleteFeedback(feedbackVO)

            return redirect(url_for("adminViewFeedback"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


