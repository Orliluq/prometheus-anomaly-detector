import pandas as pd
import streamlit as st
from prometheus_api_client import PrometheusConnect, MetricRangeDataFrame
from sklearn.ensemble import IsolationForest
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="Anomaly Detector", layout="wide")
st.title("🚨 Detección de Anomalías en Latencia (Prometheus)")

# Configuración del servidor Prometheus
PROM_URL = st.text_input("URL de Prometheus", "http://prometheus:9090")

start_date = st.date_input("Fecha de inicio", datetime(2025, 7, 1))
end_date = st.date_input("Fecha de fin", datetime(2025, 7, 25))

if st.button("🔍 Analizar"):
    try:
        prom = PrometheusConnect(url=PROM_URL, disable_ssl=True)
        metric_data = prom.get_metric_range_data(
            metric_name="http_request_duration_seconds",
            start_time=datetime.combine(start_date, datetime.min.time()),
            end_time=datetime.combine(end_date, datetime.min.time()),
            chunk_size="1d"
        )

        df = MetricRangeDataFrame(metric_data)
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df = df.dropna(subset=['value'])

        X = df['value'].values.reshape(-1, 1)
        model = IsolationForest(contamination=0.01, random_state=42)
        model.fit(X)
        df['anomaly'] = model.predict(X)

        anomalies = df[df['anomaly'] == -1]
        st.success(f"✅ {len(anomalies)} anomalías detectadas")

        fig, ax = plt.subplots(figsize=(14, 5))
        ax.plot(df.index, df['value'], label="Latencia")
        ax.scatter(anomalies.index, anomalies['value'], color='red', label="Anomalías")
        ax.set_title("Anomalías en la métrica http_request_duration_seconds")
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Duración (s)")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error al conectarse o procesar datos: {e}")