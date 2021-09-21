from project import app
from flask import render_template, request, redirect,session, url_for
from project.com.vo.CategoryVO import CategoryVO
from project.com.dao.CategoryDAO import CategoryDAO
from project.com.controller.LoginController import adminLoginSession,adminLogoutSession


@app.route('/admin/loadCategory')
def adminLoadCategory():
    try:
        if adminLoginSession() == 'admin':
            return render_template("admin/addCategory.html")
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadUserCategory')
def userLoadCategory():
    try:
        if adminLoginSession() == 'user':
            categoryDAO = CategoryDAO()
            data = categoryDAO.searchCategory()

            return render_template("user/category.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)

@app.route('/admin/insertCategory', methods=['get', 'post'])
def adminInsertCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryVO = CategoryVO()
            categoryVO.categoryName = request.form['CategoryName']
            categoryVO.categoryDescription = request.form['CategoryDescription']

            categoryDAO = CategoryDAO()
            categoryDAO.insertCategory(categoryVO)
            return redirect(url_for("adminViewCategory"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewCategory')
def adminViewCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryDAO = CategoryDAO()
            data = categoryDAO.searchCategory()
            print(data)
            return render_template("admin/viewCategory.html", key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteCategory')
def adminDeleteCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryVO = CategoryVO()
            categoryVO.categoryId = request.args.get('categoryId')
            categoryDAO = CategoryDAO()
            categoryDAO.deleteCategory(categoryVO)

            return redirect(url_for("adminViewCategory"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/editCategory', methods=['get', 'post'])
def adminEditCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryVO = CategoryVO()
            categoryVO.categoryId = request.args.get('categoryId')
            categoryDAO = CategoryDAO()

            data = categoryDAO.editCategory(categoryVO)
            print(data)
            return render_template('admin/editCategory.html', key=data)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/updateCategory', methods=['get', 'post'])
def adminUpdateCategory():
    try:
        if adminLoginSession() == 'admin':
            categoryVO = CategoryVO()
            categoryVO.categoryName = request.form['categoryName']
            categoryVO.categoryDescription = request.form['categoryDescription']
            categoryVO.categoryId = request.form['categoryId']

            categoryDAO = CategoryDAO()
            categoryDAO.updateCategory(categoryVO)

            return redirect(url_for("adminViewCategory"))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)