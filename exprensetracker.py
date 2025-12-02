import sqlite3

conn=sqlite3.connect("expenses.db")
cur=conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             amount REAL,
             category TEXT,
             date TEXT,
             note TEXT
            )""")


def add_expenses(amount, category, date, note):
    cur.execute("INSERT INTO expenses (amount, category, date, note) VALUES (?,?,?,?)",(amount, category, date, note))
    conn.commit()
    print("Expense added successfully")

def view_expenses():
    cur.execute("SELECT * FROM EXPENSES")
    rows=cur.fetchall()
    for i in rows:
        print(i)

def total_expense():
    cur.execute("SELECT SUM(amount) FROM expenses")
    print("Total Expense:", cur.fetchone()[0])

def expense_by_category(category):
    cur.execute("SELECT SUM(amount) FROM expenses WHERE category=?", (category,))
    print(f"Total {category} expense:", cur.fetchone()[0])

def monthly_expense(month):
    cur.execute("SELECT SUM(amount) FROM expenses WHERE date LIKE ?", (f"{month}%",))
    print(f"Total in {month}:", cur.fetchone()[0])


