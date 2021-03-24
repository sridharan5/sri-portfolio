from flask import Flask,render_template,request
import smtplib,ssl
import os

app = Flask(__name__)

smtpServer = "smtp.gmail.com"
port = 587
myEmail = os.environ.get("MAIL")
password = os.environ.get("PASS")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/status", methods=['POST','GET'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone')
        message = request.form.get('message')
        context = ssl.create_default_context()
        msg = f"""Message from your Portfolio, 
        Name: {name}, 
        Email: {email}, 
        Phone number: {phone_number},
         Message: {message}"""
        try:
            server = smtplib.SMTP(smtpServer, port)
            server.starttls(context=context)
            server.login(myEmail, password)
            server.sendmail(from_addr=myEmail,to_addrs=myEmail,msg=msg)
        except Exception as e:
            print("the email could not be sent.")
        finally:
            return render_template("success.html")
            server.quit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run()