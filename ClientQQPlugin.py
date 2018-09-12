# -*- coding: utf-8 -*-
import  socket
def onQQMessage(bot,contact,member,content):
    s=socket.socket()
    port=6969
    s.connect(('127.0.0.1',port))
    if contact.ctype=='buddy' and bot.isMe(contact,member)==False:
        s.send(b"QQ message:\n"+(contact.name+'：'+content))
        bot.SendTo(contact,'Hello {}，你的信息我已经收到。请加我微信1324522527，谢谢。'.format(contact.name))
