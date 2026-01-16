# Diccionario de Datos – Dataset de Churn en SaaS

## churned
- **Tipo:** Binario (0 / 1)
- **Descripción:** Indica si el usuario abandonó el servicio (churn).
- **Valores:**
  - 0 → El usuario permanece activo
  - 1 → El usuario hizo churn

## tickets_per_session
- **Tipo:** Numérico continuo
- **Descripción:** Promedio de tickets de soporte abiertos por sesión en los últimos 30 días.
- **Interpretación:** Valores altos pueden indicar fricción, problemas con el producto o insatisfacción del usuario.

## activity_ratio
- **Tipo:** Numérico continuo (0 a 1)
- **Descripción:** Relación entre las sesiones realizadas en los últimos 7 días y el total de sesiones en los últimos 30 días.
- **Interpretación:**
  - Cercano a 1 → Usuario con alta actividad reciente
  - Cercano a 0 → Caída en la actividad del usuario

## payment_risk
- **Tipo:** Entero
- **Descripción:** Indicador de riesgo de pago calculado a partir de pagos fallidos ponderados por el tipo de plan.
- **Interpretación:** Valores más altos indican mayor probabilidad de churn por problemas económicos o de facturación.

## pro_low_activity
- **Tipo:** Binario (0 / 1)
- **Descripción:** Identifica a usuarios del plan Pro con menos de 5 sesiones en los últimos 30 días.
- **Interpretación:** Puede señalar usuarios premium en riesgo por bajo uso del producto.
