from flask import Flask,render_template,request,send_file
import smtplib
from email.mime.text import MIMEText
import boto3

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'Sru_Portfolio'

aws_access = 'AKIAJKLZYKMALNGCZJMA'
aws_secret = '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'

client = boto3.client('sns',aws_access_key_id='AKIAJKLZYKMALNGCZJMA',aws_secret_access_key='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',region_name='us-east-1')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/home")
def start():
    return render_template('index.html')

@app.route('/downloadResume')
def download():
    return send_file('Resume.pdf',attachment_filename="SrushtiGangireddy_Resume.pdf",as_attachment=True)

@app.route('/contact',methods=["post","get"])
def contact():
    if request.method=='POST':
        print("POST")
        name=request.form.get('name')
        subject=request.form.get('subject')
        email=request.form.get('email')
        message=request.form.get('message')
        Info=name+" with email address: "+email+" has tried to contact you. \n Subject: \t"+subject+"\n Message: \t"+message;
        response = client.publish(TopicArn='arn:aws:sns:us-east-1:742600257451:SruPortfolio', Message=Info)
        return render_template('index.html')
    else:
        print("GET")
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)