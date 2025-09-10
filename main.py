from modulos import inventario

def main():
    print("Bienvenido al Sistema del Restaurante")
    inventario.mostrar_inventario()
    
    if inventario.verificar_disponibilidad("hamburguesa_clasica", 2):
        print("Hay ingredientes para 2 hamburguesas clásicas")
    else:
        print("No hay ingredientes suficientes")

if __name__ == "__main__":
    main()