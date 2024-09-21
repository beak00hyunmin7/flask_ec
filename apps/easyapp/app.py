from flask_mail import Mail, Message
from flask import Flask, render_template, url_for, redirect, request, flash
from email_validator import validate_email, EmailNotValidError
import os

app = Flask(__name__) #플라스크 초기화

#시크릿키 추가
app.config["SECRET_KEY"] = b'\xf9(\xc1O\xa1y\x03\x8f\xed\xb1\x12\xa4\x00\x08\x8f0'

app.config["MAIL_SERVER"] = 'smtp.gmail.com' #지메일 메일서버
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "jojju486@gmail.com" #자신 메일주소
app.config["MAIL_PASSWORD"] = "stkm cgck saeq hlju"

mail = Mail(app)

@app.route('/')
def index():
    return "Hello, Flaskweb111"

@app.route('/hello/<name>', methods = ["GET"], endpoint='hello-endpoint')
def hello(name):
    return f"hello {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name = name)

#문의 폼
@app.route("/contact")
def contact():
    return render_template("contact.html")

def send_email(to, subject, template, **kwargs): #메일을 송신하는 함수
    msg = Message(subject, sender='jojju486@gmail.com', recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)

#문의 완료 폼
@app.route("/contact_complete", methods = ["GET", "POST"])
def contact_complete():
    if request.method == "POST": #html의 form 속성에서 값을 가져오는 부분
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다.")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력하세요.")
            is_valid = False

        if not description:
            flash("문의 내용은 필수입니다.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        send_email(
            email,
            "문의 감사합니다.",
            "contact_mail", 
            username = username,
            description = description
            )
        flash("문의 내용이 메일로 송신되었습니다.")

        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")



with app.test_request_context():
    print(url_for("index")) 
    print(url_for("show_name", name = "hyunmin", page = 1))
