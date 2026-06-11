from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="host.docker.internal",
    user="root",
    password="root",
    database="notesdb"
)

cursor = db.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()
    return render_template("index.html", notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']

    sql = "INSERT INTO notes(content) VALUES(%s)"
    cursor.execute(sql, (note,))
    db.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_note(id):

    cursor.execute(
        "DELETE FROM notes WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)