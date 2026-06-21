# 🍁 Canada Housing & DS/AI Job Market Dashboard

An interactive Streamlit dashboard exploring housing prices and DS/AI job
posting trends across major Canadian cities. Built to demonstrate data
storytelling with real-world (or real-world-style) Canadian data — a strong
signal for Toronto-based recruiters that you're already thinking locally.

## Features
- City and date-range filters (multi-select + date picker)
- Live KPI cards (avg price, avg listings, avg job postings)
- Time-series line charts (price trend, job posting trend by city)
- Bubble scatter plot (listings vs. price vs. job demand)

## Tech Stack
Python · Streamlit · Pandas · NumPy · Plotly

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Free)
1. Push this repo to GitHub.
2. Go to https://streamlit.io/cloud, connect your GitHub repo.
3. Set `app.py` as the entry point. Done — you get a public live link.

## Next Steps (to make this production-grade)
- Replace `generate_sample_data()` with a real loader pulling from:
  - Statistics Canada: https://www150.statcan.gc.ca/
  - Toronto Open Data: https://open.toronto.ca/
  - CREA (Canadian Real Estate Association) housing stats
- Add caching with `@st.cache_data` on the real data loader (already scaffolded).
- Add a "download filtered data as CSV" button (`st.download_button`).
- Add forecasting (see the time-series forecasting project in this same project set)
  to predict next-quarter prices per city.

## Resume Bullet (suggested)
"Built and deployed an interactive Streamlit dashboard analyzing Canadian
housing and DS/AI job market trends across 6 cities, with dynamic filtering
and live KPI tracking."
