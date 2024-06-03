#Axel Castañeda Sánchez 010145666
import threading
import time

# Definición del semáforo
imprimir = threading.Semaphore(2)  

"""
Se crea un semáforo que permite que 2 hilos accedan simultáneamente. 
Esto se hace para controlar el acceso concurrente a las impresoras, 
permitiendo que solo dos tareas se impriman a la vez.
"""

# Clase Impresora
class Impresora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lock = threading.Lock()
        """
        Se define la clase Impresora.
        La clase se inicializa con un nombre asignado a la impresora.
        Además, se crea un bloqueo (lock) para manejar el acceso exclusivo a la impresora.
        """

    def imprimir(self, tarea):
        print(f"La impresión {tarea} ha entrado a la cola de la impresora {self.nombre}\n")
        with imprimir:
            print(f"La impresión {tarea} se está imprimiendo en {self.nombre}\n")
            time.sleep(30)  # Simulando el tiempo de impresión
            print(f"La impresión {tarea} ha liberado la cola de impresión de {self.nombre}\n")
        """
        Este método maneja las tareas de impresión. 
        - Indica que la tarea ha entrado en la cola de la impresora.
        - Usa el semáforo para controlar el acceso a la impresora, 
          permitiendo que solo dos tareas se impriman a la vez.
        - Simula el proceso de impresión con un tiempo de espera de 2 segundos.
        - Indica que la tarea ha terminado y libera la impresora.
        """

# Clase ControladorImpresoras
class ControladorImpresoras:
    def __init__(self, impresoras):
        self.impresoras = impresoras
        """
        Se define la clase ControladorImpresoras.
        Esta clase se inicializa con una lista de impresoras.
        """

    def obtener_impresora(self, tarea):
        for impresora in self.impresoras:
            if impresora.lock.acquire(blocking=False):
                try:
                    impresora.imprimir(tarea)
                finally:
                    impresora.lock.release()
                break
        """
        Este método busca una impresora disponible para realizar la tarea de impresión.
        - Itera sobre la lista de impresoras.
        - Intenta adquirir el bloqueo de una impresora sin bloquearse si no está disponible.
        - Si adquiere el bloqueo, imprime la tarea y luego libera el bloqueo.
        - Una vez encuentra una impresora disponible, rompe el bucle.
        """

# Función que simula un proceso de impresión
def proceso_impresion(controlador, tarea):
    controlador.obtener_impresora(tarea)
    """
    Esta función simula un proceso de impresión.
    - Llama al método obtener_impresora del controlador con la tarea específica.
    """

# Configuración de la simulación
impresoras = [
    Impresora("HP"),
    Impresora("LENOVO"),
    Impresora("EPSON"),
    Impresora("CANON")
]
"""
Se crean instancias de las impresoras con los nombres:
1. HP
2. LENOVO
3. EPSON
4. CANON
"""

controlador = ControladorImpresoras(impresoras)
"""
Se crea una instancia de ControladorImpresoras, inicializada con la lista de impresoras.
"""

tareas = [f"Tarea {i+1}" for i in range(10)]
"""
Se crea una lista de 10 tareas de impresión, numeradas del 1 al 10.
"""

# Creación y ejecución de los hilos
hilos = []
for tarea in tareas:
    hilo = threading.Thread(target=proceso_impresion, args=(controlador, tarea))
    hilos.append(hilo)
    hilo.start()
    """
    Se crea y ejecuta un hilo para cada tarea de impresión.
    - Se itera sobre la lista de tareas.
    - Para cada tarea, se crea un hilo que ejecuta la función proceso_impresion con el controlador y la tarea como argumentos.
    - Se añade el hilo a la lista de hilos.
    - Se inicia el hilo.
    """

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()
    """
    Se espera a que todos los hilos terminen su ejecución.
    - Se itera sobre la lista de hilos.
    - Se llama al método join() en cada hilo, que bloquea hasta que el hilo termine su ejecución.
    """