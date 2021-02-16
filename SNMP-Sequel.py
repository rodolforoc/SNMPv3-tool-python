from easysnmp import Session

def snmpv3():
	ip = input('\nEntre com o endereço de IP: ')

	oid = input('\nEntre com o OID ou MIB para prosseguir: ')

	# Criando uma sessão SNMPv3 no dispositivo
	session = Session(hostname = ip, version = 3, security_level = "auth_with_privacy", security_username = "rodolfo", auth_protocol = "SHA", auth_password = "shapass1234", privacy_protocol = "AES", privacy_password = "aespass1234")

	return oid, session

while True:
	print('\nEscolha a operação SNMP que deseja executar:\n\ng - SNMP GET\nw - SNMP WALK\ns - SNMP SET\ne - Sair do Programa')

	user_choice = input('\nDigite sua escolha: ')
    
  #SNMP GET
	if user_choice == 'g':
		snmp = snmpv3()
		oid = snmp[0]
		session = snmp[1]

		#Performing SNMP GET
		snmp_get = session.get(oid)

		result = snmp_get.value

		print('\nO resultado do SNMP GET em {} é:'.format(oid))
		print('\n' + result + '\n')

		continue
    
  #SNMP WALK
	elif user_choice == 'w':
		snmp = snmpv3()
		oid = snmp[0]
		session = snmp[1]

		snmp_walk = session.walk(oid)

		print('\nO resultado do SNMP WALK em {} é:'.format(oid))

		for obj in snmp_walk:
			result = obj.value
			print('\n' + result)

		continue

	#SNMP SET
	elif user_choice == "s":
		snmp = snmpv3()
		oid = snmp[0]
		session = snmp[1]

		value = input("\nEntre com o valor para o objeto: ")

		snmp_set = session.set(oid, value)

		print("\nCompleto. Por favor verifique a configuração do dispositivo.")

		continue

	elif user_choice == 'e':
		print('\nSaindo do programa...\n')

		break

	else:
		print('\nOpção inválida. Tente novamente!\n')

		continue
