from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.TemplateVO import TemplateVO
from project.com.dao.TemplateDAO import TemplateDAO
from project.com.dao.SubCategoryDAO import SubCategoryDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession

from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'project/static/adminResources/dataset/template/'

'''app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER'''


@app.route('/admin/loadTemplate')
def adminLoadTemplate():
    try:
        if adminLoginSession() == 'admin':
            subCategoryDAO = SubCategoryDAO()
            data = subCategoryDAO.searchSubCategory()

            return render_template("admin/addTemplate.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/user/loadTemplate')
def userLoadTemplate():
    try:
        if adminLoginSession() == 'user':
            session['sessionCharacter'] = request.args.get('characterId')
            print(session['sessionCharacter'])

            templateVO = TemplateVO()
            templateVO.subCategoryId = request.args.get('subcategoryId')
            templateDAO = TemplateDAO()

            data = templateDAO.searchUserTemplate(templateVO)
            print(data)

            return render_template("user/template.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/insertTemplate', methods=['post'])
def adminInsertTemplate():
    try:
        if adminLoginSession() == 'admin':
            templateVO = TemplateVO()
            templateDAO = TemplateDAO()

            file = request.files['templateFile']
            print(file)

            templateFilename = secure_filename(file.filename)
            print(templateFilename)

            templateFilepath = os.path.join(UPLOAD_FOLDER)
            print(templateFilepath)

            file.save(os.path.join(templateFilepath, templateFilename))

            templateVO.templateName = templateFilename

            templateVO.templatePath = templateFilepath.replace("project", "..")

            templateVO.subCategoryId = request.form['template_subCategoryId']

            templateDAO.insertTemplate(templateVO)

            return redirect(url_for("adminViewTemplate"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewTemplate')
def adminViewTemplate():
    try:
        if adminLoginSession() == 'admin':
            templateDAO = TemplateDAO()
            data = templateDAO.searchTemplate()
            print(data)

            return render_template("admin/viewTemplate.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/deleteTemplate')
def adminDeleteTemplate():
    try:
        if adminLoginSession() == 'admin':
            templateVO = TemplateVO()
            templateVO.templateId = request.args.get('templateId')
            templateDAO = TemplateDAO()
            templateDAO.deleteTemplate(templateVO)

            return redirect(url_for("adminViewTemplate"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

