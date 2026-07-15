from .producto import Producto

class Bebida(Producto):
    """Clase hija que representa una bebida, hereda de Producto."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamaño: str, tipo_envase: str):
        # Llamamos al constructor de la clase padre
        super().__init__(codigo, nombre, categoria, precio)
        # Atributos propios de Bebida
        self.tamaño = tamaño
        self.tipo_envase = tipo_envase

    def mostrar_informacion(self) -> str:
        """Sobreescribe el método para agregar datos específicos de bebidas."""
        info_base = super().mostrar_informacion()
        return (
            f"{info_base}\n"
            f"Tamaño: {self.tamaño}\n"
            f"Envase: {self.tipo_envase}"
        )