def inicializar_inventario():
    """
    Inicializa el inventario con valores por defecto
    """
    inventario_default = {
        "ingredientes": {
            "pan_hamburguesa": {"cantidad": 50, "unidad": "piezas"},
            "carne_res": {"cantidad": 30, "unidad": "piezas"},
            "pollo": {"cantidad": 25, "unidad": "piezas"},
            "queso": {"cantidad": 40, "unidad": "rebanadas"},
            "lechuga": {"cantidad": 20, "unidad": "piezas"},
            "tomate": {"cantidad": 25, "unidad": "piezas"},
            "cebolla": {"cantidad": 15, "unidad": "piezas"},
            "tocino": {"cantidad": 35, "unidad": "rebanadas"},
            "papas": {"cantidad": 20, "unidad": "kg"},
            "refresco": {"cantidad": 60, "unidad": "latas"},
            "agua": {"cantidad": 45, "unidad": "botellas"}
        },
        "productos": {
            "hamburguesa_clasica": {
                "nombre": "Hamburguesa Clásica",
                "precio": 85,
                "ingredientes": {"pan_hamburguesa": 1, "carne_res": 1, "queso": 1, "lechuga": 1, "tomate": 2}
            },
            "hamburguesa_pollo": {
                "nombre": "Hamburguesa de Pollo",
                "precio": 75,
                "ingredientes": {"pan_hamburguesa": 1, "pollo": 1, "lechuga": 1, "tomate": 2}
            },
            "hamburguesa_tocino": {
                "nombre": "Hamburguesa con Tocino",
                "precio": 95,
                "ingredientes": {"pan_hamburguesa": 1, "carne_res": 1, "queso": 1, "tocino": 2, "lechuga": 1}
            },
            "papas_fritas": {
                "nombre": "Papas Fritas",
                "precio": 35,
                "ingredientes": {"papas": 0.2}
            },
            "refresco": {
                "nombre": "Refresco",
                "precio": 25,
                "ingredientes": {"refresco": 1}
            },
            "agua": {
                "nombre": "Agua Natural",
                "precio": 20,
                "ingredientes": {"agua": 1}
            }
        }
    }
    return inventario_default

def mostrar_inventario(inventario):
    """
    Muestra el estado actual del inventario de forma organizada
    """
    print("\n" + "="*50)
    print("          INVENTARIO ACTUAL")
    print("="*50)
    
    print("\n--- INGREDIENTES ---")
    for ingrediente_id, datos in inventario["ingredientes"].items():
        print(f"{ingrediente_id}: {datos['cantidad']} {datos['unidad']}")
    
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for producto_id, datos in inventario["productos"].items():
        print(f"{producto_id}: {datos['nombre']} - ${datos['precio']}")
    
    print("="*50)

def verificar_disponibilidad(producto_id, cantidad, inventario):
    """
    Verifica si hay suficientes ingredientes para un producto
    Returns: (True, None) si hay stock, (False, ingrediente_faltante) si no hay
    """
    if producto_id not in inventario["productos"]:
        return False, "Producto no existe en el menú"
    
    producto = inventario["productos"][producto_id]
    
    for ingrediente, cantidad_necesaria in producto["ingredientes"].items():
        # Verificar si el ingrediente existe en inventario
        if ingrediente not in inventario["ingredientes"]:
            return False, f"Ingrediente '{ingrediente}' no existe en inventario"
        
        # Verificar si hay suficiente cantidad
        inventario_actual = inventario["ingredientes"][ingrediente]["cantidad"]
        if inventario_actual < (cantidad_necesaria * cantidad):
            return False, ingrediente
    
    return True, None

def actualizar_inventario(producto_id, cantidad, inventario):
    """
    Descuesta los ingredientes utilizados para un pedido
    """
    producto = inventario["productos"][producto_id]
    
    for ingrediente, cantidad_necesaria in producto["ingredientes"].items():
        inventario["ingredientes"][ingrediente]["cantidad"] -= cantidad_necesaria * cantidad

def obtener_menu(inventario):
    """
    Devuelve el menú en formato amigable para mostrar al cliente
    """
    menu = []
    for producto_id, datos in inventario["productos"].items():
        menu.append({
            "id": producto_id,
            "nombre": datos["nombre"],
            "precio": datos["precio"]
        })
    return menu

def mostrar_menu(inventario):
    """
    Muestra el menú al cliente de forma atractiva
    """
    print("\n" + "="*50)
    print("           MENÚ DEL RESTAURANTE")
    print("="*50)
    
    for producto_id, datos in inventario["productos"].items():
        print(f"{producto_id}: {datos['nombre']} - ${datos['precio']}")
    
    print("="*50)

# Función para probar el módulo
if __name__ == "__main__":
    
    inventario = inicializar_inventario()
    mostrar_inventario(inventario)
    mostrar_menu(inventario)
    
    
    producto_test = "hamburguesa_clasica"
    cantidad_test = 3
    
    disponible, mensaje = verificar_disponibilidad(producto_test, cantidad_test, inventario)
    print(f"\n¿Hay {cantidad_test} {producto_test}? {'Sí' if disponible else 'No'}")
    if not disponible:
        print(f"Razón: {mensaje}")
    
   
    if disponible:
        print(f"\nPreparando {cantidad_test} {producto_test}...")
        actualizar_inventario(producto_test, cantidad_test, inventario)
        print("Inventario actualizado:")
        mostrar_inventario(inventario)