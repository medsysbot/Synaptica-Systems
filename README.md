# Synaptica Systems Tester

Este proyecto permite probar y validar los aplicativos de MedSys de forma sencilla. Incluye un entorno listo para desplegarse en Railway.

## Objetivo

Facilitar las pruebas automatizadas y manuales de los servicios de Synaptica Systems.

## Instalación

1. Cloná el repositorio.
2. Creá un entorno virtual y activalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/macOS
   .\\venv\\Scripts\\activate  # En Windows
   ```
3. Instalá las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Variables de entorno

Copiá el archivo `.env.example` a `.env` y completá los valores requeridos.

## Uso local

Iniciá la aplicación con:
```bash
uvicorn app.synaptica_main:saludo
```
Esto mostrará un mensaje de bienvenida básico.

## Despliegue en Railway

1. Crea un nuevo proyecto en [Railway](https://railway.app/).
2. Sube el código de este repositorio.
3. Configura las variables de entorno según tu `.env`.
4. Utiliza un comando de inicio similar a:
   ```bash
   uvicorn app.synaptica_main:saludo --host 0.0.0.0 --port $PORT
   ```
5. Despliega y verifica el servicio.

## Estructura

- **public/**: archivos estáticos y `synaptica-tester.html` para pruebas visuales.
- **app/**: módulos Python principales (`synaptica_main.py`).
- **tests/**: carpeta para futuras pruebas.

¡Listo para comenzar a probar tus aplicaciones! 
