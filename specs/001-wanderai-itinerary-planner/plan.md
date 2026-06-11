# Plan: WanderAI — AI Travel Itinerary Planner

**Feature:** 001-wanderai-itinerary-planner  
**Author:** Aryan Agarwal  
**Date:** June 2026  
**Input:** specs/001-wanderai-itinerary-planner/spec.md

---

## Architecture Overview

```
User (Browser)
     │
     ▼
┌─────────────────────────────┐
│      Streamlit Frontend      │
│  ┌────────────────────────┐ │
│  │   Input Form (col1/2)  │ │
│  │   - destination        │ │
│  │   - days slider        │ │
│  │   - budget (₹ INR)     │ │
│  │   - hotel preference   │ │
│  │   - travel month       │ │
│  │   - travel style       │ │
│  │   - group type         │ │
│  │   - interests          │ │
│  └────────────────────────┘ │
│             │                │
│             ▼                │
│  ┌────────────────────────┐ │
│  │   Prompt Builder       │ │
│  │   f-string injection   │ │
│  └────────────────────────┘ │
│             │                │
└─────────────┼───────────────┘
              │
              ▼
┌─────────────────────────────┐
│        Groq API              │
│   llama-3.3-70b-versatile   │
│   temp=0.7, max_tokens=4000 │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│     JSON Response Parser     │
│   strip fences → json.loads │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│     Streamlit Result UI      │
│  - Metrics row               │
│  - Weather info box          │
│  - Hotel recommendation      │
│  - Food badges               │
│  - Day cards (loop)          │
│  - Budget breakdown          │
│  - Practical tips            │
│  - Packing tips              │
│  - Currency note             │
└─────────────────────────────┘
```

---

## File Structure

```
wanderai/
├── app.py                              ← entire application
├── requirements.txt                    ← streamlit, groq
├── README.md                           ← project overview
├── .gitignore                          ← excludes secrets.toml
├── .streamlit/
│   ├── config.toml                     ← theme: teal/off-white
│   └── secrets.toml                    ← GROQ_API_KEY (not in git)
└── specs/
    └── 001-wanderai-itinerary-planner/
        ├── spec.md                     ← this feature's requirements
        ├── plan.md                     ← this file
        ├── tasks.md                    ← ordered task list
        └── data-model.md              ← AI response schema
```

---

## Component Design

### 1. Input Form (`st.form`)

Groups all inputs so no partial submissions occur. Uses two columns (`st.columns(2)`) for clean layout.

**Inputs and widgets:**

| Field | Widget | Validation |
|-------|--------|-----------|
| Destination | `st.text_input` | Must not be empty |
| Days | `st.slider(1, 14)` | Always valid |
| Travel style | `st.selectbox` | Always valid |
| Travel month | `st.selectbox` | Always valid |
| Budget (₹ INR) | `st.number_input(min=1000, max=1000000, step=1000)` | Always valid |
| Hotel preference | `st.selectbox` | Always valid |
| Travelling as | `st.selectbox` | Always valid |
| Interests | `st.text_input` | Optional |

### 2. Prompt Builder

Constructs a detailed f-string prompt injecting all user inputs. Key decisions:
- Pre-calculates `per_day_budget = budget_per_person // days` and injects it
- Explicitly instructs: `"All prices MUST be in ₹ INR"`
- Specifies `"for Indian travellers"` to anchor cultural context
- Requests JSON-only output with exact schema — no markdown, no explanation

### 3. Groq API Call

```python
client = Groq(api_key=api_key)
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=4000,
)
```

- `temperature=0.7` — creative but coherent
- `max_tokens=4000` — handles up to 14-day itineraries
- API key read from `st.secrets` first, falls back to `os.environ`

### 4. Response Parser

```python
raw = response.choices[0].message.content.strip()
if raw.startswith("```"):
    raw = raw.split("```")[1]
    if raw.startswith("json"):
        raw = raw[4:]
data = json.loads(raw.strip())
```

Defensively strips markdown fences before JSON parsing.

### 5. Result Display

Rendered in this order:
1. Destination heading + tagline
2. Metrics row (days, budget, month, group)
3. Weather info box (`st.info`)
4. Hotel recommendation (`st.success`)
5. Must-try food badges (HTML pills)
6. Day-by-day cards (HTML loop)
7. Budget breakdown box (HTML green box)
8. Practical tips box (HTML orange box)
9. Packing tips + currency note

---

## API Response Schema

See `data-model.md` for the full JSON schema the AI is instructed to return.

---

## Security Design

- API key stored in `.streamlit/secrets.toml` locally (excluded from git via `.gitignore`)
- On Streamlit Cloud, key is stored in the dashboard Secrets section — never in code
- No user data collected or stored — fully stateless
- No database — session state only

---

## Decision Log

| Decision | Rationale |
|----------|-----------|
| Groq over Gemini | Gemini free tier hit daily quota limits during testing; Groq has no such issues |
| Llama 3.3 70B | Strong structured JSON generation, free, fast via Groq's LPU hardware |
| Streamlit over Flask/FastAPI | Hackathon scope — Streamlit gives a full UI with zero frontend code |
| INR-first design | Target users are Indian travellers; eliminating currency conversion is a core value |
| Stateless architecture | No database needed, simplifies deployment, zero infrastructure cost |
| Single file (`app.py`) | Appropriate for hackathon scope; no need to split into modules |
