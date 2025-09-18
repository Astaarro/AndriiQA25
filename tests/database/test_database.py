import pytest
from modules.common.database import Database


# TEST DATABASE FOR PERSONAL WORK

# Try to insert text instead of a number in quantity
@pytest.mark.database
def test_insert_invalid_data_type():
    db = Database()
    try:
        db.insert_products(100, 'некоректний', 'дані', 'wrong_type')
        assert False, "Expected an error when inserting invalid data type"
    except Exception as error:
        print("Caught expected exception:", error)
        
        assert True

# Check that the quantity can be negative. (Bug?)
@pytest.mark.database
def test_update_negative_quantity():
    db = Database()
    db.insert_products(5, 'молоко', 'літрове', 10)
    db.update_product_qnt_by_id(5, -5)
    qnt = db.select_product_qnt_by_id(5)
    
    assert qnt[0][0] == -5

# Check that we can insert emoji in field "name" and "description"
@pytest.mark.database
def test_insert_and_read_unicode_data():
    db = Database()
    db.insert_products(6, 'банан 🍌', 'жовтий 🟡', 15)
    product = db.select_product_qnt_by_id(6)
    
    assert product[0][0] == 15

# Test delete non existing product (Bug?)
@pytest.mark.database
def test_delete_non_existent_product():
    db = Database()
    db.delete_products_by_id(9999)  
    qnt = db.select_product_qnt_by_id(9999)

    assert len(qnt) == 0

# Test sum some similar product
@pytest.mark.database
def test_multiple_inserts_and_sum():
    db = Database()
    db.insert_products(7, 'масло', 'селянське', 1)
    db.insert_products(8, 'масло', 'вершкове', 10)
    qnt1 = db.select_product_qnt_by_id(7)[0][0]
    qnt2 = db.select_product_qnt_by_id(8)[0][0]

    assert (qnt1 + qnt2) == 11

# Test solds all products
@pytest.mark.database
def test_update_product_to_zero_quantity():
    db = Database()
    db.insert_products(9, 'ковбаса', 'лікарська', 10)
    db.update_product_qnt_by_id(9, 0)
    qnt = db.select_product_qnt_by_id(9)

    assert qnt[0][0] == 0

# Test overwrite product
@pytest.mark.database
def test_reinsert_same_id_overwrites_data():
    db = Database()
    db.insert_products(10, 'сік', 'яблучний', 12)
    db.insert_products(10, 'сік', 'апельсиновий', 30)
    qnt = db.select_product_qnt_by_id(10)

    assert qnt[0][0] == 30

# Test update noneexisting product
@pytest.mark.database
def test_update_nonexistent_product():
    db = Database()
    db.update_product_qnt_by_id(9999, 100)
    product = db.select_product_qnt_by_id(9999)

    assert len(product) == 0

# Test product with empty name
@pytest.mark.database
def test_insert_product_with_empty_name():
    db = Database()
    db.insert_products(11, '', 'без імені', 10)
    product = db.select_product_qnt_by_id(11)
    
    assert product[0][0] == 10

    # Checking that the name is empty
    name = db.get_name_product(11)[0][0]
    assert name == ''


# QA AUTOMATION COURSE DATABASE TESTS

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name ("Sergii")

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_products(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_products(99, 'тестові', 'дані', 999)
    db.delete_products_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    #Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
