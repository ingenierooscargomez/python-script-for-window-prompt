import  os
import time

app_find = 'IBOConsole.exe'           # tarea que se requiere buscar en el administrador de tareas
task = os.popen('TASKLIST').read()    # extracción en una variable tipo string de todas las tareas sobre el sistema
index = task.find(app_find)           # Verficación de coincidencia de la variable sobre el string extraido

if(index == -1):                      # Si el resultado de index es -1 es porque no hay información de la app sobre el taskmanager
	print("There isn't app with name " + app_find)		  # Si el resultados es -1 la app no esta abierta
	time.sleep(2)
else:
	os.system("taskkill /f /im IBOConsole.exe")
	print("The app was close")          # si es diferente a -1 es porque se encuentra el nombre dentro de la información extraida == app abierta
	time.sleep(2)