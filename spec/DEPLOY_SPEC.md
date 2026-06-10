# WanderAI — Deployment Specification

**Version:** 1.0  
**Date:** June 2026  
**Team:** Aryan Agarwal (Solo)

---

## 1. Prerequisites

| Requirement | Version | Notes |
|------------|---------|-------|
| Python | 3.9+ | 3.10+ recommended |
| pip | Latest | For installing dependencies |
| Git | Any recent | For cloning the repository |
| Groq account | — | Free at console.groq.com — no credit card needed |

---

## 2. Local Setup

### Step 1 — Clone the Repository

```bash
git clone https://code.swecha.org/AryanAg/individual-hackathon-aryan-wanderai.git
cd individual-hackathon-aryan-wanderai
```

### Step 2 — (Recommended) Create a Virtual Environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Your Groq API Key

Get a free key at **https://console.groq.com** → API Keys → Create Key.

```bash
# macOS / Linux
export GROQ_API_KEY=your_groq_api_key_here

# Windows (cmd)
set GROQ_API_KEY=your_groq_api_key_here
```

Alternatively, create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### Step 5 — Run the App

```bash
streamlit run app.py
```

App opens at **http://localhost:8501**

---

## 3. Streamlit Cloud Deployment (Public URL)

### Step 1 — Push to GitHub

```bash
git remote add github https://github.com/yourusername/wanderai.git
git push github master
```

### Step 2 — Deploy on Streamlit Cloud

1. Go to **https://share.streamlit.io** and sign in with GitHub
2. Click **New app**
3. Select your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Advanced settings** → **Secrets** → paste:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
6. Click **Deploy**

A public URL of the format `https://yourname-wanderai.streamlit.app` will be live within 2 minutes.

---

## 4. Project Structure

```
wanderai/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── .gitignore              # Excludes secrets.toml and venv
├── .streamlit/
│   ├── config.toml         # Streamlit theme configuration
│   └── secrets.toml        # API keys (NOT committed to git)
└── specs/
    ├── PRD.md              # Product Requirements Document
    ├── AI_SPEC.md          # AI & model specification
    └── DEPLOY_SPEC.md      # This file
```

---

## 5. Dependencies

```
streamlit==1.35.0
groq==0.9.0
```

No external API keys other than Groq are required. No database. No Docker.

---

## 6. Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Groq API key from console.groq.com |

---

## 7. Security Notes

- `secrets.toml` is listed in `.gitignore` and is never committed to the repository
- The API key is read at runtime from environment variable or Streamlit secrets
- No user data is stored — the app is fully stateless
