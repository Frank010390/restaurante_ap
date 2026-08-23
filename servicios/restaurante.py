from typing import List, Set, Dict
from modelos import Producto, Usuario

class Restaurante:
    """Servicio encargado de administrar productos y usuarios del sistema."""
    
    def __init__(self):
        # LISTAS: colecciones dinámicas
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        
        # DICCIONARIO: búsqueda rápida por código
        self._productos_por_codigo: Dict[str, Producto] = {}
        
        # TUPLA: información fija que NO cambia (opciones del menú)
        self._opciones_menu = (
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

    def obtener_opciones_menu(self) -> tuple:
        """Devuelve opciones del menú usando TUPLA."""
        return self._opciones_menu

    # ==== MÉTODOS DE PRODUCTOS ====
    def registrar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self._productos_por_codigo:
            return False
        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self._productos_por_codigo.get(codigo)

    def actualizar_producto(self, codigo: str, nuevo_nombre: str, nueva_categoria: str, nuevo_precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False
        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False
        self._productos.remove(producto)
        del self._productos_por_codigo[codigo]
        return True

    def listar_productos(self) -> List[Producto]:
        return self._productos.copy()

    # ==== MÉTODOS DE USUARIOS ====
    def registrar_usuario(self, usuario: Usuario) -> bool:
        for u in self._usuarios:
            if u.identificacion == usuario.identificacion:
                return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return self._usuarios.copy()

    # ==== MÉTODO DE CATEGORÍAS (usa SET) ====
    def obtener_categorias_unicas(self) -> Set[str]:
        """Devuelve un conjunto con las categorías sin duplicados."""
        categorias = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias