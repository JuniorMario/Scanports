import socket as S
ip = input("Digite o IP a ser scaneado: ")
final = int(input("Digite a quantidade de portas a serem scaneadas: "))
socket = S.socket(S.AF_INET, S.SOCK_STREAM)
def analisa(ip, port):#faz a tentativa de conexão com a porta
	try:
		S.connect((ip, port))
		return True
	except:
		return None
for port in range(0, final):#gera o numero das portas
	answer = analisa(ip, port)#envia a porta para a função analisa
	if answer == None:#verifica a resposta
		print('Nothing open')
	elif answer == True:
		print('Port open:', port)
		break
	else:
		print('Error')		
