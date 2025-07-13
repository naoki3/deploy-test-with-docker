from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    db_host = os.getenv('DB_HOST', 'xxx.x.x.x')
    db_port = os.getenv('DB_PORT', 'xxxx')
    db_name = os.getenv('DB_NAME', 'xxxxxxxx')
    db_user = os.getenv('DB_USER', 'xxxxxxxx')
    db_password = os.getenv('DB_PASSWORD', 'xxxxxxx')
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, message FROM messages")

    messages = ""
    records = cursor.fetchall()
    for row in records:
        messages = messages + row[1] + ","
    cursor.close()

    return messages