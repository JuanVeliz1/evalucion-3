import funciones as fn
pedidos = []

while True:
    print("""
          
          ***bienvenido a "PaquExpress***
          *******************************
          *************menu**************
          1. Registrar pedido
          2. Listar los todos los pedidos
          3. Imprimir hoja de ruta
          4. Salir del programa

""")
    
    opc = int(input("introdusca una opcion desde la opcion 1 a la 4ta "))
    if opc == 1:
        fn.registroPedido(pedidos)
    elif opc == 2:
        fn.listarPedidos(pedidos)
    elif opc== 3:
        fn.imprimirRutas(pedidos)        
    elif opc == 4:
        print("saliendo de la aplicacion, hasta luego")
        print("**************************************")
        break
    else:
        print("variable ingresada erroneamente, por favor intentar nuevamente ")    