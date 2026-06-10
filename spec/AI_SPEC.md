# WanderAI — AI Specification

**Version:** 1.0  
**Date:** June 2026  
**Team:** Aryan Agarwal (Solo)

---

## 1. Overview

WanderAI uses **Llama 3.3 70B** (via Groq API) as its AI backbone. The intelligence layer is a single, focused function that takes all trip parameters and returns a complete structured itinerary as a JSON object.

```
                    WanderAI AI Layer
┌──────────────────────────────────────────────────┐
│                                                  │
│   Itinerary Generation Agent                     │
│   ─────────────────────────                      │
│   Input:  destination, days, travel_style,       │
│           budget (INR), hotel_pref, travelers,   │
│           travel_month, interests                │
│                                                  │
│   Output: {destination, tagline, weather,        │
│            hotel_rec, days[], budget_breakdown,  │
│            practical_tips, foods, packing_tips}  │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 2. AI Agent — Itinerary Generation

**File:** `app.py`  
**Model:** `llama-3.3-70b-versatile` via Groq API  
**Trigger:** User clicks "✨ Generate My Itinerary"

### 2.1 Responsibility

Takes all user inputs and returns a complete, personalised travel itinerary with day-by-day activities, costs in INR, hotel recommendation, budget breakdown, weather advice, and practical tips.

### 2.2 Output Schema

```json
{
  "destination": "Full destination name",
  "tagline": "One evocative sentence about the destination",
  "weather_in_month": "Weather description and packing advice for the travel month",
  "currency": "Local currency name and approximate INR exchange rate",
  "hotel_recommendation": "Specific hotel or area + price per night in INR",
  "days": [
    {
      "day": 1,
      "theme": "Theme for the day",
      "morning": "Activity with place names and INR costs",
      "afternoon": "Activity with place names and INR costs",
      "evening": "Activity/dinner with INR costs",
      "food_tip": "Restaurant or dish with INR cost",
      "transport": "Transport mode and INR cost"
    }
  ],
  "budget_breakdown": {
    "hotel_total": "Total hotel cost for N nights in INR",
    "food_total": "Total food cost for N days in INR",
    "activities_total": "Total activities/entry fees in INR",
    "transport_local": "Total local transport in INR",
    "total_estimated": "Grand total in INR",
    "budget_note": "Fit assessment vs entered budget + savings tips"
  },
  "practical_tips": ["tip1", "tip2", "tip3", "tip4", "tip5"],
  "must_try_foods": ["food1", "food2", "food3", "food4"],
  "packing_tips": "Key items to pack for the travel month"
}
```

### 2.3 Prompt Design

The prompt is constructed at call time and injects all user parameters:

```
You are an expert travel planner for Indian travellers. Create a detailed,
practical {days}-day travel itinerary for {destination}.

Traveller details:
- Travel style: {travel_style}
- Total budget per person (excluding flights): ₹{budget_per_person} INR
- Per day budget: ₹{per_day_budget} INR
- Hotel preference: {hotel_budget}
- Travelling as: {travelers}
- Travel month: {travel_month}
- Special interests: {interests}

IMPORTANT: All prices and costs MUST be in Indian Rupees (₹ INR).
Convert all local prices to INR.

Return ONLY a valid JSON object... (schema as above)
```

**Prompt engineering decisions:**

| Decision | Reason |
|----------|--------|
| `"ONLY a valid JSON object"` | Prevents the model from adding explanation or markdown fences |
| Per-day budget pre-calculated and injected | Gives the model a concrete daily constraint to work within |
| `"for Indian travellers"` in system role | Anchors the model to INR pricing and Indian travel context |
| `"Convert all local prices to INR"` explicit instruction | Prevents the model from returning prices in local currency |
| Month injected into weather and packing fields | Ensures seasonal relevance without the model guessing |
| Hotel preference with INR ranges in dropdown | Gives the model a concrete budget band to recommend within |

### 2.4 Response Parsing

```python
raw = response.choices[0].message.content.strip()

# Strip markdown fences if model wraps in ```json
if raw.startswith("```"):
    raw = raw.split("```")[1]
    if raw.startswith("json"):
        raw = raw[4:]
raw = raw.strip()

data = json.loads(raw)
```

Code fences are stripped defensively even though the prompt instructs no markdown.

### 2.5 Fallback Behaviour

| Condition | Behaviour |
|-----------|-----------|
| Empty destination | Blocked at UI level — form shows error, no API call made |
| API key missing | `st.error("API error: ...")` shown to user |
| Malformed JSON from model | Error displayed + raw output shown for debugging |
| Network failure | Groq SDK raises exception; caught and displayed as error |

---

## 3. Model Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Model | `llama-3.3-70b-versatile` | Groq-hosted Llama 3.3 70B — free tier |
| Temperature | 0.7 | Allows creative itinerary variety while staying coherent |
| Max tokens | 4000 | Enough for a 14-day itinerary with full breakdown |
| Response format | JSON (prompt-enforced) | No native JSON mode used; prompt + parsing handles it |

---

## 4. Why Groq + Llama 3.3 70B

| Criterion | Decision |
|-----------|----------|
| Cost | Free tier, no credit card required |
| Speed | Groq's LPU hardware returns responses in 3–8 seconds |
| Quality | Llama 3.3 70B is strong at structured JSON generation and travel planning |
| Reliability | No daily quota issues unlike Gemini free tier |

---

## 5. Limitations

| Limitation | Detail |
|------------|--------|
| No real-time data | Prices and hotel availability are AI estimates, not live data |
| INR conversion is approximate | Exchange rates are the model's training knowledge, not live |
| No memory across sessions | Each generation is independent; no history retained |
| Single agent | One LLM call handles everything; no specialist sub-agents |
| No image support | Text-only itinerary; no photos of destinations |
