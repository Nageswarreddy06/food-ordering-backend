import mysql.connector

# Connect to the MySQL container
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port=3307,          # Add this line!
    database="food_ordering"
)
cursor = conn.cursor()

# 1. Create menu table
cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
)
""")

# 2. Insert our food items if they aren't there
cursor.execute("SELECT COUNT(*) FROM menu_items")
if cursor.fetchone()[0] == 0:
    sql = "INSERT INTO menu_items (name, price) VALUES (%s, %s)"
    val = [
        ('Pizza', 12.99),
        ('Burger', 8.49),
        ('Pasta', 10.99)
    ]
    cursor.executemany(sql, val)
    conn.commit()
    print("✅ Seeded menu items into the database!")

# 3. Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quantity INT,
    status VARCHAR(50)
)
""")

print("✅ Database tables created successfully!")
cursor.close()
conn.close()