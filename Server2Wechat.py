import itchat
import socket
itchat.auto_login(enableCmdQR=2,picDir=b'C:\Users\Administrator\Pictures\QR.png',hotReload=True)
s=socket.socket()
# host=socket.gethostname()
port=6969
s.bind(('127.0.0.1',port))
s.listen(5)
while True:
    conn,addr=s.accept()
    data=conn.recv(1024)
    itchat.send(data.decode('utf-8'),toUserName='filehelper')




