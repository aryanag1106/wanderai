# Agents: WanderAI — AI Travel Itinerary Planner

**Feature:** 001-wanderai-itinerary-planner  
**Author:** Aryan Agarwal  
**Date:** June 2026

---

## Overview

WanderAI uses a single AI agent built on **Llama 3.3 70B** via the Groq API. The agent is stateless — it receives all context in one prompt and returns a complete structured response. There is no memory, no multi-turn conversation, and no tool use.

---

## Agent 1 — Itinerary Generation Agent

**Name:** `itinerary_agent`  
**Model:** `llama-3.3-70b-versatile` (Groq)  
**Trigger:** User clicks "✨ Generate My Itinerary"  
**Type:** Single-turn, stateless  

### Responsibility

Takes all user inputs (destination, days, budget in ₹ INR, hotel preference, travel month, travel style, group type, interests) and returns a complete personalised travel itinerary as a structured JSON object.

### Input

```python
{
  "destination": str,         # e.g. "Tokyo, Japan"
  "days": int,                # e.g. 5
  "budget_per_person": int,   # e.g. 50000 (₹ INR, excluding flights)
  "per_day_budget": int,      # pre-calculated: budget // days
  "hotel_budget": str,        # e.g. "Mid-range (3-star ₹1500–₹4000/night)"
  "travel_month": str,        # e.g. "October"
  "travel_style": str,        # e.g. "Cultural & historical"
  "travelers": str,           # e.g. "Couple"
  "interests": str            # e.g. "anime, street food" (optional)
}
```

### Output

```json
{
  "destination": "Tokyo, Japan",
  "tagline": "A city where ancient temples meet neon-lit streets",
  "weather_in_month": "October is cool and pleasant (15–22°C). Pack light layers...",
  "currency": "Japanese Yen (JPY). 1 JPY ≈ ₹0.55. ₹1000 ≈ 1800 JPY",
  "hotel_recommendation": "Shinjuku area — APA Hotel Shinjuku, approx ₹3500/night",
  "days": [
    {
      "day": 1,
      "theme": "Arrival & Old Tokyo",
      "morning": "Visit Senso-ji Temple in Asakusa. Entry free. Rickshaw ride ₹800.",
      "afternoon": "Explore Nakamise shopping street. Budget ₹1500 for snacks and souvenirs.",
      "evening": "Dinner at Ichiran Ramen, Shinjuku. Cost approx ₹900 per person.",
      "food_tip": "Try Tempura at Daikokuya — a 100-year-old institution. ₹1200.",
      "transport": "IC Card (Suica) for metro — approx ₹600/day in fares."
    }
  ],
  "budget_breakdown": {
    "hotel_total": "₹17,500 (5 nights × ₹3,500)",
    "food_total": "₹12,500 (₹2,500/day × 5 days)",
    "activities_total": "₹8,000 (entry fees, experiences)",
    "transport_local": "₹3,000 (metro IC card for 5 days)",
    "total_estimated": "₹41,000",
    "budget_note": "Fits within your ₹50,000 budget with ₹9,000 buffer for shopping."
  },
  "practical_tips": ["tip1", "tip2", "tip3", "tip4", "tip5"],
  "must_try_foods": ["Ramen", "Sushi", "Takoyaki", "Matcha desserts"],
  "packing_tips": "Pack light layers for October. Comfortable walking shoes essential."
}
```

### Prompt Strategy

| Technique | Implementation |
|-----------|---------------|
| Role assignment | `"You are an expert travel planner for Indian travellers"` |
| JSON-only output | `"Return ONLY a valid JSON object — no markdown, no extra text"` |
| Schema injection | Full JSON schema with field names and descriptions in the prompt |
| Currency anchoring | `"All prices MUST be in Indian Rupees (₹ INR). Convert all local prices to INR."` |
| Budget grounding | Pre-calculated `per_day_budget` injected so model has concrete daily constraint |
| Seasonal context | `travel_month` injected to generate relevant weather and packing advice |

### Configuration

| Parameter | Value | Reason |
|-----------|-------|--------|
| Model | `llama-3.3-70b-versatile` | Best free model for structured JSON generation |
| Temperature | `0.7` | Creative variety in itineraries while staying factually coherent |
| Max tokens | `4000` | Handles full 14-day itinerary with all sections |
| API provider | Groq | Free tier, no daily quota issues, LPU hardware for fast inference |

### Error Handling

| Error | Handling |
|-------|---------|
| Empty destination | Blocked at UI — `st.stop()` before API call |
| Missing API key | Caught in try/except → `st.error("API error: ...")` |
| Malformed JSON | `json.JSONDecodeError` caught → error shown + raw output displayed |
| Network failure | Groq SDK exception caught → user-friendly error message |

### Limitations

| Limitation | Detail |
|------------|--------|
| No real-time data | Hotel prices and costs are model estimates, not live data |
| INR conversion approximate | Based on model training data, not live exchange rates |
| No memory | Each generation is fully independent — no history retained |
| Single agent | One LLM call handles all tasks — no specialist sub-agents |
| No image support | Text-only output — no photos of destinations or hotels |

---

## Future Agents (Planned)

### Agent 2 — Itinerary Refinement Agent
**Trigger:** User asks to modify a generated itinerary  
**Input:** Existing itinerary JSON + user change request  
**Output:** Updated itinerary JSON  
**Status:** Not implemented (post-hackathon)

### Agent 3 — Budget Optimiser Agent
**Trigger:** Total estimate exceeds user's budget  
**Input:** Itinerary JSON + budget gap  
**Output:** Suggestions to reduce costs while maintaining experience quality  
**Status:** Not implemented (post-hackathon)

### Agent 4 — Flight Cost Estimator Agent
**Trigger:** User requests flight cost addition  
**Input:** Origin city (India) + destination + travel month  
**Output:** Approximate round-trip flight cost in ₹ INR  
**Status:** Not implemented (post-hackathon)
