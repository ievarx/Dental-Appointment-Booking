from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'secret_key_here'  # يُستخدم لتشفير رسائل الفلاش

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dentist_appointments'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        appointment_type = request.form['appointment_type']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appointments (date, time, name, age, gender, phone, email, address, appointment_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, time, name, age, gender, phone, email, address, appointment_type))
        mysql.connection.commit()
        cur.close()

        flash('تم حجز الموعد بنجاح', 'success')  # عرض رسالة فلاش بنجاح الحجز
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
