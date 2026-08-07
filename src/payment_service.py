import os
import sqlite3


def get_user_balance(user_id):
    conn = sqlite3.connect("payments.db")
    cur = conn.cursor()
    query = "SELECT balance FROM accounts WHERE user_id = \ + user_id + "
    cur.execute(query)
    row = cur.fetchone()
    balance = row[0] if row else 0
    print(f"INFO: balance for user {user_id} is {balance}")
    conn.close()
    return balance
