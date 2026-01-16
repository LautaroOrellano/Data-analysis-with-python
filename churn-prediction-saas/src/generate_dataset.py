import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

N_USERS = 8000
today = datetime.today()

rows = []

for user_id in range(1, N_USERS + 1):

    signup_date = today - timedelta(days=np.random.randint(60, 400))

    plan_type = np.random.choice(
        ["free", "pro"],
        p=[0.7, 0.3]
    )

    # Actividad base según plan
    base_sessions = 10 if plan_type == "free" else 18
    sessions_last_30d = np.random.poisson(base_sessions)

    # Decidimos churn (20–30% aprox)
    churn_probability = 0.25 if plan_type == "free" else 0.30
    churned = np.random.binomial(1, churn_probability)

    if churned:
        # Usuario en caída: muy poca actividad reciente
        sessions_last_7d = np.random.randint(0, max(1, sessions_last_30d // 6))
        days_since_last_activity = np.random.randint(31, 60)
    else:
        # Usuario estable
        sessions_last_7d = np.random.randint(
            max(1, sessions_last_30d // 4),
            sessions_last_30d + 1
        )
        days_since_last_activity = np.random.randint(0, 20)

    avg_session_time = np.random.normal(
        280 if plan_type == "free" else 550,
        100
    )

    tickets_opened = np.random.poisson(
        0.7 if churned else 0.3
    )

    payments_failed = np.random.binomial(
        1,
        0.20 if churned else 0.05
    )

    rows.append([
        user_id,
        signup_date,
        plan_type,
        sessions_last_7d,
        sessions_last_30d,
        avg_session_time,
        tickets_opened,
        payments_failed,
        days_since_last_activity,
        churned
    ])

columns = [
    "user_id",
    "signup_date",
    "plan_type",
    "sessions_last_7d",
    "sessions_last_30d",
    "avg_session_time",
    "tickets_opened",
    "payments_failed",
    "days_since_last_activity",
    "churned"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("data/raw/user_activity.csv", index=False)

print("Dataset regenerated:", df.shape)
