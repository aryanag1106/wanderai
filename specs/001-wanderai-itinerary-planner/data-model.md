# Data Model: WanderAI AI Response Schema

**Feature:** 001-wanderai-itinerary-planner  
**Date:** June 2026

---

## AI Output Schema

The Groq/Llama model is instructed to return exactly this JSON structure:

```json
{
  "destination": "string — full destination name e.g. Tokyo, Japan",
  "tagline": "string — one evocative sentence about the destination",
  "weather_in_month": "string — weather description for travel month + packing advice",
  "currency": "string — local currency name and approximate INR exchange rate",
  "hotel_recommendation": "string — specific hotel or area + estimated price per night in INR",
  "days": [
    {
      "day": "integer — day number starting from 1",
      "theme": "string — theme for the day e.g. Ancient Temples & History",
      "morning": "string — detailed morning activity with place names and INR costs",
      "afternoon": "string — detailed afternoon activity with place names and INR costs",
      "evening": "string — evening activity and dinner recommendation with INR costs",
      "food_tip": "string — must-try food or restaurant with approximate INR cost",
      "transport": "string — how to get around that day with INR cost"
    }
  ],
  "budget_breakdown": {
    "hotel_total": "string — total hotel cost for all nights in INR",
    "food_total": "string — total food cost for all days in INR",
    "activities_total": "string — total activities and entry fees in INR",
    "transport_local": "string — total local transport for all days in INR",
    "total_estimated": "string — grand total in INR",
    "budget_note": "string — whether plan fits the entered budget + savings tips"
  },
  "practical_tips": ["string", "string", "string", "string", "string"],
  "must_try_foods": ["string", "string", "string", "string"],
  "packing_tips": "string — key items to pack for the travel month"
}
```

---

## Field Notes

| Field | Notes |
|-------|-------|
| `days` | Array length equals the number of days the user selected |
| All cost fields | Must be in ₹ INR — model instructed to convert local prices |
| `practical_tips` | Minimum 5 tips covering visas, safety, connectivity, customs |
| `must_try_foods` | Minimum 4 dishes or food experiences |
| `budget_breakdown` | Covers the full trip duration, not per day |

---

## Parsing

```python
# Strip markdown fences if present
if raw.startswith("```"):
    raw = raw.split("```")[1]
    if raw.startswith("json"):
        raw = raw[4:]

# Parse to Python dict
data = json.loads(raw.strip())

# Safe access pattern used throughout
data.get("destination", fallback_value)
```
