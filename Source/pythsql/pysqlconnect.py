import mysql.connector
def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",     # or your MySQL host
        user="root",          # your MySQL username
        password="Mysql1485",      # your MySQL password (plain text)
        database="testDB"       # your database name
    )

    print("✅ Connected to MySQL successfully")
    conn.close()


if __name__ == "__main__":
    connect_to_mysql()