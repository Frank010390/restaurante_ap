class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f}"