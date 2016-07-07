import smtplib

# server = smtplib.SMTP('smtp.163.com')
# server.login('hw1932@163.com','a123456')
# msg = 'subject:0617'
# server.sendmail('hw1932@163.com','hw1932@163.com',msg)
# server.close



server = smtplib.SMTP('smtp.163.com',25)
server.login('hw1932@163.com','a123456')
msg = 'Subject:0617'
server.sendmail('hw1932@163.com','hw1932@163.com',msg)
server.close