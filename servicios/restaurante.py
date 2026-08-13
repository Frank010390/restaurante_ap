from typing import List, Union
from modelos import Producto, Bebida, Cliente

class Restaurante:
    """Servicio encargado de administrar productos y clientes del sistema."""

    def __init__(self):
        # 📋 LISTAS: almacenan colecciones dinámicas (lo que ya tenías)
        self._lista_productos: List[Producto] = []
        self._lista_clientes: List[Cliente] = []

        # 📐 TUPLA: información fija que NO cambia (opciones del menú)
        self._opciones_menu = (
            "Registrar producto",
            "Buscar producto",
            "Listar productos",
            "Registrar cliente",
            "Listar clientes",
            "Mostrar categorías",
            "Salir"
        )

        # 🔑 DICCIONARIO: búsqueda rápida de productos por código
        self._productos_por_codigo: dict[str, Producto] = {}

        # 🔄 CONJUNTOS: evitan duplicados automáticamente
        self._categorias: set[str] = set()       # categorías únicas
        self._codigos_productos: set[str] = set() # códigos de productos
        self._ids_clientes: set[str] = set()      # identificaciones de clientes

    # --- Métodos para productos ---
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto o bebida, evitando códigos duplicados."""
        # Validación con CONJUNTO (más rápida que recorrer lista)
        if producto.codigo in self._codigos_productos:
            print(f"❌ Error: Ya existe un producto con código {producto.codigo}")
            return False

        self._lista_productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto  # diccionario
        self._categorias.add(producto.categoria)                  # conjunto
        self._codigos_productos.add(producto.codigo)              # conjunto

        print(f"✅ Producto registrado correctamente")
        return True

    def buscar_producto(self, codigo: str) -> Union[Producto, None]:
        """Busca producto usando el DICCIONARIO (búsqueda instantánea)."""
        return self._productos_por_codigo.get(codigo)

    def listar_productos(self) -> None:
        """Muestra todos los productos usando polimorfismo."""
        if not self._lista_productos:
            print("⚠️ No hay productos registrados")
            return

        print("\n" + "="*40)
        print("LISTA DE PRODUCTOS Y BEBIDAS")
        print("="*40)
        for indice, item in enumerate(self._lista_productos, start=1):
            print(f"\n--- Producto {indice} ---")
            print(item.mostrar_informacion())  # Polimorfismo

    # --- Métodos para clientes ---
    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente, evitando identificaciones duplicadas."""
        # Validación con CONJUNTO
        if cliente.identificacion in self._ids_clientes:
            print(f"❌ Error: Ya existe un cliente con identificación {cliente.identificacion}")
            return False

        self._lista_clientes.append(cliente)
        self._ids_clientes.add(cliente.identificacion)  # conjunto

        print(f"✅ Cliente registrado correctamente")
        return True

    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados."""
        if not self._lista_clientes:
            print("⚠️ No hay clientes registrados")
            return

        print("\n" + "="*40)
        print("LISTA DE CLIENTES")
        print("="*40)
        for indice, item in enumerate(self._lista_clientes, start=1):
            print(f"\n--- Cliente {indice} ---")
            print(item.mostrar_informacion())

    # --- Métodos con estructuras nuevas ---
    def mostrar_categorias(self) -> set[str]:
        """Devuelve categorías únicas usando CONJUNTO."""
        return self._categorias.copy()

    def obtener_opciones_menu(self) -> tuple:
        """Devuelve opciones del menú usando TUPLA."""
        return self._opciones_menu