import hashlib

from SaleApp.saleappv2.eapp import app

from SaleApp.saleappv2.eapp.models import Category,Product,User,UserRole

def load_categories():
    return Category.query.all()

def load_products(cate_id=None,kw=None,page=1):
    products = Product.query

    if kw:
        query=query.filter(Product.name.contains(kw))

    if cate_id:
        query=query.filter(Product.category_id.__eq__(cate_id))

    if page:
        page=int(page)
        page_size=app.config.get("PAGE_SIZE",6)
        start=(page-1)*page_size
        products=products.slice(start,start+page_size)

    return products.all()

def count_products():
    return Product.query.count()

def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username,password):
    password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username==username.strip(),
                             User.password==password).first()


