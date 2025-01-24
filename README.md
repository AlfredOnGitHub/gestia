# Gestia - Proyecto de Gestión

Gestia es una aplicación de gestión que permite realizar el registro y autenticación de usuarios, y gestionar inventarios de productos. Desarrollada en Django y Python.

## Requisitos

- Python 3.x
- Django 3.x o superior
- Otras dependencias de Python (consultar `requirements.txt`)
  
## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu_usuario/gestia.git
    cd gestia
    ```

2. **Crear un entorno virtual (opcional pero recomendado)**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar las variables de entorno**:
    - Crea un archivo `.env` en la raíz del proyecto.
    - Asegúrate de incluir las variables de configuración como:
        ```bash
        DEBUG=True
        SECRET_KEY='tu_clave_secreta'
        DATABASE_URL='sqlite:///db.sqlite3'
        ```

5. **Realizar las migraciones de la base de datos**:
    ```bash
    python manage.py migrate
    ```

6. **Ejecutar el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

    Puedes acceder a la aplicación en `http://127.0.0.1:8000/`.

## Funcionalidades

- **Registro de usuarios**: Los usuarios pueden crear una cuenta con su correo electrónico y contraseña.
- **Inicio y cierre de sesión**: Los usuarios pueden iniciar y cerrar sesión en la aplicación.
- **Recuperación de contraseña**: Los usuarios pueden recuperar su contraseña en caso de olvido.
- **Gestión de inventarios**: Los administradores pueden gestionar productos en el inventario.

## Pruebas

Si tienes pruebas automatizadas configuradas, puedes ejecutar los tests con el siguiente comando:

```bash
python manage.py test
```

## Contribución

Si deseas contribuir al proyecto, por favor abre un pull request con tus cambios. Asegúrate de seguir la convención de estilo de código de Python y Django.

