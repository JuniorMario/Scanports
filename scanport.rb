require 'socket'
def connect(ip, port)
	begin
		con = TCPSocket.open(ip, port)
		return true
	rescue Errno::ECONNREFUSED
		return false
	end
end
STDOUT.print '[IP a ser Scaneado]:' 
ip = gets.chomp
STDOUT.print '[Digite as portas a serem Scaneadas]:'
porta = gets.chomp
if porta.include? '-'
	porta = porta.split('-')
	portas = porta[0].to_i...porta[1].to_i
	puts portas
elsif porta.include? ","
	arra = []
	porta = porta.split(',')
	for ara in porta
		arra << ara 	
	end
	portas = arra
else
	puts "Use - para percorrer as portas e , para portas especificas"
end
for port in portas
	answer = connect(ip, port)
	if answer == true
		puts "Porta #{port} aberta em #{ip}"
	elsif answer == false
		puts "Porta #{port} fechada em #{ip}"
	else
		puts "Nada esta sendo retornado. :("
	end
end