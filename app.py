"""
Canada Housing & Job Market Dashboard
--------------------------------------
A live, filterable Streamlit dashboard built on (synthetic placeholder)
Canadian housing price and job market data.

HOW TO USE WITH REAL DATA:
- Replace generate_sample_data() with a loader that reads a CSV from
  Statistics Canada (https://www150.statcan.gc.ca/) or Toronto Open Data
  (https://open.toronto.ca/).
- Keep the column names consistent (city, date, avg_price, listings, jobs_posted)
  or update the filters below to match your real columns.

RUN LOCALLY:
    pip install -r requirements.txt
    streamlit run app.py

DEPLOY:
    Push this folder to a public GitHub repo, then deploy free on
    https://streamlit.io/cloud (Streamlit Community Cloud).
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Canada Housing & Job Market Dashboard", layout="wide")


@st.cache_data
def generate_sample_data():
    """Synthetic placeholder data. Swap this out for a real StatCan/Toronto Open Data CSV."""
    cities = ["Toronto", "Vancouver", "Calgary", "Ottawa", "Montreal", "Edmonton"]
    dates = pd.date_range(end=datetime.today(), periods=36, freq="MS")  # 3 years monthly

    rows = []
    rng = np.random.default_rng(42)
    base_prices = {"Toronto": 1_100_000, "Vancouver": 1_250_000, "Calgary": 550_000,
                   "Ottawa": 650_000, "Montreal": 500_000, "Edmonton": 420_000}

    for city in cities:
        trend = rng.normal(0.004, 0.01, len(dates)).cumsum()
        for i, date in enumerate(dates):
            price = base_prices[city] * (1 + trend[i]) + rng.normal(0, 8000)
            listings = max(50, int(rng.normal(300, 60)))
            jobs_posted = max(20, int(rng.normal(450, 100) * (1 + trend[i] * 0.5)))
            rows.append({
                "city": city, "date": date, "avg_price": round(price, -2),
                "listings": listings, "jobs_posted_ds_ai": jobs_posted
            })
    return pd.DataFrame(rows)


df = generate_sample_data()

st.title("🍁 Canada Housing & DS/AI Job Market Dashboard")
st.caption("Synthetic demo data — swap in real StatCan / Toronto Open Data CSVs for production use.")

# --- Sidebar filters ---
st.sidebar.header("Filters")
cities = st.sidebar.multiselect("City", sorted(df["city"].unique()), default=list(df["city"].unique()))
date_range = st.sidebar.date_input(
    "Date range",
    value=(df["date"].min().date(), df["date"].max().date()),
    min_value=df["date"].min().date(),
    max_value=df["date"].max().date(),
)

filtered = df[df["city"].isin(cities)]
if len(date_range) == 2:
    start, end = date_range
    filtered = filtered[(filtered["date"].dt.date >= start) & (filtered["date"].dt.date <= end)]

# --- KPI row ---
col1, col2, col3 = st.columns(3)
col1.metric("Avg. Home Price", f"${filtered['avg_price'].mean():,.0f}")
col2.metric("Avg. Monthly Listings", f"{filtered['listings'].mean():,.0f}")
col3.metric("Avg. DS/AI Jobs Posted/Month", f"{filtered['jobs_posted_ds_ai'].mean():,.0f}")

# --- Charts ---
st.subheader("Average Home Price Over Time")
fig1 = px.line(filtered, x="date", y="avg_price", color="city", markers=True)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("DS/AI Job Postings Over Time")
fig2 = px.line(filtered, x="date", y="jobs_posted_ds_ai", color="city", markers=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Listings vs. Price (latest month, by city)")
latest = filtered[filtered["date"] == filtered["date"].max()]
fig3 = px.scatter(latest, x="listings", y="avg_price", size="jobs_posted_ds_ai",
                   color="city", hover_name="city", size_max=40)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Built with Streamlit + Plotly. Data source: synthetic demo — replace with StatCan / Toronto Open Data for a real deployment.")
