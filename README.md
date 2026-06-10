# ✈️ WanderAI — AI Travel Itinerary Planner

**Hackathon:** Individual Hackathon 2  
**Theme:** Open  
**Team:** Aryan Agarwal (Solo)  
**Date:** June 2026

---

## What is WanderAI?

WanderAI is an AI-powered travel planner that generates a complete, personalised day-by-day itinerary in seconds. Built for Indian travellers — all prices are in ₹ INR.

Just enter your destination, budget, travel month, and preferences — and get a full trip plan with activities, hotel recommendations, food tips, weather advice, and a detailed budget breakdown.

---

## Features

- 🗓️ **Day-by-day itinerary** — morning, afternoon, evening activities with specific places and ₹ INR costs
- 💰 **Budget in ₹ INR** — enter your budget excluding flights; get a full breakdown of hotel, food, activities, transport
- 🏨 **Hotel recommendation** — matched to your preference (hostel to 5-star) with per-night cost in INR
- 🌤️ **Weather & packing tips** — tailored to your month of travel
- 🍜 **Must-try foods** — local dishes you shouldn't miss
- 💡 **Practical tips** — visas, customs, safety, connectivity

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| AI Model | Llama 3.3 70B via Groq API |
| Language | Python |
| Deployment | Streamlit Cloud |

---

## Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Groq API key (free at console.groq.com)
export GROQ_API_KEY=your-key-here   # Mac/Linux
set GROQ_API_KEY=your-key-here      # Windows

# 3. Run
streamlit run app.py
```

---

## Docs

- [Product Requirements Document](specs/PRD.md)
- [AI Specification](specs/AI_SPEC.md)
- [Deployment Specification](specs/DEPLOY_SPEC.md)
