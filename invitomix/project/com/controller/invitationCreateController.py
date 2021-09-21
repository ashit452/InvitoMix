import random
from PIL import Image, ImageDraw , ImageFont
from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.CreateVO import CreateVO
from project.com.dao.CreateDAO import CreateDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession

from project.com.vo.ContentVO import ContentVO
from project.com.dao.ContentDAO import ContentDAO



UPLOAD_FOLDER = 'project/static/adminResources/dataset/content/'

@app.route('/user/text')
def userText():
    try:
        if adminLoginSession() == 'user':
            session['sessionTemplate'] = request.args.get('templateId')

            return render_template("user/text.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/createInvitationcard',methods=['post'])
def userCreateInvitationcard():
    try:
        if adminLoginSession() == 'user':
            text = request.form['text']
            data1 = session['sessionBackground']
            createVO = CreateVO()
            createVO.backgroundId = data1
            print(createVO.backgroundId)
            createDAO = CreateDAO()
            data4 = createDAO.searchCreateBackground(createVO)
            print(data4)


            for i in data4 :
                print(i)
                print(i['backgroundPath'])
                file = i['backgroundPath']+i['backgroundName']
                filepath = file.replace("..", "project")

                session['sessionA'] = filepath




            data2 = session['sessionCharacter']
            createVO = CreateVO()
            createVO.characterId = data2
            print(createVO.characterId)
            createDAO = CreateDAO()
            data5 = createDAO.searchCreateCharacter(createVO)
            print(data5)

            for j in data5 :
                print(j)
                print(j['characterPath'])
                file = j['characterPath']+j['characterName']
                filepath = file.replace("..", "project")

                session['sessionB'] = filepath



            data3 = session['sessionTemplate']
            createVO = CreateVO()
            createVO.templateId = data3
            print(createVO.templateId)
            createDAO = CreateDAO()
            data6 = createDAO.searchCreateTemplate(createVO)
            print(data6)

            for k in data6 :
                print(k)
                print(k['templatePath'])
                file = k['templatePath']+k['templateName']
                filepath = file.replace("..", "project")

                session['sessionC'] = filepath

            a = Image.open(session['sessionA'])
            b = Image.open(session['sessionB'])
            c = Image.open(session['sessionC'])
            '''a = Image.open("E:\projectfiles\images\\template\\background\paper-2926300_1920.jpg")
            b = Image.open("E:\projectfiles\images\\baby shower\\footprint-23991_1280.png")
            c = Image.open("E:\projectfiles\images\\template\corner-47040_1280.png")'''

            a.paste(a, (0,0))
            a.paste(b, (300,300),mask=b)
            a.paste(c, (50,50),mask=c)
            fonttype = ImageFont.truetype('arial.ttf',80)
            draw = ImageDraw.Draw(a)
            draw.text(xy=(400,1600), text=text, font=fonttype ,fill="Black")

            number = random.randint(00000, 99999)

            content = "content"+str(number)+".jpg"

            path = UPLOAD_FOLDER + content

            a.save(path)

            contentVO = ContentVO()
            contentVO.categoryId = session['sessionCategory']
            print(contentVO.categoryId)
            contentVO.contentPath = path.replace("project", "..")
            print(contentVO.contentPath)
            contentVO.loginId = session['session_loginId']
            print(contentVO.loginId)

            contentDAO = ContentDAO()
            contentDAO.insertContent(contentVO)

            return redirect(url_for("userLoadContent"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)






