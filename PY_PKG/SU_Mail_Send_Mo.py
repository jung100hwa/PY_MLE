import smtplib
from email.message import EmailMessage

import os
import smtplib
 
from email import encoders
from email.utils import formataddr
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def SU_MO_MailSend(msgbody, msgsubject, msgaddr, fileadds):
    # STMP 서버의 url과 port 번호
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465

    # 1. SMTP 서버 연결
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

    EMAIL_ADDR = 'jung100hwa@gmail.com'
    EMAIL_PASSWORD = 'inkhmznzogvwzjbh'

    # 2. SMTP 서버에 로그인
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)


    # 3. MIME 형태의 이메일 메세지 작성
    msgaddr=['jung2hwa@naver.com','jung100hwa@gmail.com']
    message = EmailMessage()
    message["Subject"]  = msgsubject
    message.set_content(msgbody)
    message["From"]     = EMAIL_ADDR
    message["To"]       = msgaddr


    for filenm in fileadds:
        with open(filenm, 'rb') as content_file:
            content = content_file.read()
            message.add_attachment(content, maintype='application', subtype='mixd', filename=os.path.basename(filenm))

    # 4. 서버로 메일 보내기
    smtp.send_message(message)

    # 5. 메일을 보내면 서버와의 연결 끊기
    smtp.quit()