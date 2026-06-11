# Skills: WanderAI — AI Travel Itinerary Planner

**Feature:** 001-wanderai-itinerary-planner  
**Author:** Aryan Agarwal  
**Date:** June 2026

---

## Overview

Skills are the specific capabilities the AI agent uses to complete the itinerary generation task. Each skill maps to a distinct reasoning or generation ability that the Llama 3.3 70B model applies when processing the user's request.

---

## Skill 1 — Structured JSON Generation

**Used by:** Itinerary Generation Agent  
**Trigger:** Every itinerary request

### Description
The ability to produce a strictly structured JSON object that matches a predefined schema — with no extra text, no markdown fences, and no hallucinated fields. This is the foundational skill that makes the app work, since the entire result display depends on parsing the AI's output as JSON.

### How it's invoked
The prompt explicitly instructs:
```
Return ONLY a valid JSON object with this exact structure — no markdown, no extra text
```
The full schema with field names and types is included in the prompt so the model knows exactly what to produce.

### Validation
```python
data = json.loads(raw.strip())
```
If this fails, a `json.JSONDecodeError` is caught and the raw output is shown to the user for debugging.

---

## Skill 2 — Travel Planning & Domain Knowledge

**Used by:** Itinerary Generation Agent  
**Trigger:** Every itinerary request

### Description
The model's built-in knowledge of global destinations — tourist attractions, local food, transport systems, hotel areas, entry fees, cultural norms, visa requirements, and seasonal weather. This knowledge is applied to generate specific, accurate, and useful itinerary content for any destination.

### Examples of domain knowledge applied
- Knowing Senso-ji Temple is in Asakusa, Tokyo — and that entry is free
- Knowing that October in Japan is mild and requires light layers
- Knowing that the Suica IC card is used for Tokyo metro transport
- Knowing which areas of a city are best for budget vs luxury hotels

### Limitation
Knowledge is from the model's training data (cutoff). Prices, operating hours, and availability may have changed.

---

## Skill 3 — Currency Conversion & INR Pricing

**Used by:** Itinerary Generation Agent  
**Trigger:** Every itinerary request

### Description
The ability to convert all local prices (JPY, EUR, USD, THB, etc.) into Indian Rupees (₹ INR) and present all costs in INR throughout the itinerary. This is a custom skill activated by explicit prompt instruction.

### How it's invoked
The prompt instructs:
```
IMPORTANT: All prices and costs MUST be in Indian Rupees (₹ INR).
Convert all local prices to INR.
```
The model applies approximate exchange rates from its training data to produce INR-denominated costs for every activity, meal, hotel, and transport option.

### Limitation
Exchange rates are approximate and based on training data — not real-time rates.

---

## Skill 4 — Budget-Constrained Planning

**Used by:** Itinerary Generation Agent  
**Trigger:** Every itinerary request

### Description
The ability to generate an itinerary that fits within a specified budget. The model receives both the total budget (`budget_per_person`) and the pre-calculated daily budget (`per_day_budget`), then selects activities, restaurants, hotels, and transport options that are appropriate for that spending level.

### How it's invoked
Both values are injected into the prompt:
```
Total budget per person (excluding flights): ₹{budget_per_person} INR
Per day budget: ₹{per_day_budget} INR
Hotel preference: {hotel_budget}
```
The model then generates a `budget_breakdown` section that compares estimated spend against the entered budget and notes whether it fits.

---

## Skill 5 — Seasonal Travel Advice

**Used by:** Itinerary Generation Agent  
**Trigger:** Every itinerary request

### Description
The ability to tailor advice based on the month of travel — including weather descriptions, packing recommendations, and seasonal activity suggestions. A trip to Bali in July (dry season) generates different advice than the same trip in January (wet season).

### How it's invoked
Travel month is injected into the prompt and specifically referenced in two output fields:
- `weather_in_month` — weather description and what to pack
- `packing_tips` — specific items to bring for that month

---

## Skill 6 — Personalisation by Travel Style & Group

**Used by:** Itinerary Generation Agent  
**Trigger:** Every itinerary request

### Description
The ability to customise the itinerary based on the traveller's style (cultural, adventure, food & nightlife, luxury, budget backpacker, balanced) and group type (solo, couple, family, friends). A couple on a luxury trip to Paris gets a different plan than a solo budget backpacker going to the same city.

### How it's invoked
Both parameters are injected into the prompt:
```
Travel style: {travel_style}
Travelling as: {travelers}
Special interests: {interests}
```
The model adjusts venue types, activity pace, and recommendations accordingly.

---

## Skill Summary

| Skill | Model Capability | Activated By |
|-------|-----------------|-------------|
| Structured JSON Generation | Instruction following + schema adherence | Prompt schema + "ONLY JSON" instruction |
| Travel Planning Knowledge | Built-in world knowledge | Destination + days in prompt |
| Currency Conversion to INR | Arithmetic + knowledge | "All prices MUST be in ₹ INR" instruction |
| Budget-Constrained Planning | Constraint satisfaction | budget_per_person + per_day_budget injection |
| Seasonal Travel Advice | Temporal + geographic knowledge | travel_month injection |
| Personalisation | Context adaptation | travel_style + travelers + interests injection |
