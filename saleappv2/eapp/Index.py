from flask import render_template, request, redirect
from flask_login import login_user,logout_user
from SaleApp.saleappv2.eapp import app,dao,login
from SaleApp.saleappv2.eapp.models import UserRole
import math


@app.route('/')
def index():

    products = dao.load_products(cate_id=request.args.get('category_id'),
                                 kw=request.args.get('kw'),
                                 page=request.args.get('page'))

    return render_template('index.html',
                           pages=math.ceil(dao.count_products()/app.config['PAGE_SIZE']),
                           products=products,
                           page=request.args.get('page',1))

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')
@app.route('/login',methods=['post'])
def login_process():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')

    u=dao.auth_user(username=username,password=password)
    if u:
        login_user(user=u)

    next=request.args.get('next')
    return redirect(next if next else '/')

    return redirect('/admin')

@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

@app.context_processor
def common_response():
    return{
        'categories' :dao.load_categories()
    }

if __name__ == '__main__':
    from SaleApp.saleappv2.eapp import admin
    app.run(debug=True)
