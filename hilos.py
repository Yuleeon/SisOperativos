#Moya Albarran Laura Yuliana   20/05/24
import threading
import time
#crear un semaforo con contador inicial de 2
semaphore = threading.Semaphore(2)
#hasta dos hilos pueden adquirir el semaforo simultaneamente, si un 3ro intenta debera esperar a que uno de los hilos 
#se libere
def tarea(id):
    print(f"tarea {id} intentando acceder al recurso")
    with semaphore:
        print(f"Tarea {id} ah adquirido el semaforo")
        time.sleep(2)
        print(f"Tarea{id} ah liberado el semaforo")
#crear multiples hilos que ejecuten la funcion "tarea"

threads = []
for i in range(5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()
#esperar a que todos lo hilos terminen
for thread in threads:
    thread.join()
    
