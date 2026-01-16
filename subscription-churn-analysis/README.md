# Análisis de Churn de Clientes en Telecomunicaciones

## Descripción general

Este proyecto presenta un **análisis exploratorio y de negocio (EDA)** sobre el churn de clientes en un servicio de telecomunicaciones, utilizando el dataset **Telco Customer Churn**.

El objetivo es **identificar patrones de comportamiento, variables de negocio y señales tempranas** que expliquen la cancelación de clientes, generando **insights accionables** que puedan ser utilizados por equipos de producto, marketing o customer success para reducir el churn.

---

## Objetivo del análisis

- Analizar los **factores que influyen en el churn de clientes**
- Detectar **patrones de uso y comportamiento**
- Evaluar el impacto de:
  - Tipo de contrato
  - Servicios contratados
  - Variables económicas
  - Antigüedad y uso del servicio
- Proponer **conclusiones orientadas a negocio**, no solo estadísticas

> El enfoque del proyecto es **analítico y estratégico**, no de modelado predictivo.

---

## Dataset

**Fuente:**  
Telco Customer Churn – Kaggle  
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**Descripción:**
- ~7.000 clientes
- Variables demográficas, contractuales, de servicios y facturación
- Variable objetivo: `Churn`

---

## Enfoque metodológico

El análisis sigue una estructura profesional típica en entornos de data analytics:

1. **Comprensión del problema de negocio**
2. **Inspección estructural del dataset**
3. **Análisis de calidad de datos**
4. **Exploración univariada y bivariada**
5. **Análisis de churn por segmentos**
6. **Correlaciones y señales tempranas**
7. **Conclusiones accionables**

Se prioriza:
- Interpretabilidad
- Coherencia entre gráficos y conclusiones
- Relevancia para decisiones reales de negocio

---

## Principales insights

Algunos hallazgos relevantes del análisis:

- Clientes con **contratos mensuales** presentan mayor churn que aquellos con contratos a largo plazo.
- La **antigüedad del cliente (tenure)** es uno de los factores más fuertes: clientes nuevos churnean más.
- Ciertos servicios (ej. soporte técnico, seguridad online) están asociados a **menor churn**.
- El churn no se explica únicamente por desuso, sino por una **combinación de precio, contrato y valor percibido**.

> Estos resultados reflejan patrones comunes en empresas de telecomunicaciones reales.

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Estructura del proyecto

``` 
subscription-churn-analysis/
│
├── notebooks/
│ └── initial_exploration.ipynb
│
├── data/
│ └── raw/
│      └── telco_customer_churn.csv
│
├── test/
│
├── requirements.txt
└── README.md
``` 

---

## Próximos pasos (no incluidos)

Este proyecto se enfoca en análisis exploratorio. Posibles extensiones:

- Feature engineering avanzado
- Modelos predictivos de churn
- Scoring de riesgo por cliente
- Simulación de impacto de retención

---

## Autor

**Lautaro Orellano**  
Data Analyst  

Proyecto desarrollado con fines de **portfolio profesional** y demostración de habilidades analíticas aplicadas a problemas reales de negocio.

