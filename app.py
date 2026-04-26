from flask import Flask, render_template, request
import sqlite3
app=Flask(__name__)

def create_table():
    conn=sqlite3.connect("pythonflask.db")
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reg(
        UNAME TEXT,
        EMAIL TEXT,
        UPASS TEXT)
    """)
    conn.commit()
    conn.close()

@app.route('/home')
def hello_world():
    return render_template('register.html')

@app.route('/reg', methods=['POST','GET'])
def reg():
    conn=sqlite3.connect("pythonflask.db")
    cursor=conn.cursor()
    if request.method=='POST':
        uname=request.form["uname"]
        email=request.form["email"]
        upass=request.form["upass"]

        cursor.execute(
            "INSERT INTO reg(UNAME,EMAIL,UPASS) VALUES (?,?,?)",
            (uname,email,upass)
        )

        conn.commit()
        conn.close()

        return render_template('success.html')

if __name__=='__main__':
    create_table()
    app.run(debug=True)