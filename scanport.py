
print("\nDeveloped By: Junior Mario and Diego Bernardes")
import socket as S
ip = input("Digite o IP a ser scaneado: ")
portas = input("Digite a quantidade de portas a serem scaneadas: ")

if ',' in portas: portas = portas.split(',')
elif '-' == portas: portas = range(1,65536)
elif '-' in portas:
        portas = portas.split('-')
        portas = range(int(portas[0]), int(portas[1])+1)
else: portas = [int(portas)]

socket = S.socket(S.AF_INET, S.SOCK_STREAM)
def analisa(ip, port):#faz a tentativa de conexão com a porta
	try:
		socket.connect((ip, port))
		return True
	except:
		return False
for port in portas:
        resposta = analisa(ip, int(port))
        if resposta == True:
                print('porta {port} ABERTA em {ip}'.format(port = port, ip = ip))
        else:
                print('porta {port} FECHADA em {ip}'.format(port = port, ip = ip))
