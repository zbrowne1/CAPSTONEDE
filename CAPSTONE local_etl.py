
import pandas as pd
import psycopg2

# -------------------------------
# CONFIGURATION
# -------------------------------
CUSTOMERS_FILE = 'customers.csv'
ORDERS_FILE = 'orders.csv'
ORDER_ITEMS_FILE = 'order_items.csv'

DB_CONFIG = {
    'dbname': 'sales-data-zora',
    'user': 'postgres',
    'password': 'JoelticA2',
    'host': '35.192.75.27',
    'port': '5432'
}

# -------------------------------
# DATABASE CONNECTION
# -------------------------------
def connect_db(config):
    return psycopg2.connect(**config)

# -------------------------------
# MAIN ETL FUNCTION
# -------------------------------
def run_etl():
    # Load data from local CSV files
    customers_df = pd.read_csv(CUSTOMERS_FILE)
    orders_df = pd.read_csv(ORDERS_FILE)
    order_items_df = pd.read_csv(ORDER_ITEMS_FILE)

    conn = connect_db(DB_CONFIG)
    cursor = conn.cursor()

    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS order_items, orders, customers CASCADE;")

    # Create tables
    cursor.execute("""
        CREATE TABLE customers (
            customer_id SERIAL PRIMARY KEY,
            full_name VARCHAR(150),
            email VARCHAR(100),
            signup_date DATE,
            region VARCHAR(100)
        );
    """)

    cursor.execute("""
        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            customer_id INT REFERENCES customers(customer_id),
            order_date TIMESTAMP,
            total_amount NUMERIC(10, 2)
        );
    """)

    cursor.execute("""
        CREATE TABLE order_items (
            order_item_id SERIAL PRIMARY KEY,
            order_id INT REFERENCES orders(order_id),
            product_name VARCHAR(200),
            quantity INT,
            unit_price NUMERIC(10, 2),
            total_price NUMERIC(10, 2)
        );
    """)

    # Insert data
    for _, row in customers_df.iterrows():
        cursor.execute(
            "INSERT INTO customers (customer_id, full_name, email, signup_date, region) VALUES (%s, %s, %s, %s, %s)",
            tuple(row)
        )

    for _, row in orders_df.iterrows():
        cursor.execute(
            "INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES (%s, %s, %s, %s)",
            tuple(row)
        )

    for _, row in order_items_df.iterrows():
        cursor.execute(
            "INSERT INTO order_items (order_item_id, order_id, product_name, quantity, unit_price, total_price) VALUES (%s, %s, %s, %s, %s, %s)",
            tuple(row)
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("ETL completed successfully.")

if __name__ == "__main__":
    run_etl()
