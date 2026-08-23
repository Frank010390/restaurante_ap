from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    OPCIONES_MENU = (
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
    for i, opcion in enumerate(OPCIONES_MENU, 1):
        print(f"{i}. {opcion}")
    print("-" * 40)
    return len(OPCIONES_MENU)

def registrar_producto(restaurante: Restaurante):
    print("\n--- Registrar Producto ---")
    try:
        codigo = input("Código: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: $").strip())
        producto = Producto(codigo, nombre, categoria, precio)
        if restaurante.registrar_producto(producto):
            print("✅ Producto registrado correctamente.")
        else:
            print("❌ Error: Ya existe un producto con ese código.")
    except ValueError:
        print("❌ Error: El precio debe ser un número.")

def buscar_producto(restaurante: Restaurante):
    print("\n--- Buscar Producto ---")
    codigo = input("Código del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto:
        print(f"✅ {producto}")
    else:
        print("❌ Producto no encontrado.")

def actualizar_producto(restaurante: Restaurante):
    print("\n--- Actualizar Producto ---")
    codigo = input("Código del producto a actualizar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if not producto:
        print("❌ Producto no encontrado.")
        return
    try:
        nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ").strip() or producto.nombre
        nueva_categoria = input(f"Nueva categoría ({producto.categoria}): ").strip() or producto.categoria
        nuevo_precio = input(f"Nuevo precio ({producto.precio}): $").strip()
        nuevo_precio = float(nuevo_precio) if nuevo_precio else producto.precio
        if restaurante.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
            print("✅ Producto actualizado correctamente.")
    except ValueError:
        print("❌ Error: El precio debe ser un número.")

def eliminar_producto(restaurante: Restaurante):
    print("\n--- Eliminar Producto ---")
    codigo = input("Código del producto a eliminar: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("✅ Producto eliminado correctamente.")
    else:
        print("❌ Producto no encontrado.")

def listar_productos(restaurante: Restaurante):
    print("\n--- Lista de Productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for prod in productos:
        print(prod)

def registrar_usuario(restaurante: Restaurante):
    print("\n--- Registrar Usuario ---")
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    usuario = Usuario(identificacion, nombre, correo)
    if restaurante.registrar_usuario(usuario):
        print("✅ Usuario registrado correctamente.")
    else:
        print("❌ Error: Ya existe un usuario con esa identificación.")

def listar_usuarios(restaurante: Restaurante):
    print("\n--- Lista de Usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for user in usuarios:
        print(user)

def mostrar_categorias(restaurante: Restaurante):
    print("\n--- Categorías Únicas ---")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for cat in categorias:
        print(f"• {cat}")

def main():
    restaurante = Restaurante()
    while True:
        total_opciones = mostrar_menu()
        try:
            opcion = int(input("Elige una opción: ").strip())
            acciones = {
                1: registrar_producto,
                2: buscar_producto,
                3: actualizar_producto,
                4: eliminar_producto,
                5: listar_productos,
                6: registrar_usuario,
                7: listar_usuarios,
                8: mostrar_categorias
            }
            if opcion == 9:
                print("👋 ¡Gracias por usar el sistema!")
                break
            if 1 <= opcion <= 8:
                acciones[opcion](restaurante)
            else:
                print("⚠️ Opción inválida. Intenta entre 1 y 9.")
        except ValueError:
            print("⚠️ Por favor, escribe un número válido.")
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()