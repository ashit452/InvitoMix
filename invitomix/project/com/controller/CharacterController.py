from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.CharacterVO import CharacterVO
from project.com.dao.CharacterDAO import CharacterDAO
from project.com.dao.SubCategoryDAO import SubCategoryDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession

from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'project/static/adminResources/dataset/character/'

'''app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER'''


@app.route('/admin/loadCharacter')
def adminLoadCharacter():
    try:
        if adminLoginSession() == 'admin':
            subCategoryDAO = SubCategoryDAO()
            data = subCategoryDAO.searchSubCategory()

            return render_template("admin/addCharacter.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadCharacter')
def userLoadCharacter():
    try:
        if adminLoginSession() == 'user':
            session['sessionBackground'] = request.args.get('backgroundId')
            print(session['sessionBackground'])

            characterVO = CharacterVO()
            characterVO.subCategoryId = request.args.get('subcategoryId')
            characterDAO = CharacterDAO()

            data = characterDAO.searchUserCharacter(characterVO)
            print(data)

            return render_template("user/character.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/insertCharacter', methods=['post'])
def adminInsertCharacter():
    try:
        if adminLoginSession() == 'admin':
            characterVO = CharacterVO()
            characterDAO = CharacterDAO()

            file = request.files['characterFile']
            print(file)

            characterFilename = secure_filename(file.filename)
            print(characterFilename)

            characterFilepath = os.path.join(UPLOAD_FOLDER)
            print(characterFilepath)

            file.save(os.path.join(characterFilepath, characterFilename))

            characterVO.characterName = characterFilename

            characterVO.characterPath = characterFilepath.replace("project", "..")

            characterVO.subCategoryId = request.form['character_subCategoryId']

            characterDAO.insertCharacter(characterVO)

            return redirect(url_for("adminViewCharacter"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/viewCharacter')
def adminViewCharacter():
    try:
        if adminLoginSession() == 'admin':
            characterDAO = CharacterDAO()
            data=characterDAO.searchCharacter()

            return render_template("admin/viewCharacter.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/deleteCharacter')
def adminDeleteCharacter():
    try:
        if adminLoginSession() == 'admin':
            characterVO = CharacterVO()
            characterVO.characterId = request.args.get('characterId')
            characterDAO = CharacterDAO()
            characterDAO.deleteCharacter(characterVO)

            return redirect(url_for("adminViewCharacter"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

