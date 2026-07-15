class Cliente:
    """Clase que representa un cliente registrado del restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self) -> str:
        """Devuelve los datos formateados del cliente."""
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre completo: {self.nombre}\n"
            f"Correo electrónico: {self.correo}"
        )