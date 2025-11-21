import streamlit as st
import pandas as pd

st.title("Información del Dataset de Auditoría")

st.write("""
Este apartado permite consultar el dataset original utilizado para entrenar el modelo
de detección de fraude.
""")

df = pd.read_csv("audit_risk.csv")
st.dataframe(df)


st.title("Información del Dataset de Auditoría")

st.write("""
Este apartado permite consultar el dataset original utilizado para entrenar el modelo de detección de fraude.
Los datos proceden del repositorio UCI Machine Learning Repository (Audit Data).
""")

# Cargar dataset
@st.cache_data
def load_data():
    return pd.read_csv("audit_risk.csv")  # ajusta nombre si es distinto

df = load_data()

st.subheader("Vista general del dataset")
st.dataframe(df)

st.subheader("Dimensiones del dataset")
st.write(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

st.subheader("Descripción de las variables")
st.write("""
**Sector_score:** Puntuación del riesgo asociado al sector económico.  
**LOCATION_ID:** Identificador numérico de la localización.  
**PARA_A / PARA_B:** Indicadores preliminares de auditoría.  
**Score_A, Score_B, Score_B.1, Score_MV:** Distintos scores cuantitativos calculados por los auditores.  
**Risk_A, Risk_B, Risk_C, Risk_D, Risk_E, Risk_F:** Medidas específicas de riesgo por categoría.  
**TOTAL:** Indicador agregado de riesgo.  
**numbers:** Frecuencia de auditorías previas o hallazgos.  
**Money_Value:** Valor económico asociado a operaciones.  
**History:** Registro histórico del comportamiento de la entidad.  
**Prob / PROB:** Probabilidad estimada de riesgo inicial.  
**Score:** Score global de riesgo.  
**Inherent_Risk:** Riesgo inherente según el auditor.  
**CONTROL_RISK:** Riesgo de control.  
**Detection_Risk:** Riesgo de detección.  
**Audit_Risk:** Riesgo total de auditoría.  
**Risk:** Variable objetivo (0 = no fraudulenta, 1 = fraudulenta).
""")

st.subheader("Estadísticas descriptivas")
st.write(df.describe())
