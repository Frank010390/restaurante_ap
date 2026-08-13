from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def main():
    app = Restaurante()

    while True:
        # Usa la TUPLA para mostrar opciones
        opciones = app.obtener_opciones_menu()
        print("\n" + "="*50)
        print("          SISTEMA DE RESTAURANTE")
        print("="*50)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        print("-"*50)

        try:
            seleccion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Ingrese un número válido.")
            continue

        if seleccion == 1:
            # Registrar producto o bebida
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                precio = float(input("Precio: $"))
            except ValueError:
                print("⚠️ Precio inválido.")
                continue

            es_bebida = input("¿Es bebida? (s/n): ").strip().lower()
            if es_bebida == "s":
                tamano = input("Tamaño (ej: 500ml): ").strip()
                tipo_envase = input("Tipo de envase: ").strip()
                producto = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
            else:
                producto = Producto(codigo, nombre, categoria, precio)

            app.registrar_producto(producto)

        elif seleccion == 2:
            # Buscar producto
            codigo = input("Código del producto a buscar: ").strip()
            prod = app.buscar_producto(codigo)
            if prod:
                print("\n" + prod.mostrar_informacion())
            else:
                print("❌ Producto no encontrado.")

        elif seleccion == 3:
            # Listar productos
            app.listar_productos()

        elif seleccion == 4:
            # Registrar cliente
            ide = input("Identificación: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()
            cliente = Cliente(ide, nombre, correo)
            app.registrar_cliente(cliente)

        elif seleccion == 5:
            # Listar clientes
            app.listar_clientes()

        elif seleccion == 6:
            # Mostrar categorías (CONJUNTO)
            cats = app.mostrar_categorias()
            if cats:
                print("\n📂 Categorías únicas:")
                print(", ".join(cats))
            else:
                print("No hay categorías registradas.")

        elif seleccion == 7:
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    main()