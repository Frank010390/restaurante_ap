class Usuario:
    def __init__(self, id_usuario: str, nombre: str, telefono: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Teléfono: {self.telefono}"