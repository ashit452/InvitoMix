
from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.BackgroundVO import BackgroundVO
from project.com.dao.BackgroundDAO import BackgroundDAO
from project.com.dao.SubCategoryDAO import SubCategoryDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession

from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'project/static/adminResources/dataset/background/'

'''app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER'''


@app.route('/admin/loadBackground')
def adminLoadBackground():
    try:
        if adminLoginSession() == 'admin':
            subCategoryDAO = SubCategoryDAO()
            data = subCategoryDAO.searchSubCategory()

            return render_template("admin/addBackground.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/user/loadBackground')
def userLoadBackground():
    try:
        if adminLoginSession() == 'user':
            backgroundVO = BackgroundVO()
            backgroundVO.subCategoryId = request.args.get('subcategoryId')
            backgroundDAO = BackgroundDAO()
            data = backgroundDAO.searchUserBackground(backgroundVO)
            print(data)

            return render_template("user/background.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/insertBackground', methods=['post'])
def adminInsertBackground():
    try:
        if adminLoginSession() == 'admin':
            backgroundVO = BackgroundVO()
            backgroundDAO = BackgroundDAO()

            file = request.files['backgroundFile']
            print(file)

            backgroundFilename = secure_filename(file.filename)
            print(backgroundFilename)

            backgroundFilepath = os.path.join(UPLOAD_FOLDER)
            print(backgroundFilepath)

            file.save(os.path.join(backgroundFilepath, backgroundFilename))

            backgroundVO.backgroundName = backgroundFilename

            backgroundVO.backgroundPath = backgroundFilepath.replace("project", "..")

            backgroundVO.subCategoryId = request.form['background_subCategoryId']

            backgroundDAO.insertBackground(backgroundVO)

            return redirect(url_for("adminViewBackground"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewBackground')
def adminViewBackground():
    try:
        if adminLoginSession() == 'admin':
            backgroundDAO = BackgroundDAO()
            data=backgroundDAO.searchBackground()

            return render_template("admin/viewBackground.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteBackground')
def adminDeleteBackground():
    try:
        if adminLoginSession() == 'admin':
            backgroundVO = BackgroundVO()
            backgroundVO.backgroundId = request.args.get('backgroundId')
            backgroundDAO = BackgroundDAO()
            backgroundDAO.deleteBackground(backgroundVO)

            return redirect(url_for("adminViewBackground"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

