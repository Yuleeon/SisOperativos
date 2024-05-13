#elaborar un programa en python dentro de ubuntu que ejecute lo siguiente, 
#1 crear un abrchivo txt, llamado "mis notas.txt"
#2 crear una carpeta que se llame calificaciones,
#3 crear una carpeta, dentro de calificaciones, que se llame primer parcial,
#4 mover el archivo mis notas.txt a la carpeta de calificaciones,
#5 dentro de la carpeta primer parcial deberas mover el programa, calculadora.py 
#Elabora un menu con las opciones anteriores para que el usuario elija, 

#! /usr/bin/env python
print("MENU: \n 1 Crear una archivo llamado misnotas.txt \n 2 crear una carpeta llamada calificaciones \n")
print("3 mover el archivo misnotas.txt a la carpeta calificaciones \n 4 mover el programa calculadora.py a calificaciones")
opcion=input("Ingrese la opcion que desea elegir")
if opcion == "1": 
    #crear mis notas.txt
    def ejecutar(comando):
        subprocess.run ("touch misnotas.txt", shell=True)

elif opcion == "2":
    def ejecutar(comando):
        subprocess.run ("mkdir calificaciones",shell=True)

elif opcion == "3":
    def ejecutar(commando):
        subprocess.run("mv misnotas.txt > /home/kali/calificaciones",shell=True)
        
elif opcion == "4":
    def ejecutar(comando):
        subprocess.run("calculadora.py /home/kali/calificaciones+",shell=True)
else:
    print("Opcion invalida")
