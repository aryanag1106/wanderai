# ✈️ WanderAI – AI Travel Itinerary Planner

A Streamlit app that generates personalised day-by-day travel itineraries using Claude AI.

## Features
- 🗺️ Full day-by-day itinerary with morning / afternoon / evening activities
- 🍜 Must-try foods for the destination
- 💡 Practical travel tips
- 🎒 Personalised by travel style, budget, group type & interests

## Run locally

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your-key-here   # or set in .streamlit/secrets.toml
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Push this repo to GitHub/GitLab
2. Go to https://share.streamlit.io → New app → select your repo
3. Add `ANTHROPIC_API_KEY` in the Secrets section
4. Click Deploy
