# main.py
from modulos import inventario

def main():
    # 1. Inicializar el inventario
    inventario_restaurante = inventario.inicializar_inventario()
    
    # 2. Mostrar el menú al cliente
    inventario.mostrar_menu(inventario_restaurante)
    
    # 3. Aquí iría la lógica 
    
    # Ejemplo de cómo se usaría:
    pedido = "hamburguesa_clasica"
    cantidad = 2
    
    # Verificar si hay disponibilidad
    disponible, motivo = inventario.verificar_disponibilidad(
        pedido, cantidad, inventario_restaurante
    )
    
    if disponible:
        print("¡Pedido confirmado!")
        # Actualizar inventario
        inventario.actualizar_inventario(pedido, cantidad, inventario_restaurante)
        # Mostrar inventario actualizado
        inventario.mostrar_inventario(inventario_restaurante)
    else:
        print(f"Lo sentimos, no hay suficiente {motivo}")

if __name__ == "__main__":
    main()