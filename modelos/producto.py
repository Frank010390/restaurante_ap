class Producto:
    """Clase base que representa un producto general del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self) -> str:
        """Devuelve los datos formateados del producto."""
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}"
        )