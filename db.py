import sqlite3 

def create_tables():

    conn = sqlite3.connect("userfile.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT UNIQUE NOT NULL,
        user_name TEXT NOT NULL,
        user_tg_id INTEGER UNIQUE
    );

    CREATE TABLE IF NOT EXISTS place (
        place_id INTEGER PRIMARY KEY,
        place_name TEXT NOT NULL,
        address TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        category TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS product_variants (
        id INTEGER PRIMARY KEY,
        product_id INTEGER NOT NULL,
        variant_name TEXT NOT NULL,
        price INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    );

    CREATE TABLE IF NOT EXISTS modifiers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS carts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        pickup_point_id INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES users(user_id),
        FOREIGN KEY (pickup_point_id) REFERENCES place(place_id)
    );

    CREATE TABLE IF NOT EXISTS cart_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cart_id INTEGER NOT NULL,
        product_variant_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        item_price INTEGER NOT NULL,
        FOREIGN KEY (cart_id) REFERENCES carts(id),
        FOREIGN KEY (product_variant_id) REFERENCES product_variants(id)
    );

    CREATE TABLE IF NOT EXISTS cart_item_modifiers (
        cart_item_id INTEGER NOT NULL,
        modifier_id INTEGER NOT NULL,
        PRIMARY KEY (cart_item_id, modifier_id),
        FOREIGN KEY (cart_item_id) REFERENCES cart_items(id),
        FOREIGN KEY (modifier_id) REFERENCES modifiers(id)
    );

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        pickup_point_id INTEGER NOT NULL,
        total_price INTEGER NOT NULL,
        status TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT (datetime('now','localtime')),
        FOREIGN KEY (customer_id) REFERENCES users(user_id),
        FOREIGN KEY (pickup_point_id) REFERENCES place(place_id)
    );

    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        variant_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        item_price INTEGER NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(id)
    );

    CREATE TABLE IF NOT EXISTS order_item_modifiers (
        order_item_id INTEGER NOT NULL,
        modifier_name TEXT NOT NULL,
        price INTEGER NOT NULL,
        PRIMARY KEY (order_item_id, modifier_name),
        FOREIGN KEY (order_item_id) REFERENCES order_items(id)
    );
    """)

    conn.commit()
    conn.close()

def products_in():
    conn = sqlite3.connect("userfile.db")
    cur = conn.cursor()

    cur.executescript("""
        INSERT INTO products (id, product_name, category) 
        VALUES (1, 'Американо', 'drinks'), (2, 'Эспрессо', 'drinks'), (3, 'Фильтр-кофе', 'drinks'), (4, 'Капучино', 'drinks'), (5, 'Латте', 'drinks'), (6, 'Флэт Уайт', 'drinks'), (7, 'Раф', 'drinks'), (8, 'Матча', 'drinks'), (9, 'Какао', 'drinks'),
        (10, 'Бабка с шоколадом и вишней', 'food'), (11, 'Сэндвич с мясом', 'food'), (12, 'Краффин с соленой карамелью', 'food'), (13, 'Канеле', 'food'), (14, 'Ржаной даниш с брынзой', 'food'), (15, 'Круассан с сыром', 'food'), (16, 'Пан шоколя', 'food'); 

        INSERT INTO place (place_id, place_name, address)
        VALUES (1, 'ЛЕНПОЛИГРАФМАШ', 'Санкт-Петербург, Аптекарский просп., 2'), (2, 'У КАРАНДАША', 'Санкт-Петербург, Большой Сампсониевский просп., 76');

        INSERT INTO modifiers (id, name, price)
        VALUES (1, 'Сироп карамель', 20), (2, 'Сироп ваниль', 30), (3, 'Сироп орех', 50), (4, 'Овсяное молоко', 50), (5, 'Миндальное молоко', 20), (6, 'Кокосовое молоко', 31);
                      
        INSERT INTO product_variants (id, product_id, variant_name, price)
        VALUES 
            -- drinks
            (1, 1, 'Small', 180), (2, 1, 'Big', 220), -- американо
            (3, 2, 'Small', 150), -- эспрессо
            (4, 3, 'Small', 180), (5, 3, 'Big', 220), -- фильтр кофе
            (6, 4, 'Small', 220), (7, 4, 'Big', 280), -- капучино
            (8, 5, 'Small', 210), (9, 5, 'Big', 260), -- латте
            (10, 6, 'Small', 240), -- флэт вайт 
            (11, 7, 'Small', 250), (12, 7, 'Big', 310), -- Раф
            (13, 8, 'Small', 240), (14, 8, 'Big', 280), -- Матча
            (15, 9, 'Small', 300),  -- Какао
                      
            -- food
            (16, 10, 'onesize', 270), -- Бабка           
            (17, 11, 'onesize', 350), -- Сэндвич с мясом
            (18, 12, 'onesize', 270), -- Крафин 
            (19, 13, 'onesize', 150), -- Канеле       
            (20, 14, 'onesize', 250), -- Даниш
            (21, 15, 'onesize', 250), -- круасан с сыром
            -- Пан шоколя
            (22, 16, 'onesize', 250);
                      
""")


    conn.commit()
    conn.close()
