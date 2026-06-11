import os
import time

from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "mysql"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "root"),
    "database": os.getenv("MYSQL_DATABASE", "notesdb"),
}


def get_db():
    for attempt in range(10):
        try:
            return mysql.connector.connect(**DB_CONFIG)
        except mysql.connector.Error:
            if attempt == 9:
                raise
            time.sleep(3)

@app.route('/')
def home():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("index.html", notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']

    db = get_db()
    cursor = db.cursor()
    sql = "INSERT INTO notes(content) VALUES(%s)"
    cursor.execute(sql, (note,))
    db.commit()
    cursor.close()
    db.close()

    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_note(id):

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM notes WHERE id=%s",
        (id,)
    )

    db.commit()
    cursor.close()
    db.close()

    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
