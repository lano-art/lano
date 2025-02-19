from flask import Flask, render_template, request, redirect, url_for
from user_handler import UserHandler
from lessons_manager import LessonsManager

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('signin.html')  # صفحة تسجيل الدخول


@app.route('/signup')
def signup():
    return render_template('signup.html')  # صفحة إنشاء حساب


@app.route('/signup', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    user_handler = UserHandler()
    success, message = user_handler.create_user(username, password)

    if success:
        return redirect(url_for('home'))  # بعد التسجيل الناجح، إعادة التوجيه إلى صفحة تسجيل الدخول
    else:
        return message  # عرض رسالة الخطأ


@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']

    user_handler = UserHandler()
    success, message = user_handler.login_user(username, password)

    if success:
        return render_template('homepage.html', username=username)  # صفحة الترحيب بعد تسجيل الدخول
    else:
        return message  # عرض رسالة الخطأ


@app.route('/draw')
def draw():
    return render_template('draw_canvas.html')  # صفحة الرسم التفاعلي


if __name__ == '__main__':
    app.run(debug=True)
