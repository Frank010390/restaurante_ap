from typing import List, Set, Dict
from modelos import Producto, Usuario

class Restaurante:
    """Servicio encargado de administrar productos y usuarios del sistema."""

    def __init__(self):
        # 📋 LISTAS: colecciones dinámicas
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

        # 📖 DICCIONARIO: búsqueda rápida por código
        self._productos_por_codigo: Dict[str, Producto] = {}

        # 🔄 CONJUNTOS: evitan duplicados automáticamente
        self._categorias: Set[str] = set()
        self._codigos_productos: Set[str] = set()
        self._ids_usuarios: Set[str] = set()

    # ──────────── MÉTODOS DE PRODUCTOS ────────────
    def registrar_producto(self, codigo: str, nombre: str, precio: float, categoria: str) -> bool:
        if codigo in self._codigos_productos:
            print(f"❌ El código {codigo} ya existe.")
            return False
        
        producto = Producto(codigo, nombre, precio, categoria)
        self._productos.append(producto)
        self._productos_por_codigo[codigo] = producto
        self._codigos_productos.add(codigo)
        self._categorias.add(categoria)
        print(f"✅ Producto '{nombre}' registrado.")
        return True

    def buscar_producto(self, codigo: str):
        return self._productos_por_codigo.get(codigo)

    def actualizar_producto(self, codigo: str, nombre: str = None, precio: float = None, categoria: str = None) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            print(f"❌ Producto con código {codigo} no encontrado.")
            return False
        
        if nombre: producto.nombre = nombre
        if precio: producto.precio = precio
        if categoria: 
            producto.categoria = categoria
            self._categorias.add(categoria)
        print(f"✅ Producto '{codigo}' actualizado.")
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            print(f"❌ Producto con código {codigo} no encontrado.")
            return False
        
        self._productos.remove(producto)
        del self._productos_por_codigo[codigo]
        self._codigos_productos.remove(codigo)
        print(f"✅ Producto '{codigo}' eliminado.")
        return True

    def listar_productos(self) -> List[Producto]:
        return self._productos

    # ──────────── MÉTODOS DE USUARIOS ────────────
    def registrar_usuario(self, id_usuario: str, nombre: str, telefono: str) -> bool:
        if id_usuario in self._ids_usuarios:
            print(f"❌ El ID {id_usuario} ya está registrado.")
            return False
        
        usuario = Usuario(id_usuario, nombre, telefono)
        self._usuarios.append(usuario)
        self._ids_usuarios.add(id_usuario)
        print(f"✅ Usuario '{nombre}' registrado.")
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return self._usuarios

    # ──────────── MÉTODOS AUXILIARES ────────────
    def obtener_categorias(self) -> Set[str]:
        return self._categorias