from datetime import datetime
import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_user(self, chat_id):
        self.cur.execute("""
            insert into kebab_site_admin_user(
                chat_id, 
                first_name,
                last_name, 
                lang_id,
                phone_number
            ) values (?, ?, ?, ?, ?)
        """, (
            chat_id,  # chat_id
            None,  # first_name = None
            None,  # last_name = None
            None,  # lang_id = None
            None  # phone_number = None
        ))
        self.conn.commit()

    def update_user_data(self, chat_id, key, value):
        self.cur.execute(f"""update kebab_site_admin_user set {key} = ? where chat_id = ?""", (value, chat_id))
        self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        self.cur.execute("""select * from kebab_site_admin_user where chat_id = ?""", (chat_id, ))
        user = dict_fetchone(self.cur)
        return user

    def get_categories_by_parent(self, parent_id=None):
        if parent_id:
            self.cur.execute("""select * from kebab_site_admin_category where parent_id = ?""", (parent_id, ))
        else:
            self.cur.execute("""select * from kebab_site_admin_category where parent_id is NULL""")

        categories = dict_fetchall(self.cur)
        return categories

    def get_category_parent(self, category_id):
        self.cur.execute("""select parent_id from kebab_site_admin_category where id = ?""", (category_id, ))
        category = dict_fetchone(self.cur)
        return category

######### new ##############
    def get_products_by_category(self, category_id):
        self.cur.execute("""select * from kebab_site_admin_product where category_id = ?""", (category_id, ))
        products = dict_fetchall(self.cur)
        return products

    def get_product_by_id(self, product_id):
        self.cur.execute("""select * from kebab_site_admin_product where id = ?""", (product_id, ))
        product = dict_fetchone(self.cur)
        return product
##################################

# lesson-4 ####################

    def get_product_for_cart(self, product_id):
        self.cur.execute(
            """select kebab_site_admin_product.*, kebab_site_admin_category.name_uz as cat_name_uz, kebab_site_admin_category.name_ru as cat_name_ru 
            from kebab_site_admin_product inner join kebab_site_admin_category on kebab_site_admin_product.category_id = kebab_site_admin_category.id where kebab_site_admin_product.id = ?""",
            (product_id, )
        )
        product = dict_fetchone(self.cur)
        return product

    def create_order(self, user_id, products, payment_type, location):
        self.cur.execute(
            """insert into "kebab_site_admin_order"(status, created_at, user_id, payment_type, longitude, latitude) values (?, ?, ?, ?, ?, ?)""",
            (1,datetime.now(), user_id, payment_type, location.longitude, location.latitude)
        )
        self.conn.commit()
        self.cur.execute(
            """select max(id) as last_order from "kebab_site_admin_order" where user_id = ?""", (user_id, )
        )
        last_order = dict_fetchone(self.cur)['last_order']
        for key, val in products.items():
            self.cur.execute(
                """insert into "kebab_site_admin_orderproduct"(product_id, order_id, amount, created_at) values (?, ?, ?, ?)""",
                (int(key), last_order,  int(val), datetime.now())
            )
        self.conn.commit()

    def get_user_orders(self, user_id):
        self.cur.execute(
            """select * from "kebab_site_admin_order" where user_id = ? and status = 1""", (user_id, )
        )
        orders = dict_fetchall(self.cur)
        return orders

    def get_order_products(self, order_id):
        self.cur.execute(
            """select kebab_site_admin_orderproduct.*, kebab_site_admin_product.name_uz as product_name_uz, kebab_site_admin_product.name_ru as product_name_ru, 
            kebab_site_admin_product.price as product_price from kebab_site_admin_orderproduct inner join kebab_site_admin_product on kebab_site_admin_orderproduct.product_id = product.id
            where order_id = ?""", (order_id, ))
        products = dict_fetchall(self.cur)
        return products

    # def update_suggestions(self,user_id, message ):

##############################

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
