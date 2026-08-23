# Restaurante App — Semana 9
*Asignatura:* Programación Orientada a Objetos  
*Estudiante:* Frank Marlon Carriel Santos

---

## 📋 Descripción del Proyecto
Sistema de administración de *productos y usuarios, desarrollado en Python aplicando los principios de Programación Orientada a Objetos. El objetivo es integrar estructuras de datos adecuadas para gestionar información del sistema, manteniendo una arquitectura modular separada en **modelos, servicios y lógica de ejecución*.

---

## 🧱 Estructuras de Datos Utilizadas
Cada estructura se elige para resolver una necesidad específica del sistema:

| Estructura | Uso en el sistema | Justificación |
|---|---|---|
| *📋 Lista* | Almacenar productos y usuarios | Colección dinámica, permite agregar, eliminar y recorrer elementos |
| *🔗 Tupla* | Opciones del menú principal | Información fija que no cambia durante la ejecución |
| *📖 Diccionario* | Búsqueda de productos por código | Acceso rápido y directo sin recorrer toda la lista |
| *🔄 Conjunto (Set)* | Obtener categorías únicas | Elimina automáticamente duplicados |

---

## 📂 Estructura del Proyecto
restaurante_ap/
├── modelos/
│   ├── init.py      # Exporta las clases Producto y Usuario
│   ├── producto.py      # Clase Producto: código, nombre, categoría, precio
│   └── usuario.py       # Clase Usuario: identificación, nombre, correo
├── servicios/
│   ├── init.py
│   └── restaurante.py   # Lógica del sistema: registrar, buscar, actualizar, eliminar, listar
├── main.py              # Menú principal y ejecución del programa
└── README.md            # Documentación del proyecto
## ✅ Funcionalidades del Sistema
1. *Registrar producto* → Código, nombre, categoría y precio
2. *Buscar producto* → Por código (búsqueda rápida con diccionario)
3. *Actualizar producto* → Modificar datos de un producto existente
4. *Eliminar producto* → Remover un producto del sistema
5. *Listar productos* → Mostrar todos los productos registrados
6. *Registrar usuario* → Identificación, nombre y correo
7. *Listar usuarios* → Mostrar todos los usuarios registrados
8. *Mostrar categorías* → Categorías únicas sin duplicados (usa conjunto)
9. *Salir* → Cerrar la aplicación

---

## ▶️ Cómo Ejecutar el Programa
```bash
python main.py
