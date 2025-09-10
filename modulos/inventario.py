"""
Módulo de gestión de inventario para el restaurante
Responsable: Equipo de inventario
"""

import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTARIO_FILE = os.path.join(BASE_DIR, '..', 'data', 'inventario.json')

def cargar_inventario():
    """
    Carga el inventario desde el archivo JSON
    Retorna: diccionario con el inventario
    """
    try:
        with open(INVENTARIO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Archivo de inventario no encontrado.")
        return {}
    except json.JSONDecodeError:
        print("Error: Archivo de inventario corrupto.")
        return {}

def guardar_inventario(inventario):
    """
    Guarda el inventario en el archivo JSON
    """
    try:
        # Asegurar que el directorio existe
        os.makedirs(os.path.dirname(INVENTARIO_FILE), exist_ok=True)
        
        with open(INVENTARIO_FILE, 'w') as file:
            json.dump(inventario, file, indent=4)
        return True
    except Exception as e:
        print(f"Error guardando inventario: {e}")
        return False

def inicializar_inventario():
    """
    Inicializa el inventario con valores por defecto si no existe
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
    
    # Verificar si el archivo ya existe
    if not os.path.exists(INVENTARIO_FILE):
        guardar_inventario(inventario_default)
        print("Inventario inicializado con valores por defecto.")
    
    return cargar_inventario()

def verificar_disponibilidad(producto_id, cantidad=1):
    """
    Verifica si hay suficientes ingredientes para un producto
    """
    inventario = cargar_inventario()
    
    if producto_id not in inventario["productos"]:
        print(f"Error: Producto {producto_id} no encontrado.")
        return False
    
    producto = inventario["productos"][producto_id]
    
    for ingrediente, cantidad_necesaria in producto["ingredientes"].items():
        if ingrediente not in inventario["ingredientes"]:
            print(f"Error: Ingrediente {ingrediente} no encontrado en inventario.")
            return False
        
        cantidad_total_necesaria = cantidad_necesaria * cantidad
        if inventario["ingredientes"][ingrediente]["cantidad"] < cantidad_total_necesaria:
            print(f"Insuficiente {ingrediente} para preparar {cantidad} {producto_id}")
            return False
    
    return True

def actualizar_inventario(producto_id, cantidad=1):
    """
    Actualiza el inventario después de preparar un producto
    """
    if not verificar_disponibilidad(producto_id, cantidad):
        return False
    
    inventario = cargar_inventario()
    producto = inventario["productos"][producto_id]
    
    for ingrediente, cantidad_necesaria in producto["ingredientes"].items():
        inventario["ingredientes"][ingrediente]["cantidad"] -= cantidad_necesaria * cantidad
    
    return guardar_inventario(inventario)

def mostrar_inventario():
    """
    Muestra el estado actual del inventario
    """
    inventario = cargar_inventario()
    
    print("\n--- INVENTARIO ACTUAL ---")
    print("INGREDIENTES:")
    for ingrediente, info in inventario["ingredientes"].items():
        print(f"  {ingrediente}: {info['cantidad']} {info['unidad']}")
    
    print("\nPRODUCTOS DISPONIBLES:")
    for producto_id, info in inventario["productos"].items():
        print(f"  {producto_id}: {info['nombre']} - ${info['precio']}")

# Inicializar inventario cuando se importe el módulo
inventario = inicializar_inventario()