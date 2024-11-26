def es_valido(direccion):
    respuesta=True
    if("@" not in direccion):
        respuesta=False
    if("." not in direccion):
        respuesta=False
    if(direccion.rindex("@")>direccion.rindex(".")):
        respuesta=False

    return(respuesta)


def correos():
    cadena_entrada=raw_input("Introduzca una lista de correors separados por comas: ")
    lista_correos=cadena_entrada.split(",")
    for direccion in lista_correos:
        if(es_valido(direccion)==True):
            respuesta="Correcto"
        else:
            respuesta="Incorrecto"
        print(direccion+" "+str(respuesta))

correos()
