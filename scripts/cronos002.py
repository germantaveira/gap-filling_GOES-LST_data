import sys
sys.path.append('../')
from funciones_G1 import *
from funciones_G2 import *
from funciones_G4 import *

import schedule
import time

def job():
    
    print("I'm working - Chequeo de conexión...")

    start = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    end = datetime.datetime.utcnow()

    if chequeo_internet():
        
        verbose = True
        dir_root = '../'
        
        hora_inicio = datetime.datetime.now()
        print("Hora de Inicio Ejecucion: ", str(hora_inicio))
        
        print("Generando carpetas...")
        crear_carpetas(dir_root=dir_root)
        
        print("Descargando GOES de ayer...")
        Descarga_Controlada_GOES(dir_root = dir_root, gdh_usuario_descarga_goes = GFechaHora_descarga_utc_ayer_GOES(), verbose = verbose)


        print("Descargando GOES de Hoy...")
        Descarga_Controlada_GOES(dir_root = dir_root, gdh_usuario_descarga_goes = GFechaHora_descarga_utc_hoy_GOES(), verbose = verbose)


        print("Descargando GFS de ayer y hoy...")
        descarga_gfs(dir_root=dir_root, start=start, end=end, verbose=verbose)

        print("Procesando GOES...")
        Controlar_y_Procesar_GOES_G1(dir_root = dir_root, verbose = verbose)


        print("Procesando GFS...")
        procesamiento_gfs(dir_root = dir_root, verbose = verbose)
        
        print("Procesando Función de corregistro y rellenado...")
        proceso_grupo2(dir_root = dir_root, verbose = verbose)

        print("Procesando Función de Heladas acumuladas...")
        hha(dir_root=dir_root, verbose = verbose)

        print(" ")
        hora_fin = datetime.datetime.now()
        print("Hora de Fin Ejecucion: ", str(hora_fin))

        tiempo_ejecucion = hora_fin - hora_inicio
        print("Tiempo de Ejecucion: ", str(tiempo_ejecucion))
        print("#############################################################")
    else:
        print('[!] No se puede acceder a la web para realizar las descargas')

    return

# schedule.every().hour.at(":28").do(job)
schedule.every(20).minutes.do(job)

job()

while True:
    schedule.run_pending()
    time.sleep(10)