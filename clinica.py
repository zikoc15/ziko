class Usuario:
	def __init__(self):
		self.nombre="a"
		self.apellido="b"
		self.cedula="c"
		self.genero="d"
		self.telefono="e"
		self.edad="f"
		self.fn="g"
		self.pr="h"

usu=Usuario()

caso=list()
pais=list()
p=int(0)
LISTA_Sintomas=list()
dias="dias"
dia="dia"	
semanas="semanas"
semana="semana"
meses="meses"
mes="mes"
num_sospechoso=int(0)
num_descartado=int(0)
num_confirmado=int(0)
num_recuperado=int(0)
num_fallecido=int(0)
tercera=int(0)
pmenor=int(0)
ptotal=int(0)
P1=int(0)
P2=int(0)
P3=int(0)
P4=int(0)
P5=int(0)
Sospechosos=list()
Descartados=list()
confirmados=list()
Fallecidos=list()
Recuperados=list()
lista_pasientes=list()
grado1=int(0)
grado2=int(0)
grado3=int(0)
espacio="  "
for i in range(1000):
	print("")
	print("_______________________________")
	print("_______________________________")
	print("         CLINICA MOVIL         ")
	print("_______________________________")
	print("_______________________________")
	print("")
	print("-INFORMACION")
	print("-CHEQUEO")
	print("-SALIR (Escribir SALIR para cerrar el programa)")
	option=input()
	if option=="1":
		print("")
		print("_______________________________")
		print("          INFORMACION          ")
		print("_______________________________")
		user=input('Usuario: ')
		if user=="ziko":
			clave=input('Contraseña: ')
			if clave=="1999":
				for i in range(1000):
					print("")
					print("_______________________________")
					print("          INFORMACION          ")
					print("_______________________________")
					print("")
					print("-Planeta (Casos [" ,p, "])")
					print("-CASOS [" ,ptotal, "]")
					print("-Cerrar seccion")
					option=input()
					if option=="1":
						for i in pais:
							print("Se han registrado [" ,len(pais), "] en todo el mundo")
							print("")
							buscar=input('Bucador: ')
							if buscar in pais:
								print("En " ,buscar, " existen: " ,pais.count(buscar), " casos de CORONAVIRUS")
							print("")
							continue
					
					if option=="2":
						print("")
						print("_______________________________")
						print("          INFORMACION          ")
						print("_______________________________")
						print("-Niños[" ,pmenor, "]")
						print("-Adultos[" ,P5, "]")
						print("-Tercera edad[" ,tercera, "]")
						print("-SALIR")
						option=input()
						if option=="1":
							print("")
							print("_______________________________")
							print("          INFORMACION          ")
							print("_______________________________")
							for i in range(1000):
								print("-Sospechosos[" ,num_sospechoso, "]")
								print("-Descartados[" ,num_descartado, "]")
								print("-confirmados[" ,num_confirmado, "]")
								print("-Recuperados[" ,num_recuperado, "]")
								print("-Fallecidos[" ,num_fallecido, "]")
								print("-SALIR")
								option=input()
								if option=="1":
									
									print("")
									print(Sospechosos)
									print("")
									continue
								if option=="2":
									
									print("")
									print(Descartados)
									print("")
									continue
								if option=="3":
									
									print("")
									print(confirmados)
									print("")
									continue
								if option=="4":
									
									print("")
									print(Recuperados)
									print("")
									continue
								if option=="5":
									
									print("")
									print(Fallecidos)
									print("")
									continue
								if option=="6":
									break
						if option=="2":
							print("")
							print("_______________________________")
							print("          INFORMACION          ")
							print("_______________________________")
							for i in range(1000):
								print("-Sospechosos[" ,num_sospechoso, "]")
								print("-Descartados[" ,num_descartado, "]")
								print("-confirmados[" ,num_confirmado, "]")
								print("-Recuperados[" ,num_recuperado, "]")
								print("-Fallecidos[" ,num_fallecido, "]")
								print("-SALIR")
								option=input()
								if option=="1":
									
									print("")
									print(Sospechosos)
									print("")
									continue
								if option=="2":
									
									print("")
									print(Descartados)
									print("")
									continue
								if option=="3":
									
									print("")
									print(confirmados)
									print("")
									continue
								if option=="4":
									
									print("")
									print(Recuperados)
									print("")
									continue
								if option=="5":
									
									print("")
									print(Fallecidos)
									print("")
									continue
								if option=="6":
									break
						if option=="3":
							print("")
							print("_______________________________")
							print("          INFORMACION          ")
							print("_______________________________")
							for i in range(1000):
								print("-Sospechosos[" ,num_sospechoso, "]")
								print("-Descartados[" ,num_descartado, "]")
								print("-confirmados[" ,num_confirmado, "]")
								print("-Recuperados[" ,num_recuperado, "]")
								print("-Fallecidos[" ,num_fallecido, "]")
								print("-SALIR")
								option=input()
								if option=="1":
									
									print("")
									print(Sospechosos)
									print("")
									continue
								if option=="2":
									
									print("")
									print(Descartados)
									print("")
									continue
								if option=="3":
									
									print("")
									print(confirmados)
									print("")
									continue
								if option=="4":
									
									print("")
									print(Recuperados)
									print("")
									continue
								if option=="5":
									
									print("")
									print(Fallecidos)
									print("")
									continue
								if option=="6":
									break
						if option=="4":
							break
					if option=="3":
						break
			else:
				print("")
				print("Contraseña invalida")
				print("")
				continue
		else:
			print("")
			print("Usuario invalido")
			print("")
			continue

	if option=="2":

		usu.nombre=input('Pasiente (Nombre): ')
		lista_pasientes.append(usu.nombre)
		usu.apellido=input('Pasiente (apellido): ')
		lista_pasientes.append(usu.apellido)
		usu.cedula=input('Cedula de identidad: ')
		lista_pasientes.append(usu.cedula)
		for i in range(1000):
			usu.edad=input('Edad: ')
			lista_pasientes.append(usu.edad)
			if usu.edad<="17" and usu.edad >="12":
				
				P1=P1+1
				persona="Adolecente"
				break
			if usu.edad<="12" and usu.edad >="9":					
					
				P2=P2+1
				persona="Pre-adolecente"
				break
			if usu.edad<="9" and usu.edad >="4":						
						
				P3=P3+1
				persona="Niño"
				break
			if usu.edad<="4":
						
				P4=P4+1
				persona="Bebe"
				break
			if usu.edad>="18" and usu.edad <="60":
					
				P5=P5+1
				persona="Adulto"
				break
			if usu.edad>="60" and usu.edad <="80":
				persona="Tercera edad"
				Alarma="Grado 1"
						
				grado1=grado1+1
				break
			if usu.edad>="80" and usu.edad <="90":
				persona="Tercera edad"
				Alarma="Grado 2"						
							
				grado2=grado2+1						
				break
			if usu.edad>="90":
				persona="Tercera edad"
				Alarma="Grado 3"
								
				grado3=grado3+1	
				num_fallecido=num_fallecido+1
				Fallecidos.append([lista_pasientes])				
				break
			else:
				print("No ha introducido una edad")
				continue

		tercera=tercera+grado1+grado2+grado3		
		pmenor=pmenor+P1+P2+P3+P4					
		ptotal=ptotal+pmenor+P5+tercera
		for i in range(1000):			
			usu.genero=input('Genero: ')
			if usu.genero=="Hombre":
				hombre=int(0)
				hombre=hombre+1
				break
			elif usu.genero=="Mujer":
				if usu.genero=="Mujer":
					mujer=int(0)
					mujer=mujer+1
					break
				else:
					otro=int(0)
					otro=otro+1
					break
			else:
				print("Recuerde responer con mayuscula (Hombre/Mujer)")
				continue
		lista_pasientes.append(usu.genero)
		usu.telefono=input('Numero de telefono: ')
		lista_pasientes.append(usu.telefono)
		usu.fn=input('Fecha de nacimiento: ')
		lista_pasientes.append(usu.fn)
		usu.pr=input('Pais recidencial: ')
		p+=1
		lista_pasientes.append(usu.pr)
		pais.append(usu.pr)
		if usu.edad>="90":
			print("Listo siguinte....!")
			continue
		else:			
			for i in range(1000):
				print("")
				print("_______________________________")
				print("         CUESTIONARIO          ")
				print("_______________________________")		
				print("-Sintomas")
				print("-Lista de pasientes registrados")
				print("-Atencion")
				print("-SALIR & GUARDAR")
				option=input()

				if option=="1":
					print("_______________________________")
					print("          CONVID-19            ")
					print("_______________________________")
					C_leve=["Fiebre","Cansancio","Tos seca","Congestion nasal","Rinorrea","Dolor de Garganta","Diarrea"]
					print("CONVID-19 [LEVE]:")
					print("")
					print(C_leve)
					print("")
					print("CONVID-19 [GRAVE]:")
					C_grave=["Fiebre","Escalosfrios","Tos seca","Dificultad respiratoria","Dolor de cabeza"]
					print("")
					print(C_grave)
					print("")				
				if option=="2":
					print("_______________________________")
					print("      LISTA DE PASIENTES       ")
					print("_______________________________")
					print("")
					print(lista_pasientes)
					print("")
				if option=="3":
					print("")
					print("_______________________________")
					print("Pasiente: ",usu.nombre," ",usu.apellido)
					print("_______________________________")
					act=int(0)
					negt=int(0)		
					if usu.edad <= "17":
						print("Porfavor 'RESPONDER' (SI/NO)")
						for i in range(1000):				
							fiebre=input('Ah sentido fiebre?: ')
							if fiebre == "si":
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre == "Si":
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre =="SI":								
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							if fiebre == "no":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre == "No":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre =="NO":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):						
							escalosfrios=input('No has tenido encalosfrios o fiebre interna?: ')
							if escalosfrios == "si":
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios == "Si":
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios =="SI":								
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							if escalosfrios == "no":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios == "No":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios=="NO":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):
							dolor_cabeza=input('Te ha dolido la cabeza?: ')
							if dolor_cabeza == "si":
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza == "Si":
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza =="SI":								
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							if dolor_cabeza == "no":
								dolor_cabeza = "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza == "No":
								dolor_cabeza = "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza=="NO":
								dolor_cabeza= "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):			
							Cansancio=input('Ah sentido Cansancio?: ')
							if Cansancio == "si":
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio == "Si":
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio =="SI":								
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							if Cansancio == "no":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio == "No":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio=="NO":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):						
							tos_seca=input('Ah tenido tos seca o con poca flema?: ')
							if tos_seca == "si":
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca == "Si":
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca =="SI":								
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							if tos_seca == "no":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca == "No":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca =="NO":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							dificultad_respiratoria=input('Siente dificultad respiratoria?: ')
							if dificultad_respiratoria == "si":
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria == "Si":
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria =="SI":								
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							if dificultad_respiratoria == "no":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria == "No":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria=="NO":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							congestios_nasal=input('Siente congestion nasal?: ')
							if congestios_nasal == "si":
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal == "Si":
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal =="SI":								
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							if congestios_nasal == "no":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal == "No":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal=="NO":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							dolor_garganta=input('Te duele la gargante?: ')
							if  dolor_garganta == "si":
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif dolor_garganta == "Si":
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta =="SI":								
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							if  dolor_garganta == "no":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta == "No":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta=="NO":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							rinorrea=input('Ah tenido rinorea?: ')
							if  rinorrea == "si":
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif  rinorrea == "Si":
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif rinorrea  =="SI":								
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							if rinorrea == "no":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif  rinorrea == "No":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif rinorrea =="NO":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							diarrea=input('Ah tenido diarrea?: ')
							if  diarrea == "si":
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif  diarrea == "Si":
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif diarrea =="SI":								
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							if diarrea == "no":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif  diarrea == "No":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif diarrea=="NO":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue									
					elif usu.edad >="18" and usu.edad <= "60":		
						print("Porfavor 'RESPONDER' (SI/NO)")
						for i in range(1000):				
							fiebre=input('Ah sentido fiebre?: ')
							if fiebre == "si":
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre == "Si":
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre =="SI":								
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							if fiebre == "no":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre == "No":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre =="NO":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):						
							escalosfrios=input('No has tenido encalosfrios o fiebre interna?: ')
							if escalosfrios == "si":
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios == "Si":
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios =="SI":								
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							if escalosfrios == "no":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios == "No":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios=="NO":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):
							dolor_cabeza=input('Te ha dolido la cabeza?: ')
							if dolor_cabeza == "si":
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza == "Si":
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza =="SI":								
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							if dolor_cabeza == "no":
								dolor_cabeza = "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza == "No":
								dolor_cabeza = "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza=="NO":
								dolor_cabeza= "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):			
							Cansancio=input('Ah sentido Cansancio?: ')
							if Cansancio == "si":
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio == "Si":
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio =="SI":								
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							if Cansancio == "no":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio == "No":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio=="NO":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):						
							tos_seca=input('Ah tenido tos seca o con poca flema?: ')
							if tos_seca == "si":
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca == "Si":
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca =="SI":								
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							if tos_seca == "no":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca == "No":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca =="NO":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							dificultad_respiratoria=input('Siente dificultad respiratoria?: ')
							if dificultad_respiratoria == "si":
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria == "Si":
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria =="SI":								
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							if dificultad_respiratoria == "no":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria == "No":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria=="NO":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							congestios_nasal=input('Siente congestion nasal?: ')
							if congestios_nasal == "si":
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal == "Si":
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal =="SI":								
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							if congestios_nasal == "no":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal == "No":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal=="NO":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							dolor_garganta=input('Te duele la gargante?: ')
							if  dolor_garganta == "si":
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif dolor_garganta == "Si":
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta =="SI":								
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							if  dolor_garganta == "no":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta == "No":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta=="NO":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							rinorrea=input('Ah tenido rinorea?: ')
							if  rinorrea == "si":
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif  rinorrea == "Si":
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif rinorrea  =="SI":								
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							if rinorrea == "no":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif  rinorrea == "No":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif rinorrea =="NO":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							diarrea=input('Ah tenido diarrea?: ')
							if  diarrea == "si":
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif  diarrea == "Si":
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif diarrea =="SI":								
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							if diarrea == "no":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif  diarrea == "No":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif diarrea=="NO":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue	
					elif usu.edad >= "60" and usu.edad <= "73":
						print("Porfavor 'RESPONDER' (SI/NO)")
						for i in range(1000):				
							fiebre=input('Ah sentido fiebre?: ')
							if fiebre == "si":
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre == "Si":
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre =="SI":								
								fiebre = "Fiebre: SI"
								act+=1
								LISTA_Sintomas.append(fiebre)
								break
							if fiebre == "no":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre == "No":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							elif fiebre =="NO":
								fiebre = "Fiebre: NO"
								negt+=1
								LISTA_Sintomas.append(fiebre)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):						
							escalosfrios=input('No has tenido encalosfrios o fiebre interna?: ')
							if escalosfrios == "si":
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios == "Si":
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios =="SI":								
								escalosfrios = "Escalosfrios: SI"
								act+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							if escalosfrios == "no":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios == "No":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							elif escalosfrios=="NO":
								escalosfrios = "Escalosfrios: NO"
								negt+=1
								LISTA_Sintomas.append(escalosfrios)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):
							dolor_cabeza=input('Te ha dolido la cabeza?: ')
							if dolor_cabeza == "si":
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza == "Si":
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza =="SI":								
								dolor_cabeza = "Dolor de cabeza: SI"
								act+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							if dolor_cabeza == "no":
								dolor_cabeza = "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza == "No":
								dolor_cabeza = "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							elif dolor_cabeza=="NO":
								dolor_cabeza= "Dolor de cabeza: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_cabeza)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):			
							Cansancio=input('Ah sentido Cansancio?: ')
							if Cansancio == "si":
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio == "Si":
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio =="SI":								
								Cansancio = "Cansancio: SI"
								act+=1
								LISTA_Sintomas.append(Cansancio)
								break
							if Cansancio == "no":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio == "No":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							elif Cansancio=="NO":
								Cansancio = "Cansancio: NO"
								negt+=1
								LISTA_Sintomas.append(Cansancio)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range(1000):						
							tos_seca=input('Ah tenido tos seca o con poca flema?: ')
							if tos_seca == "si":
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca == "Si":
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca =="SI":								
								tos_seca = "Tos seca: SI"
								act+=1
								LISTA_Sintomas.append(tos_seca)
								break
							if tos_seca == "no":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca == "No":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							elif tos_seca =="NO":
								tos_seca = "Tos seca: NO"
								negt+=1
								LISTA_Sintomas.append(tos_seca)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							dificultad_respiratoria=input('Siente dificultad respiratoria?: ')
							if dificultad_respiratoria == "si":
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria == "Si":
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria =="SI":								
								dificultad_respiratoria = "Dificultad respiratoria: SI"
								act+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							if dificultad_respiratoria == "no":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria == "No":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							elif dificultad_respiratoria=="NO":
								dificultad_respiratoria = "Dificultad respiratoria: NO"
								negt+=1
								LISTA_Sintomas.append(dificultad_respiratoria)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							congestios_nasal=input('Siente congestion nasal?: ')
							if congestios_nasal == "si":
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal == "Si":
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal =="SI":								
								congestios_nasal = "Congestion nasal: SI"
								act+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							if congestios_nasal == "no":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal == "No":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							elif congestios_nasal=="NO":
								congestios_nasal = "Congestion nasal: NO"
								negt+=1
								LISTA_Sintomas.append(congestios_nasal)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							dolor_garganta=input('Te duele la gargante?: ')
							if  dolor_garganta == "si":
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif dolor_garganta == "Si":
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta =="SI":								
								dolor_garganta = "Dolor de garganta: SI"
								act+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							if  dolor_garganta == "no":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta == "No":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							elif  dolor_garganta=="NO":
								dolor_garganta = "Dolor de garganta: NO"
								negt+=1
								LISTA_Sintomas.append(dolor_garganta)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							rinorrea=input('Ah tenido rinorea?: ')
							if  rinorrea == "si":
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif  rinorrea == "Si":
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif rinorrea  =="SI":								
								rinorrea  = "Rinorrea: SI"
								act+=1
								LISTA_Sintomas.append(rinorrea)
								break
							if rinorrea == "no":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif  rinorrea == "No":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							elif rinorrea =="NO":
								rinorrea  = "Rinorrea: NO"
								negt+=1
								LISTA_Sintomas.append(rinorrea)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue

						for i in range (1000):
							diarrea=input('Ah tenido diarrea?: ')
							if  diarrea == "si":
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif  diarrea == "Si":
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif diarrea =="SI":								
								diarrea = "Diarrea: SI"
								act+=1
								LISTA_Sintomas.append(diarrea)
								break
							if diarrea == "no":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif  diarrea == "No":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							elif diarrea=="NO":
								diarrea = "Diarrea: NO"
								negt+=1
								LISTA_Sintomas.append(diarrea)
								break
							else: 
								print("Porfavor RESPONDER con (SI/NO)")
								continue	
					lista_pasientes.append([LISTA_Sintomas])
					if act == 10 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Positivo (100%)"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Activo")
						num_confirmado=num_confirmado+1
						lista_pasientes.append(estado)
						confirmados.append([lista_pasientes])
					if act == 9 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Positivo (90%)"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Activo")
						num_confirmado=num_confirmado+1
						lista_pasientes.append(estado)
						confirmados.append([lista_pasientes])
					if act == 8 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Positivo (80%)"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Activo")
						num_confirmado=num_confirmado+1
						lista_pasientes.append(estado)
						confirmados.append([lista_pasientes])
					if act == 7 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Positivo (70%)"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Activo")
						num_sospechoso=num_sospechoso+1
						lista_pasientes.append(estado)
						Sospechosos.append([lista_pasientes])
					if act == 6 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Positivo (40%)"
						print("Resultado:", estado)
						print("")
						print("CONVID-19")
						num_sospechoso=num_sospechoso+1
						lista_pasientes.append(estado)
						Sospechosos.append([lista_pasientes])
					if act == 5 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Negativo"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Inactivo")
						num_sospechoso=num_sospechoso+1
						lista_pasientes.append(estado)
						Sospechosos.append([lista_pasientes])
					if act == 4 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Negativo"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Inactivo")
						num_descartado=num_descartado+1
						lista_pasientes.append(estado)
						Descartados.append([lista_pasientes])
					if act == 3 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Negativo"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Inactivo")
						num_descartado=num_descartado+1
						lista_pasientes.append(estado)
						Descartados.append([lista_pasientes])
					if act == 2 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Negativo"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Inactivo")
						num_descartado+=1
						lista_pasientes.append(estado)
						Descartados.append([lista_pasientes])
					if act == 1 :
						print("")
						print("_______________________________")
						print("             EXAMEN            ")
						print("_______________________________")
						print("")
						estado="Negativo"
						print("Resultado:", estado)
						print("")
						print("CONVID-19 Inactivo")
						num_descartado=num_descartado+1
						lista_pasientes.append(estado)
						Descartados.append([lista_pasientes])


				if option=="4":

					lista = '\n'.join(lista_pasientes)
					archivo=open("CLINICA MOVIL.txt","w")
					archivo.write(lista)
					archivo.close()

					break		
	if option=="salir":
		break
	if option=="Salir":
		break
	if option=="SALIR":
		break