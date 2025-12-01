## Proyecto de análisis de auditoría con Machine Learning

Este proyecto desarrolla un modelo de *machine learning* para predecir la probabilidad de fraude en auditorías internas. A partir de un conjunto de variables de riesgo (inherente, de control y de detección), junto con puntuaciones sectoriales y métricas específicas de cada área, se genera un clasificador que determina si un caso es **fraudulento** o **no fraudulento**.

La aplicación final está implementada en **Streamlit**, permitiendo cargar datos, visualizar correlaciones, ejecutar el modelo y obtener predicciones en tiempo real.


## Variables utilizadas

Para el dataset reducido final (el usado en el modelo y en Streamlit), solo se emplean las siguientes columnas:

* Sector_score
* Score_A
* Risk_A
* TOTAL
* Score_B.1
* Score_MV
* PROB
* RiSk_E
* Prob
* Score
* Inherent_Risk
* CONTROL_RISK
* Detection_Risk

* `Risk`  *(variable objetivo, 1 = fraude, 0 = no fraude)*

Estas variables se seleccionaron por su peso predictivo y por la correlación con la variable objetivo.

---

## Flujo del modelo

1. **Carga del dataset**
   Se leen los datos y se seleccionan las columnas relevantes.

2. **Preprocesado**

   * Eliminación de nulos
   * Estandarización de variables numéricas
   * Separación en *train* y *test*

3. **Entrenamiento**
   Se probó con varios modelos:

   * Random Forest
   * AdaBoost
   * Gradient Boosting
   * KNN

   El mejor rendimiento lo ofreció el que estás utilizando actualmente en tu notebook (según tus pruebas internas).

4. **Evaluación**

   * Accuracy
   * Matriz de confusión
   * F1 Score
   * ROC-AUC

5. **Exportación del modelo**
   El modelo final se guarda en `best_model.pkl`.

6. **Implementación en Streamlit**
   La aplicación permite:

   * Analizar un CSV
   * Ejecutar la predicción para cada fila
  

---

## Streamlit

### Ejecución local

1. Instalar dependencias:

```
pip install -r requirements.txt
```

2. Ejecutar la aplicación:

```
streamlit run app.py
```

### Funcionalidades de la app

* Selector de empresa (o dataset)
* Visualización gráfica (correlaciones, distribución de riesgos)
* Predicción caso a caso
* Descarga del archivo con predicciones

---

## Dataset ficticio de pruebas

El archivo `test_sample.csv` contiene 30+ filas con valores realistas para las columnas requeridas. Lo puedes ampliar en cualquier momento para testear comportamiento del modelo.

---

## Licencia

Uso académico y experimental.

