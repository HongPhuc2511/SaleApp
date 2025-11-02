from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from SaleApp.saleappv2.eapp import app,db
from SaleApp.saleappv2.eapp.models import Category, Product

app.secret_key="!@#$%^&*()123456789"
admin=Admin(app=app,name="e-Commerce's Admin")
admin.add_view(ModelView(Category,db.session))
admin.add_view(ModelView(Product,db.session))
