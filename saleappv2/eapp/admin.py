from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from SaleApp.saleappv2.eapp import app,db
from SaleApp.saleappv2.eapp.models import Category, Product,UserRole
from flask import redirect
from flask_login import logout_user,current_user
admin=Admin(app=app,name="e-Commerce's Admin")

class AuthenticatedModelView(ModelView):
    def is_accessible(self)->bool:
        return current_user.is_authenticated and current_user.user_role==UserRole.ADMIN

class ProductModelView(AuthenticatedModelView):
    column_list = ('id','name','price','category_id')
    can_export = True
    page_size = 5
    column_searchable_list = ['name']
    column_filters = ['id','name','price']
    column_editable_list = ['name','price']
    edit_modal = True

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(AuthenticatedModelView(Category,db.session))
admin.add_view(ProductModelView(Product,db.session))
admin.add_view(LogoutView(name='Đăng xuất'))