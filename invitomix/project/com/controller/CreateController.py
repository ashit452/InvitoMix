from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.CreateVO import CreateVO
from project.com.dao.CreateDAO import CreateDAO
from project.com.dao.BackgroundDAO import BackgroundDAO
from project.com.dao.CharacterDAO import CharacterDAO
from project.com.dao.TemplateDAO import TemplateDAO

from project.com.dao.SubCategoryDAO import SubCategoryDAO


@app.route('/user/create')
def userCreate():

    data1 = session['sessionBackground']
    createVO = CreateVO()
    createVO.backgroundId = data1
    print(createVO.backgroundId)
    createDAO = CreateDAO()
    data4 = createDAO.searchCreateBackground(createVO)
    print(data4)

    data2 = session['sessionCharacter']
    createVO = CreateVO()
    createVO.characterId = data2
    print(createVO.characterId)
    createDAO = CreateDAO()
    data5 = createDAO.searchCreateCharacter(createVO)
    print(data5)

    session['sessionTemplate'] = request.args.get('templateId')
    data3 = session['sessionTemplate']
    createVO = CreateVO()
    createVO.templateId = data3
    print(createVO.templateId)
    createDAO = CreateDAO()
    data6 = createDAO.searchCreateTemplate(createVO)
    print(data6)

    ls = [data4, data5, data6]

    return render_template("user/create.html", key=ls)