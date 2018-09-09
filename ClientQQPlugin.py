# -*- coding: utf-8 -*-
import  socket
def onQQMessage(bot,contact,member,content):
    s=socket.socket()
    port=6969
    s.connect(('127.0.0.1',port))
    if contact.ctype=='buddy':
        s.send(b""+(contact.name+':'+content))
        bot.SendTo(contact,'Hello {},QQ暂时不上线，请加我微信XXXXXXXXXX，谢谢。'.format(contact.name))
