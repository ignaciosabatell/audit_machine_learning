import streamlit as st
import pandas as pd
import numpy as np
import joblib  # Para cargar tu modelo

st.set_page_config(page_title="Fraude Auditoría", page_icon="🕵️‍♂️")


# Cargar el modelo entrenado
best_model = joblib.load("best_model.pkl")  # Cambia el nombre si tu modelo tiene otro

st.image("logo.png", width=250)
st.title("Predicción de Empresas Fraudulentas")
st.write("Introduce los datos de la empresa y obtén la predicción.")

# Crear inputs para cada feature
import streamlit as st

st.title("Predicción de Empresas Fraudulentas")
st.write("Introduce los datos de la empresa y obtén la predicción. Todas las puntuaciones son estimaciones de riesgo basadas en auditorías.")

Sector_score = st.number_input(
    "Sector Score", 
    min_value=0.0, 
    max_value=10.0, 
    value=3.89,
    help="Riesgo promedio del sector al que pertenece la empresa (0 = bajo, 10 = alto)"
)

Score_A = st.number_input(
    "Score A", 
    min_value=0.0, 
    max_value=10.0, 
    value=0.6,
    help="Puntuación asociada a un parámetro de auditoría específico"
)

Risk_A = st.number_input(
    "Risk A", 
    min_value=0.0, 
    max_value=10.0, 
    value=2.5,
    help="Riesgo calculado para el parámetro A"
)

TOTAL = st.number_input(
    "TOTAL", 
    min_value=0.0, 
    max_value=50.0, 
    value=6.68,
    help="Suma ponderada de varios scores de riesgo"
)

Score_B_1 = st.number_input(
    "Score B.1", 
    min_value=0.0, 
    max_value=10.0, 
    value=0.2,
    help="Puntuación asociada al parámetro B"
)

Score_MV = st.number_input(
    "Score MV", 
    min_value=0.0, 
    max_value=10.0, 
    value=0.2,
    help="Score relacionado con valores monetarios"
)

PROB = st.number_input(
    "PROB", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.2,
    help="Probabilidad de que se materialice el riesgo total"
)

RiSk_E = st.number_input(
    "Risk E", 
    min_value=0.0, 
    max_value=10.0, 
    value=0.4,
    help="Riesgo calculado para el parámetro E"
)

Prob_col = st.number_input(
    "Prob", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.2,
    help="Probabilidad asociada a un riesgo específico"
)

Score = st.number_input(
    "Score", 
    min_value=0.0, 
    max_value=10.0, 
    value=2.4,
    help="Score general de riesgo de la empresa"
)

Inherent_Risk = st.number_input(
    "Inherent Risk", 
    min_value=0.0, 
    max_value=10.0, 
    value=8.574,
    help="Riesgo inherente del negocio sin controles internos"
)

CONTROL_RISK = st.number_input(
    "Control Risk", 
    min_value=0.0, 
    max_value=10.0, 
    value=0.4,
    help="Riesgo de que los controles internos fallen"
)

Detection_Risk = st.number_input(
    "Detection Risk", 
    min_value=0.0, 
    max_value=10.0, 
    value=0.5,
    help="Riesgo de que los auditores no detecten fraude o errores"
)


# Botón para predecir
if st.button("Predecir"):
    # Crear DataFrame con los datos introducidos
    nuevos_datos = pd.DataFrame({
        "Sector_score": [Sector_score],
        "Score_A": [Score_A],
        "Risk_A": [Risk_A],
        "TOTAL": [TOTAL],
        "Score_B.1": [Score_B_1],
        "Score_MV": [Score_MV],
        "PROB": [PROB],
        "RiSk_E": [RiSk_E],
        "Prob": [Prob_col],
        "Score": [Score],
        "Inherent_Risk": [Inherent_Risk],
        "CONTROL_RISK": [CONTROL_RISK],
        "Detection_Risk": [Detection_Risk]
    })

    # Predicción
    pred = best_model.predict(nuevos_datos)
    prob = best_model.predict_proba(nuevos_datos)

    st.write("### Resultado de la predicción:")
    if pred[0] == 1:
        st.error("La empresa es **fraudulenta**")
    else:
        st.success("La empresa **no es fraudulenta**")

    st.write("### Probabilidades:")
    st.write(f"No fraude: {prob[0][0]:.2f}")
    st.write(f"Fraude: {prob[0][1]:.2f}")