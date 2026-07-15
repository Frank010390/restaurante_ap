from servicios import Restaurante
from modelos import Producto, Bebida, Cliente

def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""
    print("\n" + "="*40)
    print("        SISTEMA DE RESTAURANTE")
    print("="*40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-"*40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-"*40)
    print("6. Salir")

def registrar_producto_sistema(restaurante: Restaurante) -> None:
    """Solicita datos y crea un objeto Producto."""
    print("\n--- Registrar nuevo producto ---")
    codigo = input("Ingrese código: ").strip()
    nombre = input("Ingrese nombre: ").strip()
    categoria = input("Ingrese categoría: ").strip()
    try:
        precio = float(input("Ingrese precio: ").strip())
    except ValueError:
        print("❌ Error: El precio debe ser un número")
        return
    producto_nuevo = Producto(codigo, nombre, categoria, precio)
    restaurante.registrar_producto(producto_nuevo)

def registrar_bebida_sistema(restaurante: Restaurante) -> None:
    """Solicita datos y crea un objeto Bebida."""
    print("\n--- Registrar nueva bebida ---")
    codigo = input("Ingrese código: ").strip()
    nombre = input("Ingrese nombre: ").strip()
    categoria = input("Ingrese categoría: ").strip()
    try:
        precio = float(input("Ingrese precio: ").strip())
    except ValueError:
        print("❌ Error: El precio debe ser un número")
        return
    tamaño = input("Ingrese tamaño (ej: 500ml): ").strip()
    tipo_envase = input("Ingrese tipo de envase: ").strip()
    bebida_nueva = Bebida(codigo, nombre, categoria, precio, tamaño, tipo_envase)
    restaurante.registrar_producto(bebida_nueva)

def registrar_cliente_sistema(restaurante: Restaurante) -> None:
    """Solicita datos y crea un objeto Cliente."""
    print("\n--- Registrar nuevo cliente ---")
    identificacion = input("Ingrese identificación: ").strip()
    nombre = input("Ingrese nombre completo: ").strip()
    correo = input("Ingrese correo electrónico: ").strip()
    cliente_nuevo = Cliente(identificacion, nombre, correo)
    restaurante.registrar_cliente(cliente_nuevo)

def main():
    """Función principal que ejecuta el sistema."""
    sistema_restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            registrar_producto_sistema(sistema_restaurante)
        elif opcion == "2":
            registrar_bebida_sistema(sistema_restaurante)
        elif opcion == "3":
            registrar_cliente_sistema(sistema_restaurante)
        elif opcion == "4":
            sistema_restaurante.listar_productos()
        elif opcion == "5":
            sistema_restaurante.listar_clientes()
        elif opcion == "6":
            print("\n👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida, intente nuevamente")

if __name__ == "__main__":
    main()