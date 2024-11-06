
import random

#Creamos un diccionario con los datos de las canciones y cantantes
musica=[]

#Agregamos los datos del archivo playlist.txt al diccionario
def agregarMusicaArchivo():
    fichero=open("playlistPepe.txt","r")
    for linea in fichero:
        datos={}
        cancion,cantante,genero=linea.split("-")
        datos["Nombre: "]=cancion
        datos["Cantante: "]=cantante
        datos["Genero: "]=genero
        musica.append(datos)
        #musica[cancion.strip()]=cantante.strip()
    
    print(musica)
    fichero.close()

#Agregamos los datos de las canciones y cantantes al diccionario
def agregarCanciones():
    elementos=int(input("Cuantas canciones desea agregar: "))
    for i in range(elementos):
        cancion=input("Ingrese el nombre de la cancion: ")
        cantante=input("Ingrese el nombre del cantante: ")
        musica[cancion]=cantante
    
    print("================================")
    print("Cantante y cancion agregados")


#Eliminamos una cancion del diccionario
def eliminarCanciones():
    cancion=input("Ingresa nombre de la cancion que deseas eliminar:")
    if cancion in musica:
        del musica[cancion]
        print("================================")
        print("La cancion "+cancion+" ha sido eliminada")
    else:
        print("================================")
        print("La cancion no se encuentra en la lista")


#Buscar canciones por cantante
def buscarCancionesporCantante():
    listaCanciones=[]
    cantante=input("Ingrese el nombre del cantante: ")
    for cancion in musica:
        if musica[cancion]==cantante:
            listaCanciones.append(cancion)

    print("================================")       
    print("El cantante "+cantante+" ha producido estas canciones:")
    print(listaCanciones)
    
        

#Guardar lista de reproduccion en un archivo
def guardarListaReproduccionArchivo(listaCancionesAleatorias):
    # Abre (o crea si no existe) el archivo en modo de escritura
    fichero = open("playlistAleatoria.txt", "w")
    
    # Escribe cada canción en una nueva línea del archivo
    for cancion in listaCancionesAleatorias:
        fichero.write(cancion + "\n")
    
    # Cierra el archivo después de escribir en él
    fichero.close()
    
    print("================================")
    print("Lista de reproducción guardada en archivo")



agregarMusicaArchivo()

#print("Canciones y cantantes")
#print(musica)

#agregarCanciones()
#print(musica)
#eliminarCanciones()
#print(musica)
#contarCanciones()
#buscarCancionesporCantante()
#crearListaReproduccionAleatoria()
#guardarListaReproduccionArchivo(listaCancionesAleatorias)
