import socket
ip = '192.168.56.1'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
def scan(ip,port):
        try:
                socket.connect((ip,port))
                return True
        except:
                return None
for port in range(1,5000):
        resultado = scan(ip,port)
 
        if resultado == None:
                print('Nothing open')
        elif resultado == True:
                print('Port open: %d' %port)
                break
        else:
                print('Error')