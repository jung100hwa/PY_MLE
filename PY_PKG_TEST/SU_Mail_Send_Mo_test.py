import sys
sys.path.append("c:\\work\\PLangVim")
import os
import PY_PKG.SU_Mail_Send_Mo as SC

 
if __name__ == '__main__':
  
    attachments = [os.path.join( os.getcwd(),'aa.txt' ), os.path.join( os.getcwd(),'bb.txt' )]
    msgsubject = "주제"
    msgbody    = "메일테스트 최종 더럽게 안되네_1"
    msgaddr    = "jung2hwa@naver.com,jung100hwa@gmail.com"
    SC.SU_MO_MailSend(msgsubject, msgbody, msgaddr, attachments)