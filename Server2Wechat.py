import itchat
import socket
itchat.auto_login(enableCmdQR=1,hotReload=True)
s=socket.socket()
# host=socket.gethostname()
port=6969
s.bind(('127.0.0.1',port))
s.listen(5)
while True:
    conn,addr=s.accept()
    data=conn.recv(1024)
    itchat.send(data.decode('utf-8'),toUserName='filehelper')






