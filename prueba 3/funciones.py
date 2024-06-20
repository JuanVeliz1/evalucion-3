 

PEDIDO = ["pequeño", "mediano", "grande"]
SECTOR = ["centro", "norte", "sur"]
precio = ['pequeño: 5000',]


def registroPedido(pedidos):
    nombre = input("ingrese su nombre y apellido completo \n")
    direccion = input("ingrese su direccion [nombre de calle, numero] \n")
    sector = input("ingrese el sector donde reside \n").lower()
    while sector not in SECTOR:
        print ("no tenemos covertura en el sector que ingreso")
        sector = input("ingrese el sector donde reside \n").lower()
    pedido = input("ingrese el tamaño de su pedido, porfavor \n").lower()
    while pedido not in PEDIDO:
        print("la variable ingresada no es valida, porfavor prueve con [pequeño,mediano,grande]")
        pedido = input("ingrese el tamaño de su pedido, porfavor \n").lower()    
    pedidos.append({

        "Nombre y apellido" : nombre,
        "Direccion de Pedido" : direccion+" , " +sector,
        "Tamaño del pedido  " : pedido
    })
    print("felicitaciones sus datos han sido ingresados de manera exitosa ")
    

def listarPedidos(pedidos):
    for pedido in pedidos:
        print(pedidos)


def imprimirRutas(pedidos):
    sectores = input("a que comuna pertece el pedido? ").lower()
    while sectores not in SECTOR:
        print("datos ingresados de forma erronea, vuelva a intentar. ")
        sectores = input("a que comuna pertece el pedido? ").lower
   
    with open(sectores + '.txt', 'w') as f:
        for pedido in pedidos:
            f.write(str(pedidos) + '\n')
            with  open("_parcel.txt", "w") as f:
                print("se esta imprimiendo su archivo")
                print("******************************")
                print("******************************")



