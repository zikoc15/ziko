class Usuario:
	def __init__(self):
		self.nombre="a"
		self.apellido="s"
		self.correo="x"
		self.clave="c"
usu=Usuario()
listausu=list()
correo="zikocazorla@gmail.com"
clave="daniel1999"
salir="salir"
for i in range (10):
	print("_______________________________")
	print("           	INICIO            ")
	print("_______________________________")
	print("")
	print("- Monitoreo")
	print("- Crear Usuario")
	print("- Escribe ('SALIR') para cerrar el programa")
	option=input()
	if option=="1":
		correo1=input('Correo: ')
		if correo==correo1:
			clave1=input('Clave: ')
			if clave==clave1:
				print("_______________________________")
				print("           	MENU              ")
				print("_______________________________")
				print("")
				print("- Registro de Usuario")
				print("- Borrar Usuario")
				print("- Cerrar el secion")
				option=input()
				if option=="1":
					for i in range(10):	
						print("_______________________________")
						print(listausu)
					cha=input('Oprime enter')
					continue
				if option=="2":
					print("")
				if option=="3":
					continue			
			else:
				print("Clave invalida")
				continue
		else:
			print("Correo no existente")
			continue
	if option=="2":
		print ("Usuario (Nombre): ")
		usu.nombre=input()
		print ("Usuario (apellido): ")
		usu.apellido=input()
		print ("Usuario (Correo): ")
		usu.correo=input()
		print ("Usuario (Clave): ")
		usu.clave=input()

		lista = ("Nombre: "+ usu.nombre +"  Apellido: "+ usu.apellido + "  Correo: "+ usu.correo +"  Clave: "+ usu.clave+"\n"+"\n")

		listausu.append(usu.nombre + usu.apellido + usu.correo + usu.clave)

		archivo=open("Registro de Usuarios.txt","a")
		archivo.write(lista)
		archivo.close()
		for i in range (100):
			print("_______________________________")
			print("           	MENU              ")
			print("_______________________________")
			print("")
			print("- SUMA")
			print("- RESTA")
			print("- MULTIPLICAR")
			print("- DIVIDIR")
			print("- SALIR DE LA CALCULADORA")
			option=input()
			num3=int()
			if option=="1":
				print("Introduce dos numeros")
				num1=int(input())
				num2=int(input())
				num3=num2+num1
				print(num1,"+",num2,"=",num3)

			if option=="2":
				print("Introduce dos numeros")
				num1=int(input())
				num2=int(input())
				num3=num2-num1
				print(num1,"-",num2,"=",num3)

			if option=="3":
				print("Introduce dos numeros")
				num1=int(input())
				num2=int(input())
				num3=num2*num1
				print(num1,"*",num2,"=",num3)

			if option=="4":
				print("Introduce dos numeros")
				num1=int(input())
				num2=int(input())
				num3=num2/num1
				print(num1,"/",num2,"=",num3)

			if option=="5":
				break
	if option=="salir":
		break