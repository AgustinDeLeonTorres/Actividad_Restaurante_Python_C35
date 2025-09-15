import inventario
                                                                        
#Aqui llamamos a la clase inventario 
#Cargamos lo productos del inventario

cocina = list(inventario.cargar_inventario()["productos"].keys())


def mostrar_menu(): #Mostramos los productor disponibles en el menu
    print("Menu del Restaurante:")
    for producto in cocina: 
        print("-", producto) #"-" para que se vea mejor el menu 

def tomar_pedido(): #Tomamos el pedido del cliente 
    pedido = [] #Lista vacia para tomar el pedido
    while True:
        item = input("Ingrese el nombre del producto que desea ( 'salir' para terminar): ") #item es el producto que el cliente desea  #input para que el cliente ingrese el producto
        if item.Lower() == "Salir": #Si el cliente ingresa salir, se termina el pedido
            break #Salimos del bucle
        elif item in cocina: #Si el producto esta en el menu, se agrega al pedido 
            pedido.appen(item) #Se agrega el producto al pedido
            print(f"{item} agregado al pedido. ") #Se confirma que el producto fue agregado al pedido
        else : #Si el producto no esta en el menu, se le informa al cliente
            print(f"{item} no esta en el menu. Por favor, elija otro producto.") 
            