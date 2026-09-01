from servicios import Restaurante

def mostrar_menu(opciones):
    """Muestra el menú principal del sistema."""
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN — RESTAURANTE")
    print("="*50)
    for i, opcion in enumerate(opciones, 1):
        print(f" {i}. {opcion}")
    print("="*50)

def main():
    # 📌 TUPLA: opciones fijas del menú (NO cambian)
    opciones_menu = (
        "Registrar producto",
        "Buscar producto",
        "Actualizar producto",
        "Eliminar producto",
        "Listar productos",
        "Registrar usuario",
        "Listar usuarios",
        "Mostrar categorías",
        "Salir"
    )

    sistema = Restaurante()

    while True:
        mostrar_menu(opciones_menu)
        try:
            eleccion = int(input("\n👉 Seleccione una opción: "))
            indice = eleccion - 1

            if indice == len(opciones_menu) - 1:
                print("\n👋 ¡Gracias por usar el sistema! Hasta luego.")
                break

            elif indice == 0:  # Registrar producto
                print("\n── REGISTRAR PRODUCTO ──")
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                precio = float(input("Precio: $"))
                categoria = input("Categoría: ").strip()
                sistema.registrar_producto(codigo, nombre, precio, categoria)

            elif indice == 1:  # Buscar producto
                print("\n── BUSCAR PRODUCTO ──")
                codigo = input("Ingrese el código: ").strip()
                producto = sistema.buscar_producto(codigo)
                if producto:
                    print(f"\n✅ Encontrado:\n{producto}")
                else:
                    print(f"❌ Producto con código {codigo} no existe.")

            elif indice == 2:  # Actualizar producto
                print("\n── ACTUALIZAR PRODUCTO ──")
                codigo = input("Código del producto a actualizar: ").strip()
                nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip() or None
                precio_input = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
                precio = float(precio_input) if precio_input else None
                categoria = input("Nueva categoría (dejar vacío para no cambiar): ").strip() or None
                sistema.actualizar_producto(codigo, nombre, precio, categoria)

            elif indice == 3:  # Eliminar producto
                print("\n── ELIMINAR PRODUCTO ──")
                codigo = input("Código del producto a eliminar: ").strip()
                sistema.eliminar_producto(codigo)

            elif indice == 4:  # Listar productos
                print("\n── LISTA DE PRODUCTOS ──")
                productos = sistema.listar_productos()
                if not productos:
                    print("📭 No hay productos registrados.")
                else:
                    for p in productos:
                        print(p)

            elif indice == 5:  # Registrar usuario
                print("\n── REGISTRAR USUARIO ──")
                id_usuario = input("ID / Cédula: ").strip()
                nombre = input("Nombre completo: ").strip()
                telefono = input("Teléfono: ").strip()
                sistema.registrar_usuario(id_usuario, nombre, telefono)

            elif indice == 6:  # Listar usuarios
                print("\n── LISTA DE USUARIOS ──")
                usuarios = sistema.listar_usuarios()
                if not usuarios:
                    print("📭 No hay usuarios registrados.")
                else:
                    for u in usuarios:
                        print(u)

            elif indice == 7:  # Mostrar categorías
                print("\n── CATEGORÍAS ──")
                categorias = sistema.obtener_categorias()
                if not categorias:
                    print("📭 No hay categorías registradas.")
                else:
                    for cat in categorias:
                        print(f"• {cat}")

            else:
                print("⚠️ Opción no válida. Intente de nuevo.")

        except ValueError:
            print("❌ Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()