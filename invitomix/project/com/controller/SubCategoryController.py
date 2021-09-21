from project import app
from flask import request, render_template,redirect,url_for,session
from project.com.vo.SubCategoryVO import SubCategoryVO
from project.com.dao.SubCategoryDAO import SubCategoryDAO
from project.com.dao.CategoryDAO import CategoryDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession


@app.route('/admin/loadSubCategory')
def adminLoadSubCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryDAO = CategoryDAO()
            data = categoryDAO.searchCategory()

            return render_template("admin/addSubCategory.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadSubCategory')
def userLoadSubCategory():
    try:
        if adminLoginSession() == 'user':
            subCategoryVO = SubCategoryVO()
            session['sessionCategory'] = request.args.get('categoryId')
            subCategoryVO.subCategory_categoryId = request.args.get('categoryId')
            subCategoryDAO = SubCategoryDAO()
            data = subCategoryDAO.searchUserSubCategory(subCategoryVO)
            print(data)

            return render_template("user/subCategory.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/insertSubCategory', methods=['get', 'post'])
def adminInsertSubCategory():
    try:
        if adminLoginSession() == 'admin':
            subCategoryVO = SubCategoryVO()

            subCategoryVO.subCategoryName = request.form['subCategoryName']
            subCategoryVO.subCategoryDescription = request.form['subCategoryDescription']
            subCategoryVO.subCategory_categoryId = request.form['subCategory_categoryId']
            print(subCategoryVO.subCategory_categoryId)

            subCategoryDAO = SubCategoryDAO()
            subCategoryDAO.insertSubCategory(subCategoryVO)

            return redirect(url_for("adminViewSubCategory"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewSubCategory')
def adminViewSubCategory():
    try:
        if adminLoginSession() == 'admin':
            subCategoryDAO = SubCategoryDAO()
            data=subCategoryDAO.searchSubCategory()


            return render_template("admin/viewSubCategory.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/deleteSubCategory')
def adminDeleteSubCategory():
    try:
        if adminLoginSession() == 'admin':
            subCategoryVO = SubCategoryVO()
            subCategoryVO.subCategoryId = request.args.get('subcategoryId')
            subCategoryDAO = SubCategoryDAO()
            subCategoryDAO.deleteSubCategory(subCategoryVO)

            return redirect(url_for("adminViewSubCategory"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/editSubCategory', methods=['get', 'post'])
def adminEditSubCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryDAO = CategoryDAO()
            cat = categoryDAO.searchCategory()
            subCategoryVO = SubCategoryVO()
            subCategoryVO.subCategoryId = request.args.get('subcategoryId')

            subCategoryDAO = SubCategoryDAO()

            data = subCategoryDAO.editSubCategory(subCategoryVO)

            print(data)
            return render_template('admin/editSubCategory.html', key=data, key2=cat)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/updateSubCategory', methods=['get', 'post'])
def adminUpdateSubCategory():
    try:
        if adminLoginSession() == 'admin':
            subCategoryVO = SubCategoryVO()
            subCategoryVO.subCategoryName = request.form['subCategoryName']
            subCategoryVO.subCategoryDescription = request.form['subCategoryDescription']
            subCategoryVO.subCategoryId = request.form['subCategoryId']
            subCategoryVO.subCategory_categoryId = request.form['subCategory_categoryId']
            print(subCategoryVO.subCategoryName)
            print(subCategoryVO.subCategoryDescription)
            subCategoryDAO = SubCategoryDAO()
            subCategoryDAO.updateSubCategory(subCategoryVO)

            return redirect(url_for("adminViewSubCategory"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)
