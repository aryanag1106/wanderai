# Spec: WanderAI — AI Travel Itinerary Planner

**Feature:** 001-wanderai-itinerary-planner  
**Author:** Aryan Agarwal  
**Date:** June 2026  
**Status:** Complete  
**Branch:** main

---

## Overview

WanderAI is a Streamlit web application that generates personalised, AI-powered travel itineraries for Indian travellers. Users input their destination, budget in ₹ INR, travel month, hotel preference, travel style, and group type — and receive a complete day-by-day itinerary with costs in rupees, a hotel recommendation, weather advice, budget breakdown, food tips, and practical travel tips.

---

## Problem

Planning a trip requires visiting 10+ websites for itineraries, hotel costs, weather, currency conversion, and food recommendations. Generic travel blogs give the same advice to everyone regardless of budget, group type, or season. Indian travellers are especially underserved — prices are always in USD or local currency, requiring manual conversion.

---

## Goals

- Generate a complete, personalised day-by-day itinerary in under 15 seconds
- Show all prices in ₹ INR — no manual currency conversion needed
- Tailor the plan to budget, travel style, group type, and month of travel
- Provide a full budget breakdown so travellers can plan finances before booking
- Recommend specific hotels matched to the user's preference and budget

---

## Non-Goals (Out of Scope)

- User authentication or saved itineraries
- Live hotel pricing via booking APIs
- Flight cost estimation or booking
- Map view with pinned locations
- PDF export
- Mobile-native app

---

## User Stories

### US1 — Generate Itinerary
**As an** Indian traveller,  
**I want to** enter my destination, budget in ₹ INR, travel month, hotel preference, and preferences,  
**So that** I get a complete personalised day-by-day trip plan without hours of research.

**Acceptance Criteria:**
- [ ] User can enter destination as free text
- [ ] User can set number of days via slider (1–14)
- [ ] User can enter budget per person in ₹ INR (excluding flights)
- [ ] User can select hotel preference with INR price ranges
- [ ] User can select travel month from all 12 months
- [ ] User can select travel style, group type, and add optional interests
- [ ] Clicking "Generate My Itinerary" triggers the AI call
- [ ] A spinner shows while the API call is in progress
- [ ] If destination is empty, show an error and block the API call

### US2 — View Day-by-Day Plan
**As an** Indian traveller,  
**I want to** see a card for each day with morning, afternoon, and evening activities,  
**So that** I know exactly what to do at each part of the day.

**Acceptance Criteria:**
- [ ] One styled card rendered per day
- [ ] Each card shows: theme, morning activity, afternoon activity, evening activity
- [ ] Each card shows a food tip and local transport tip
- [ ] All mentioned costs are in ₹ INR
- [ ] Specific place names are included, not generic descriptions

### US3 — View Budget Breakdown
**As an** Indian traveller,  
**I want to** see a breakdown of how my budget will be spent,  
**So that** I can plan my finances before booking anything.

**Acceptance Criteria:**
- [ ] Budget breakdown shows hotel total, food total, activities total, local transport total
- [ ] Grand total shown in ₹ INR
- [ ] A note says whether the plan fits within the entered budget
- [ ] Breakdown is shown in a visually distinct green box

### US4 — View Weather & Hotel Info
**As an** Indian traveller,  
**I want to** know the weather for my travel month and a hotel recommendation,  
**So that** I know what to pack and where to stay.

**Acceptance Criteria:**
- [ ] Weather info shown for the selected month with packing advice
- [ ] Hotel recommendation includes a specific name or area and INR price per night
- [ ] Weather shown in a blue info box
- [ ] Hotel shown in a green success box

### US5 — View Food & Practical Tips
**As an** Indian traveller,  
**I want to** see must-try foods and practical tips for the destination,  
**So that** I don't miss local experiences and I'm prepared for common challenges.

**Acceptance Criteria:**
- [ ] Must-try foods displayed as styled badge pills
- [ ] At least 5 practical tips shown in an orange tips box
- [ ] Packing tips shown below the tips box
- [ ] Currency exchange rate shown at the bottom

---

## Constraints

- All costs must be in ₹ INR — no USD or local currency shown
- App must work on Streamlit Cloud free tier
- Only the Groq API is required — no other external API keys
- No user data is stored — fully stateless
- API key must never be committed to git

---

## Tech Stack

| Layer | Choice | Reason |
|-------|--------|--------|
| UI Framework | Streamlit | Rapid prototyping, Python-native, free deployment |
| AI Model | Llama 3.3 70B (Groq) | Free, fast, no credit card, strong JSON generation |
| Language | Python 3.10+ | Team familiarity, rich ecosystem |
| Deployment | Streamlit Cloud | Free hosting, GitHub integration, secrets management |
