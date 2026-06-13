# AGENTS.md — WanderAI AI Agents

## Overview
WanderAI uses a single AI agent for itinerary generation, with support for multiple AI backends.

## Itinerary Generation Agent

**Model:** Llama 3.3 70B (via Groq) or local model (via Ollama/LM Studio)  
**Type:** Single-turn, stateless  
**Trigger:** User clicks "Generate My Itinerary"

### What it does
Takes all user inputs and returns a complete personalised travel itinerary as structured JSON — including day-by-day activities, hotel recommendation, budget breakdown, weather advice, food tips, and practical tips. All costs in ₹ INR.

### Supported Backends
| Backend | Model | Type | Cost |
|---------|-------|------|------|
| Groq API | llama-3.3-70b-versatile | Cloud | Free |
| Groq API | llama-3.1-8b-instant | Cloud | Free |
| Groq API | mixtral-8x7b-32768 | Cloud | Free |
| Ollama | phi3, mistral, tinyllama | Local | Free |
| LM Studio | phi-3-mini, gemma-2b | Local | Free |

### Input Parameters
- destination, days, budget_per_person (₹ INR), hotel_preference
- travel_month, travel_style, travelers, interests, language

### Output Schema
Returns JSON with: destination, tagline, weather_in_month, currency,
hotel_recommendation, days[], budget_breakdown, practical_tips,
must_try_foods, packing_tips

### Prompt Engineering
- Role: "expert travel planner for Indian travellers"
- All prices instructed to be in ₹ INR
- JSON-only output enforced
- Language injection for multilingual support
- Per-day budget pre-calculated before prompt

### Error Handling
- Empty destination → blocked at UI level
- Missing API key → clear error message shown
- Malformed JSON → error + raw output shown
- Network failure → caught exception displayed

## Future Agents (Planned)
- **Refinement Agent:** Modify existing itinerary based on user feedback
- **Budget Optimiser:** Suggest cost reductions when over budget
- **Flight Estimator:** Add approximate flight costs from Indian cities
