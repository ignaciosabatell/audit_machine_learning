import streamlit as st
import pandas as pd
import joblib

st.title("Análisis de Empresas desde Archivo CSV")

st.write("""
Sube un archivo CSV con los datos de las empresas y el modelo te dirá si son fraudulentas o no.
El CSV debe contener las columnas utilizadas por el modelo.
""")

# Cargar modelo entrenado
best_model = joblib.load("best_model.pkl")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Datos cargados")
        st.write(df.head())

        # Filtrar solo las columnas que usa el modelo
        columns_model = best_model.feature_names_in_
        df_model = df[columns_model]

        # Predecir
        pred = best_model.predict(df_model)
        df["Predicción_fraude"] = pred

        st.subheader("Predicciones")
        st.write(df)

        st.success("Predicciones realizadas correctamente!")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
