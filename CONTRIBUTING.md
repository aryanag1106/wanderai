# Contributing to WanderAI

## Setup
```bash
git clone https://code.swecha.org/AryanAg/individual-hackathon-aryan-wanderai.git
cd individual-hackathon-aryan-wanderai
pip install -r requirements.txt
```

## Running locally
```bash
export GROQ_API_KEY=your_key
streamlit run app.py
```

## Code style
We use `ruff` for linting. Run before committing:
```bash
pip install ruff
ruff check .
```
