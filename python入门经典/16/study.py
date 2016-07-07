#coding=utf-8
import smtplib,os,sys,mimetypes,email

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email import encoders
from email.message import Message

img_path = 'e:/temp/python.jpg'
txt_path = 'c:/a.txt'
from_addr = 'hw1932@163.com'
username = 'hw1932@163.com'
to_addr = '947412461@qq.com'
mail_subject = '这是邮件题目'
mail_body = 'this is the body of the message!'
pwd = 'a123456'
host = 'smtp.163.com'
port = 25

#标准正文邮件
def mail_MIMEText():
    msg = MIMEText(mail_body)#生成邮件对象，mail_body是邮件正文
    msg['subject'] = mail_subject#定义邮件主题
    msg['from'] = from_addr
    msg['to'] = to_addr

    sender = smtplib.SMTP(host,port)
    sender.login(username,pwd)
    #所有MIME****的对象都要调用as_string()方法才能作为sendmail()的方法，如下
    #sender.sendmail(from_addr,to_addr,msg.as_string())
    sender.send_message(msg)#send_message方法收发地址从msg中获取
    sender.close()

#最简单的邮件，没有用到邮件对象，只有邮箱发送对象sender
def mail_msg():
    try:
        msg = 'Subject: 0621\n\nThis is the body of the message!'
        sender = smtplib.SMTP(host,port)
        sender.login(from_addr,pwd)
        sender.sendmail(from_addr,to_addr,msg)
        sender.close()
        return 1
    except Exception as error:
        print(error)
        return 0

#Message类发送普通邮件
def mail_message():
    try:
        message = Message()
        message['Subject'] = mail_subject
        message.set_payload(mail_body)
        print(str(message))
        sender = smtplib.SMTP(host,port)
        sender.login(username,pwd)
        sender.sendmail(from_addr,to_addr,message.as_string())
        sender.close()
        return 1
    except Exception as e:
        print(e)
        return 0
#276-277
def quopri_base64():
    import base64,quopri
    encoded = quopri.encodestring(bytes('i will hava just a soupcon of soup.','utf-8'))
    print('quopri.encodestring(bytes()):',encoded)
    print('quopri.decodestring(encoded):',quopri.decodestring(encoded))

    encoded_base64 = base64.encodebytes(bytes('i will hava just a soupcon of soup.','utf-8'))
    print('base64.encodestring(bytes()):',encoded_base64)
    print('base64.decodestring(encoded):',base64.decodebytes(encoded_base64))

#278-279
#发送一个图片附件,收到的不是图片，有BUG
def mail_img():
    msg = MIMEMultipart()
    msg['from'] = from_addr
    msg['to'] = to_addr
    msg['subject'] = mail_subject

    pic = open(img_path,'rb')
    img = MIMEImage(pic.read())
    pic.close()
    print(str(msg))
    msg.attach(img)

    sender = smtplib.SMTP(host,port)
    sender.login(username,pwd)
    sender.send_message(msg)
    #sender.sendmail(from_addr,to_addr,msg.as_string())
    sender.close()

#未能携带附件
def mail_txt_MIMEText():
    fp = open(txt_path,'rb')
    msg = MIMEText(fp.read(),'base64','utf-8')
    fp.close()
    msg['from'] = from_addr
    msg['to'] = to_addr
    msg['subject'] = 'mail_fujian'

    sender = smtplib.SMTP(host,port)
    sender.login(username,pwd)
    #sender.send_message(msg)
    sender.sendmail(from_addr,to_addr,msg.as_string())
    sender.close()

#未能附件
def mail_txt_MIMEMultipart():
    msg = MIMEMultipart()
    msg['from'] = from_addr
    msg['to'] = to_addr
    msg['subject'] = 'mail_text()'

    txt = open(txt_path,'rb')
    mail_txt = MIMEText(txt.read(),'base64','utf-8')#必须指定邮件编码类型和文本的类型
    txt.close()
    msg.attach(mail_txt)

    sender = smtplib.SMTP(host,port)
    sender.login(username,pwd)
    #sender.send_message(msg)
    sender.sendmail(from_addr,to_addr,msg.as_string())
    sender.close()

#发送正文+图片的邮件
def mail_txt_img():
    msg = MIMEMultipart()
    # msg['from'] = from_addr
    # msg['to'] = to_addr
    msg['subject'] = mail_subject

    text = MIMEText(mail_body)
    msg.attach(text)

    img = open(img_path,'rb')
    image = MIMEImage(img.read())
    img.close()
    print(str(img))
    #img_name = (os.path.split(img_path)[1])#图片名称
    msg.attach(image)

    sender = smtplib.SMTP(host,port)
    sender.login(username,pwd)
    sender.sendmail(from_addr,to_addr,msg.as_string())
    sender.close()


if __name__ == '__main__':
    pass
    #mail_txt_img()
    #quopri_base64()
    #mail_message()
    #mail_txt_MIMEMultipart()
    #mail_MIMEText()
    #mail_img()
    #mail_txt_MIMEText()