class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Categoría: {self.categoria}"