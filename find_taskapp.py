# Este script permite buscar en el taskmanager si un programa esta abierto o no
# Reemplace sobre la variable app_find el nombre del identificador del programa a buscar

import os # Modulo para ejecutar comandos de windows sobre python
import time # Modulo para usar retardos entre lineas

while True:
	app_find = 'IBOConsole.exe'           # tarea que se requiere buscar en el administrador de tareas
	task = os.popen('TASKLIST').read()    # extracción en una variable tipo string de todas las tareas sobre el sistema
	index = task.find(app_find)           # Verficación de coincidencia de la variable sobre el string extraido

	if(index == -1):                      # Si el resultado de index es -1 es porque no hay información de la app sobre el taskmanager
		print("The app is closed")		  # Si el resultados es -1 la app no esta abierta
	else:
		print("The app is open")          # si es diferente a -1 es porque se encuentra el nombre dentro de la información extraida == app abierta

	time.sleep(1)                         # cada 1 segundo repite el bucle while