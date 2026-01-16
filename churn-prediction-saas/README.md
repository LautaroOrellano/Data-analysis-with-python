# Análisis de Churn en SaaS

Este proyecto presenta un **análisis exploratorio de churn** utilizando un dataset simulado de actividad de usuarios en una plataforma SaaS.  
El objetivo es identificar **señales tempranas asociadas al abandono de usuarios** y entender cómo variables de uso, soporte y pagos se relacionan con el churn.

El enfoque está puesto tanto en el **análisis técnico** como en la **interpretación desde una perspectiva de negocio**.

---

## Objetivo del proyecto

- Analizar el comportamiento de usuarios que abandonan la plataforma (churn).
- Identificar métricas de actividad y fricción asociadas al churn.
- Explorar diferencias entre usuarios pagos y gratuitos.
- Practicar un flujo de trabajo profesional de análisis de datos con Python.

---

## Estructura del proyecto


```
data/
raw/
user_activity.csv # Dataset simulado
notebooks/
churn_analysis.ipynb # Análisis exploratorio principal
docs/
data_dictionary.md # Diccionario de datos
src/ # Código auxiliar
README.md
```


---

## Análisis realizado

El notebook incluye los siguientes pasos:

- Exploración inicial del dataset y distribución de churn
- Análisis de churn por tipo de plan
- Relación entre uso de la plataforma y churn
- Impacto de fallos de pago
- Creación de métricas de actividad reciente
- Feature engineering orientado a churn
- Análisis por cohortes (plan + nivel de actividad)
- Evaluación de correlaciones entre variables

Cada gráfico está acompañado por:
- una pregunta clara
- una observación basada en los datos
- una interpretación orientada a negocio

---

## Principales insights

- Los usuarios del plan Pro presentan una tasa de churn más alta que los usuarios gratuitos.
- La cantidad total de sesiones no muestra una diferencia clara entre usuarios que churnean y los que no.
- La actividad reciente (`activity_ratio`) es un indicador fuerte de churn.
- Los fallos de pago están asociados a una mayor probabilidad de abandono.
- Usuarios pagos con baja actividad presentan mayor riesgo de churn que usuarios gratuitos con el mismo nivel de uso.

---

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/LautaroOrellano/Churn-prediction-saas.git

pip install -r requirements.txt

jupyter notebook notebooks/churn_analysis.ipynb
```
---
## Nota

El dataset utilizado es sintético y fue generado con fines educativos.
Los resultados no deben interpretarse como conclusiones universales, sino como un ejercicio de análisis exploratorio orientado a prácticas reales de análisis de datos.
