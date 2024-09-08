# Proyecto Blog en Django

Este proyecto es una aplicación web estilo blog desarrollada con Python y Django.

## Características

- Creación, edición y eliminación de blogs.
- Registro y autenticación de usuarios.
- Comentarios en los blogs.
- Páginas de perfil de usuario.
- Funcionalidades CRUD completas para blogs y comentarios.
- Página de "Acerca de mí" con información de los creadores del blog.

## Instalación

1. Clona el repositorio:
    ```
    git clone <URL_DEL_REPOSITORIO>
    ```
2. Navega al directorio del proyecto:
    ```
    cd mi_blog
    ```
3. Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```
4. Aplica las migraciones de la base de datos:
    ```
    python manage.py migrate
    ```
5. Crea un superusuario para acceder al admin:
    ```
    python manage.py createsuperuser
    ```
6. Inicia el servidor de desarrollo:
    ```
    python manage.py runserver
    ```

## Funcionalidades

- **Páginas**: Puedes ver todas las páginas en el route `/pages/`.
- **Detalles de blog**: Haciendo clic en "Leer más" puedes ver el detalle del blog.
- **Perfil**: Los usuarios pueden ver y editar su perfil en `/accounts/profile/`.
- **Administrador**: Gestiona los blogs, usuarios y comentarios desde `/admin/`.

## Casos de prueba

Los casos de prueba están incluidos en el archivo excel.
