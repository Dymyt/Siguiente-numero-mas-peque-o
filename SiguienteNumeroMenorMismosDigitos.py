#Este programa recibe un número y devuelve el siguiente número más pequeño con los mismos digitos.
#OJO: el siguiente más pequeño, que no el más pequeño. 7908 sería igual a 7890, que no a 7089.
#Los ceros no pueden ir a la izquierda, como es lógico. Si no existe ninguna posibilidad se devuelve un -1.

#*******************************
#CÓMO HE ENFOCADO EL PROBLEMA:
# 1)Convierto el número entero en una lista de números de una cifra, así 7908 quedaría: [7,9,0,8].

#2)La idea es recorrer la lista de derecha a izquierda empezando en el penúltimo elemento.
#En [7,9,0,8] empezamos en el 0 y creamos de esta lista una sublista hacia la derecha, en este caso [8].
#Porque 8 no es menor que 0, continuamos, con el 9 tenemos la sublista [0,8], donde si hay números menores que 9.
#Por lo que es posible que exista un número menor.

#3)Ahora no hay que dar el menor númeroi, sino el SIGUIENTE MENOR a 7908, para ello primero hallaremos el número máximo
#de la sublista [0,8] que no sea mayor que 9, en este caso es 8, y la posición en la que se encuentra (indice = 1)

#4)Intercambiamos el 8 por el 9 quedando la lista así [7,8,0,9], y ahora sí, partimos nuestra lista en dos sublistas
#a las que llamaremos raíz [7,8] y variable [0,9], a la parte variable la ordenamos de mayor a menor [9,0].
#Luego juntamos ambas lista, y la volvemos a convertir en un numero entero de varias cifras: 7890.
#*******************************

#Esta función recibe una lista de números enteros y un número entero llamado numeroClave. Devuelve dos variables.
#retnumber, que es el número de mayor valor en la lista menor que numeroClave.
#retposicion, que es la posición en la que se encuentra este número.
#Si no encuentra ningún número devolverá -1, que nos servirá para saber que no se cumplen las condiciones
def MaxNumMenorA (numeroClave, listaPosibles):
    retposicion = 0
    retnumber = -1
    for loc in range(0, len(listaPosibles)):
        if listaPosibles[loc] < numeroClave and listaPosibles[loc] > retnumber:
            retnumber = listaPosibles[loc]
            retposicion = loc
    return retposicion, retnumber


#FUNCIÓN PRINCIPAL
def next_smaller(n):
    #Estas variables se crean aquí para que sean globales a toda la función.
    listanumero = []
    resCandidato = -1
    for num in str(n):
        listanumero.append(int(num))

    for pos in reversed(range(0, len(listanumero)-1)):
        #Llamo a la función anterior, dando como parámetros el numero que estamos recorriendo y la sublista después de él
        indice, numeroCandidato = MaxNumMenorA(listanumero[pos], listanumero[pos+1:])

        #Si nuestra variable numeroCandidato es -1 significa que no se cumplen las condiciones y seguiremos recorriendo el
        #bucle for con otros candidatos.
        if numeroCandidato != -1:
            #Usamos una variable intermedia llamada intercambiador para hacer el típico intercambio a=b y b=a.
            intercambiador = listanumero[pos]
            listanumero[pos] = listanumero[pos+1+indice]
            listanumero[pos + 1 + indice] = intercambiador
            #Creación de la lista raiz y variable, la variable se ordena de mayor a menos y se incluye en la lista raiz
            listaFija =  listanumero[:pos+1]
            listaVariable = listanumero[pos+1:]
            listaVariable.sort()
            listaVariable.reverse()
            listaFija.extend(listaVariable)
            #Ya que la respuesta no puede estar precedida por un 0, si es así abortamos y se devolverá -1.
            if listaFija[0] != 0:
                resCandidato = int("".join(map(str, listaFija)))
            break

    return resCandidato

contador = 0
while (contador < 10):
    print ("\nPara usar la función SIGUIENTE NÚMERO MENOR CON MISMOS DÍGITOS\n pulsa 1. \n\nPara salir del programa\n pulsa 0\n")
    respuesta = input()
    if respuesta == '1':
        print("\n************************\nEscribe cualquier número entero, se devolverá -1 si no existe\nun número menor con los mismos dígitos.")
        numeroInput = input()
        print ("\nEl siguiente número más pequeño es: ", next_smaller(numeroInput), "\n******\n")
    elif respuesta == '0':
        break