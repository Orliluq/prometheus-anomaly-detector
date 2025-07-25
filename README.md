# Prometheus Anomaly Detector

Este proyecto es una aplicación web interactiva desarrollada con Streamlit para la detección de anomalías en métricas de latencia obtenidas desde un servidor Prometheus. Está pensado para facilitar el monitoreo y análisis de servicios, permitiendo identificar comportamientos anómalos en la latencia de las solicitudes HTTP de manera automática.

## ¿Cómo funciona?
La aplicación se conecta a un servidor Prometheus, consulta la métrica `http_request_duration_seconds` en un rango de fechas definido por el usuario, y aplica un modelo de aprendizaje automático (Isolation Forest) para detectar posibles anomalías en los valores de latencia. Los resultados se visualizan de forma gráfica e intuitiva.

## Estructura del proyecto

- `streamlit_app.py`: Código principal de la aplicación Streamlit. Aquí se define la interfaz, la lógica de conexión a Prometheus y el análisis de anomalías.
- `requirements.txt`: Lista de dependencias de Python necesarias para ejecutar la aplicación.
- `Dockerfile`: Define la imagen Docker para la aplicación Streamlit.
- `docker-compose.yml`: Orquesta el despliegue de Prometheus y la aplicación de Streamlit en contenedores.
- `prometheus.yml`: Archivo de configuración para el servidor Prometheus.
- `LICENSE`: Licencia MIT del proyecto.

## Requisitos
- Docker y Docker Compose instalados en el sistema.

## Instrucciones de uso

1. Clona este repositorio:
   ```bash
   git clone <url-del-repo>
   cd prometheus-anomaly-detector
   ```

2. Levanta los servicios con Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Accede a la aplicación Streamlit en tu navegador en [http://localhost:8501](http://localhost:8501).

4. Configura la URL de Prometheus (por defecto es `http://prometheus:9090`) y selecciona el rango de fechas para analizar. Haz clic en "Analizar" para detectar anomalías.

## Notas
- El archivo `prometheus.yml` configura el scraping de métricas en Prometheus.
- Puedes modificar el modelo de detección de anomalías en `streamlit_app.py` según tus necesidades.

---

Proyecto bajo licencia MIT.