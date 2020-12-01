import os
import ArchivosExp
import AG

def main():
    metodo = ''
    ruta = ""
    archivos = []
    pesos = []
    tamanioDeseado = 0
    
    #Obtenemos los parametros del problema
    print("Optimizador de Limpiador de Archivos")
    
    ruta = input("Ingrese el directorio a analizar (C:\\Users\\user\\Desktop\\folder):")
    if os.path.exists(ruta)==False:
        print("El directorio especificado no existe")
    else:
        print("Obteniendo información del directorio ",ruta," ...")
        #Obtenemos los archivos y los asignamos al problema
        tamanioActual = 0
        carpeta = os.listdir(ruta)
        for archivo in carpeta:
            rutaArchivo = ruta+'\\'+archivo
            t = int(os.path.getsize(rutaArchivo))
            archivos.append(archivo)
            pesos.append(t)
            tamanioActual += t
        tamanioActual=tamanioActual/1024/1024
        print("El directorio contiene ",len(archivos)," archivos")
        print("El directorio actual tiene archivos equivalentes a ",tamanioActual,"(MB)")
        tamanioDeseado = float(input("Ingrese el tamanio final deseado (MB):"))
        tamanioDeseado=tamanioDeseado*1024*1024
        directorio = ArchivosExp.archivosExp(archivos, pesos, tamanioDeseado)
        
        metodo=input("Ingrese el metodo a utilizar:")
        
        #Ejecuta Algoritmo Evolutivo
        if(metodo=='Genetico'):
            genetico(len(archivos),directorio)
        elif(metodo =='Diferencial'):
            diferencial()
        elif(metodo=='Enjambre'):
            enjambreParticulas()
        else:
            print('Metodo no soportado')
            
        #Mostramos el peso final alcanzado y que archivos eliminar
    
    
def genetico(numAlelos, directorio):
    # :::::::::::::::::::::: Algoritmo Genetico ::::::::::::::::::::::::::
    alelos = numAlelos
    individuos = 32
    tamano_gen = 1 #cada bit representa a un artículo de la mochila
    generaciones = 2000
    factor_mutacion = 0.01
    ag = AG.AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, directorio)
    ag.run()

def enjambreParticulas():
    print('In progress...')
    
def diferencial():
    print('In progress...')

if __name__ == '__main__':
    main()
