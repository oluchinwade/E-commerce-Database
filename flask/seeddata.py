import random
import string
import hashlib
from faker import Faker
from e_commerce.src.models import User, Vendor, Order, Product, product_order, db
from e_commerce.src import create_app
import secrets
f = Faker()

data_number= 31
order_number = 10
product_categories =['Clothing', 'Accessories','Footwears', 'Face + Body']
product_description = ['New in stock.', ' trending.', 'on sale 10percent off.', 'out of stock coming soon.','low stock buy now.']

def random_passwordhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&', # valid pw characters
            k=random.randint(8, 15) # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()

def truncate_tables():
    try:
        # Truncate tables
        db.session.query(User).delete()
        db.session.query(Vendor).delete()
        db.session.query(Product).delete()

        # Commit the changes
        db.session.commit()
        print("Tables truncated successfully.")
    except Exception as e:
        print(f"Error truncating tables: {e}")
        db.session.rollback()

def main():
    app = create_app()
    app.app_context().push()
    truncate_tables()

    vendor_info = None
    for _ in range(data_number):
        vendor_info = Vendor(
            name = f.unique.company(),
            email=f.unique.email().lower()
        )
        db.session.add(vendor_info)
    db.session.commit()

    user_info = None  # save users information
    for _ in range(data_number):
        user_info = User(
            username=f.unique.first_name().lower() + str(random.randint(1,99)),
            email=f.unique.email().lower(),
            
            password=random_passwordhash()
        )
        db.session.add(user_info)
    db.session.commit()



    product_info = None
    for _ in range(data_number):
        product_info = Product(
            name = f.unique.word(),
            category = random.choice(product_categories),
            description = random.choice(product_description),
            amount = random.uniform(10, 1000),
            vendor_id = random.randint(vendor_info.id - data_number + 1, vendor_info.id)
        )
        db.session.add(product_info)
    db.session.commit()

main()






