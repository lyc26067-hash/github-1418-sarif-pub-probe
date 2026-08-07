import sqlite3

def get_balance(user_id):
    conn = sqlite3.connect("payments.db")
    cur = conn.cursor()
    query = "SELECT balance FROM accounts WHERE user_id = '" + user_id + "'
    cur.execute(query)
    row = cur.fetchone()
    balance = row[0] if row else 0
    conn.close()
    return balance
