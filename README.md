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

Copiá el archivo `.env.example` a `.env` y completá los valores requeridos. El archivo contiene:

```env
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
DATABASE_URL=postgresql://user:pass@localhost:5432/fake
```

## Uso local

Iniciá la aplicación con:
```bash
uvicorn app.synaptica_main:app --host 0.0.0.0 --port 7860
```
Luego ingresá en `http://localhost:7860/public/synaptica-tester.html` para ver la interfaz de prueba.

## Despliegue en Railway

1. Crea un nuevo proyecto en [Railway](https://railway.app/).
2. Sube el código de este repositorio.
3. Configura las variables de entorno según tu `.env`.
4. Railway utilizará el `Procfile` incluido, que ejecuta:
   ```bash
   uvicorn app.synaptica_main:app --host=0.0.0.0 --port=7860
   ```
5. Despliega y verifica el servicio.

## Estructura

- **public/**: archivos estáticos y `synaptica-tester.html` para pruebas visuales.
- **app/**: módulos Python principales (`synaptica_main.py`).
- **tests/**: carpeta para futuras pruebas.

¡Listo para comenzar a probar tus aplicaciones! 
