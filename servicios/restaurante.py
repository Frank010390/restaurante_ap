from typing import List, Union
from modelos import Producto, Bebida, Cliente

class Restaurante:
    """Servicio encargado de administrar productos y clientes del sistema."""

    def __init__(self):
        # Almacenamos Producto y Bebida en la MISMA lista (cumpliendo LSP)
        self._lista_productos: List[Producto] = []
        self._lista_clientes: List[Cliente] = []

    # --- Métodos para productos ---
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto o bebida, evitando códigos duplicados."""
        for item in self._lista_productos:
            if item.codigo == producto.codigo:
                print(f"❌ Error: Ya existe un producto con código {producto.codigo}")
                return False
        self._lista_productos.append(producto)
        print(f"✅ Producto registrado correctamente")
        return True

    def listar_productos(self) -> None:
        """Muestra todos los productos usando polimorfismo."""
        if not self._lista_productos:
            print("ℹ️ No hay productos registrados")
            return
        print("\n" + "="*40)
        print("LISTA DE PRODUCTOS Y BEBIDAS")
        print("="*40)
        for indice, item in enumerate(self._lista_productos, start=1):
            print(f"\n--- Producto {indice} ---")
            print(item.mostrar_informacion()) # Polimorfismo: funciona en Producto y Bebida

    # --- Métodos para clientes ---
    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente, evitando identificaciones duplicadas."""
        for item in self._lista_clientes:
            if item.identificacion == cliente.identificacion:
                print(f"❌ Error: Ya existe un cliente con identificación {cliente.identificacion}")
                return False
        self._lista_clientes.append(cliente)
        print(f"✅ Cliente registrado correctamente")
        return True

    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados."""
        if not self._lista_clientes:
            print("ℹ️ No hay clientes registrados")
            return
        print("\n" + "="*40)
        print("LISTA DE CLIENTES")
        print("="*40)
        for indice, item in enumerate(self._lista_clientes, start=1):
            print(f"\n--- Cliente {indice} ---")
            print(item.mostrar_informacion())