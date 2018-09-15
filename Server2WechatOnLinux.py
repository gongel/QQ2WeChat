import itchat
import socket
#阿里云linux服务器上hotReload只能为False，picDir为微信登录二维码的存储地址，便于发送到邮箱
itchat.auto_login(enableCmdQR=2,picDir='/root/QR.png',hotReload=False)
s=socket.socket()
# host=socket.gethostname()
port=6969
s.bind(('127.0.0.1',port))
s.listen(5)
while True:
    conn,addr=s.accept()
    data=conn.recv(1024)
    itchat.send(data.decode('utf-8'),toUserName='filehelper')




