# 🍽️ Restaurante App — Semana 9
*Estudiante:* Frank Marlon Carriel Santos
*Asignatura:* Programación Orientada a Objetos

## 📋 Descripción del Proyecto
Sistema de gestión para restaurante que permite administrar *productos* y *usuarios*, aplicando estructuras de datos en Python y arquitectura modular.

## 📂 Estructura del Proyecto
Restaurante__app/
├── main.py                    
├── modelos/
│   ├── init.py
│   ├── producto.py            
│   └── usuario.py             
└── servicios/
├── init.py
└── restaurante.py
         
## 🗂️ Estructuras de Datos Utilizadas
| Estructura | Uso en el sistema |
|---|---|
| *Lista* | Almacenar productos y usuarios registrados |
| *Diccionario* | Búsqueda rápida de productos por código |
| *Conjunto* | Evitar duplicados: códigos, IDs, categorías |
| *Tupla* | Opciones fijas del menú (no modificables) |

## ✅ Funcionalidades
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Listar usuarios
8. Mostrar categorías
9. Salir

## 🚀 Ejecución
```bash
python main.py