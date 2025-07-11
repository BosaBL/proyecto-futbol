# Registro Fútbol

Un proyecto simple de Django para gestionar equipos y jugadores de fútbol.

## Backup de la Base de Datos

El proyecto cuenta con el archivo `db.sqlite3.bak` que sirve como backup para la base de datos, de ser necesario copiarlo y cambiar el nombre a `db.sqlite3` para recuperar el estado original.

## Rutas Disponibles

### Interfaz Web

- `/`: Redirige a la lista de jugadores.
- `/equipos/`: Lista todos los equipos.
- `/equipos/crear/`: Añade un nuevo equipo.
- `/equipos/editar/<id>/`: Edita un equipo existente.
- `/equipos/eliminar/<id>/`: Elimina un equipo.
- `/jugadores/`: Lista todos los jugadores.
- `/jugadores/crear/`: Añade un nuevo jugador.
- `/jugadores/editar/<id>/`: Edita un jugador existente.
- `/jugadores/eliminar/<id>/`: Elimina un jugador.

### Endpoints de la API

- `/api/paises/<id>/`: Obtiene detalles de un país.
- `/api/equipos/`: Lista o crea equipos.
- `/api/equipos/<id>/`: Obtiene, actualiza o elimina un equipo.
- `/api/torneos/`: Lista torneos.
- `/api/jugadores/`: Lista o crea jugadores.
- `/api/jugadores/<id>/`: Obtiene, actualiza o elimina un jugador.
- `/api/partidos/`: Lista partidos.

## Instalación

1.  **Crear un entorno virtual:**
    ```sh
    python -m venv .venv
    ```

2.  **Activar el entorno:**
    -   En Windows:
        ```sh
        .\.venv\Scripts\activate
        ```
    -   En macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```

3.  **Instalar dependencias:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Ejecutar las migraciones de la base de datos:**
    ```sh
    python manage.py migrate
    ```

5.  **Ejecutar el servidor de desarrollo:**
    ```sh
    python manage.py runserver
    ```
