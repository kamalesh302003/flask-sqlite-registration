from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)
app.config['SECRET_KEY']='replace_this_with_a_secret_key'
DATABASE = 'pythonflask.db'

def create_table():
    conn=sqlite3.connect(DATABASE)
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reg(
        UNAME TEXT,
        EMAIL TEXT UNIQUE,
        UPASS TEXT)
    """)
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/reg',methods=['POST'])
def reg():
    if request.method=='POST':
        fullname=request.form.get('fullname')
        email=request.form.get('email')
        password=request.form.get('password')

        conn=sqlite3.connect(DATABASE)
        cursor=conn.cursor()
        cursor.execute(
            'INSERT INTO reg (UNAME,EMAIL,UPASS) VALUES (?,?,?)',
            (fullname,email,password)
        )
        conn.commit()
        conn.close()
        return render_template('success.html',title='Registration Successful',message='Your account has been created successfully.')

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        conn=sqlite3.connect(DATABASE)
        cursor=conn.cursor()
        cursor.execute('SELECT UNAME FROM reg WHERE EMAIL=? AND UPASS=?',(email,password))
        user=cursor.fetchone()
        conn.close()

        if user:
            return render_template('success.html',title='Welcome Back',message=f'Welcome,{user[0]}! You have successfully logged in.')
        error='Invalid email or password. Please try again.'
    return render_template('login.html', error=error)

if __name__=='__main__':
    create_table()
    app.run(debug=True)
