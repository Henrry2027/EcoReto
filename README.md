# Misión Eco-Reto - Proyecto Integrador CECyTeM

Proyecto de desarrollo web para la gestión de acciones ecológicas comunitarias, desarrollado como parte del programa de estudios de desarrollo de software en CECyTeM Plantel Chimalhuacán. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre registros de impacto ambiental, conectando un backend en Flask alojado en Render con una base de datos PostgreSQL alojada en Neon.

---

## 🚀 Tecnologías Utilizadas

* **Lenguaje Backend:** Python 3.11+
* **Framework Web:** Flask (con Jinja2 para renderizado de plantillas HTML)
* **Servidor WSGI:** Gunicorn
* **Conector de Base de Datos:** Psycopg (PostgreSQL)
* **Base de Datos Remota:** Neon (PostgreSQL en la nube)
* **Plataforma de Despliegue (PaaS):** Render
* **Control de Versiones:** Git y GitHub

---

## 🔗 Enlaces Oficiales del Proyecto

* **Sitio Web Público (Render):** https://ecoreto-53pw.onrender.com
* **Repositorio de Código (GitHub):** https://github.com/Henrry2027/EcoReto

---

## 🛠️ Arquitectura del Proyecto

EcoReto/
├── instance/               # Archivos locales / contexto de app
├── static/                 # Hojas de estilo CSS e imágenes estáticas
├── templates/              # Plantillas HTML (Jinja2)
├── app.py                  # Lógica de las rutas CRUD y consultas SQL
├── wsgi.py                 # Punto de entrada WSGI para Gunicorn en Render
├── requirements.txt        # Dependencias de Python del proyecto
└── README.md               # Documentación general del proyecto

---

## ⚙️ Configuración e Instalación Local

1. Clonar el repositorio:
   git clone https://github.com/Henrry2027/EcoReto.git
   cd EcoReto

2. Crear y activar un entorno virtual (opcional pero recomendado):
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Configurar Variable de Entorno:
   Crea una variable de entorno llamada DATABASE_URL con tu cadena de conexión a PostgreSQL de Neon:
   # En Linux/Mac:
   export DATABASE_URL="postgresql://usuario:password@ep-flat-wildflower-b4kbyqz3-pooler.c-6.us-east-2.aws.neon.tech/neondb?sslmode=require"
   # En Windows PowerShell:
   $env:DATABASE_URL="postgresql://usuario:password@ep-flat-wildflower-b4kbyqz3-pooler.c-6.us-east-2.aws.neon.tech/neondb?sslmode=require"

5. Iniciar el servidor local:
   python app.py

---

## 📋 Estructura de la Base de Datos (Neon)

CREATE TABLE IF NOT EXISTS acciones (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descripcion TEXT NOT NULL,
    propuesto_por VARCHAR(100) NOT NULL
);

---

## 🔒 Seguridad de Credenciales

Este repositorio no almacena credenciales ni cadenas de conexión hardcodeadas en el código fuente. La variable DATABASE_URL es administrada de forma segura a través del panel de Environment Variables de Render para proteger los secretos del servidor.
