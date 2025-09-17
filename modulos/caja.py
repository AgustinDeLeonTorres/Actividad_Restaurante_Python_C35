#caja
import datetime
import inventario

# Inicia inventario y ventas
datos_inventario = inventario.inicializar_inventario()
cocina = datos_inventario["productos"]
historial_ventas = []


def calcular_total(pedido, inventario):
    #Calcula el total del pedido y valida ingredientes
    total = 0
    for producto_id in pedido:
        disponible, faltante = inventario.verificar_disponibilidad(producto_id, 1, datos_inventario)
        if not disponible:
            print(f"No hay suficiente de {faltante}. Pedido cancelado.")
            return None
        total += inventario.inicializar_inventario()["productos"][producto_id]["precio"]
    return total


def registrar_venta(pedido, inventario, historial):
    #Registra la venta: descuenta inventario, guarda historial y genera ticket
    total = 0
    detalles = []

    # Verificamos y actualizamos inventario
    for producto_id in pedido:
        disponible, faltante = inventario.verificar_disponibilidad(producto_id, 1, datos_inventario)
        if not disponible:
            print(f"No hay suficiente de {faltante}. Pedido cancelado.")
            return False

    # Descontamos e imprimimos ticket
    for producto_id in pedido:
        producto = datos_inventario["productos"][producto_id]
        inventario.actualizar_inventario(producto_id, 1, datos_inventario)
        subtotal = producto["precio"]
        total += subtotal
        detalles.append(f"{producto['nombre']} - ${subtotal}")

    # Guardamos historial
    venta = {
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "productos": pedido,
        "total": total
    }
    historial.append(venta)

    # Imprimimos ticket
    print("\nTICKET DE VENTA")
    print("-" * 30)
    for d in detalles:
        print(d)
    print("-" * 30)
    print(f"TOTAL: ${total}")
    print("Gracias por su compra \n")

    return True


def mostrar_historial(historial):
    """Muestra todas las ventas registradas"""
    print("\nHistorial de ventas")
    print("=" * 40)
    total_dia = 0
    for venta in historial:
        print(f"{venta['fecha']} - Total: ${venta['total']}")
        total_dia += venta['total']
    print("=" * 40)
    print(f"Total del dia: ${total_dia}\n")
