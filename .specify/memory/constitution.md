# WanderAI — Project Constitution

## Mission
Build an AI-powered travel itinerary planner for Indian travellers that generates personalised, budget-aware, INR-priced trip plans in seconds.

## Core Values
- **Indian-first:** All prices in INR. Designed for Indian budgets and travel needs.
- **Accessible:** Works with free AI (Groq) and local AI (Ollama/LM Studio).
- **Private:** Local inference option ensures user data never leaves their machine.
- **Multilingual:** Supports English, Hindi, and Telugu.
- **Open source:** Licensed under AGPLv3.

## Architecture Principles
- Single-file Streamlit app for simplicity
- Stateless: no database, no user accounts
- All AI via prompt engineering, no fine-tuning
- JSON-structured AI output for reliable parsing

## Tech Stack
- Frontend: Streamlit
- AI Cloud: Llama 3.3 70B via Groq API (BYOK)
- AI Local: Ollama / LM Studio
- Language: Python 3.10+
- Deployment: Streamlit Cloud

## Non-Goals
- No user authentication
- No live hotel/flight pricing APIs
- No mobile native app
- No data collection or analytics
