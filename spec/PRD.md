# WanderAI — Product Requirements Document (PRD)

**Version:** 1.0  
**Date:** June 2026  
**Team:** Aryan Agarwal (Solo)  
**Status:** Hackathon Submission

---

## 1. Problem Statement

Planning a trip is time-consuming and overwhelming. Travellers — especially from India — face three compounding problems:

1. **Information Overload:** Planning requires visiting dozens of websites for itineraries, hotel costs, food tips, weather, local transport, and currency — all in different places.
2. **No Personalisation:** Generic travel blogs give the same itinerary to everyone, regardless of budget, travel style, group type, or month of travel.
3. **Currency Confusion:** Most travel tools show prices in USD or local currency, which means Indian travellers have to manually convert everything to rupees while budgeting.

---

## 2. Vision

> **"Your trip, planned in seconds"** — a personalised AI travel planner that generates a complete, day-by-day itinerary tailored to your budget in ₹ INR, your travel month, your group, and your interests — all in one click.

---

## 3. Goals

### Primary Goals (Hackathon Scope)

- Let users input destination, travel month, budget in ₹ INR, hotel preference, travel style, group type, and interests
- Generate a complete day-by-day itinerary using an AI language model
- Show morning, afternoon, and evening activities for each day with specific places and INR costs
- Display a full budget breakdown — hotel, food, activities, transport — in ₹ INR
- Show weather advice for the travel month and packing tips
- Recommend a specific hotel matching the user's budget

### Secondary Goals (Post-Hackathon)

- Save and share itineraries as PDF
- User login to save past itineraries
- Integrate live hotel pricing via APIs
- Add a map view with pinned attractions
- Offline support for saved itineraries

---

## 4. Users

### Indian Traveller (Primary User)

**Who they are:** Individuals, couples, families, or friend groups from India planning domestic or international trips.

**Goals:**
- Get a full, ready-to-use trip plan without hours of research
- Understand the total cost in rupees before booking
- Know what weather to expect and what to pack

**Pain points:**
- All travel resources show prices in USD or local currency — not INR
- Generic itineraries don't account for their budget or travel style
- Have to visit 10+ websites to get all the information they need

---

## 5. User Stories

| ID | As a... | I want to... | So that... |
|----|---------|--------------|------------|
| U-01 | Traveller | Enter my destination and number of days | I can get a custom itinerary for my trip |
| U-02 | Traveller | Enter my budget in ₹ INR (excluding flights) | I get recommendations that fit what I can actually spend |
| U-03 | Traveller | Select my hotel preference | I get hotel suggestions matching my comfort level |
| U-04 | Traveller | Select the month I'm travelling | I know what weather to expect and what to pack |
| U-05 | Traveller | Select my travel style (cultural, adventure, food, etc.) | The itinerary matches what I enjoy |
| U-06 | Traveller | See a day-by-day plan with morning/afternoon/evening | I know exactly what to do each day |
| U-07 | Traveller | See all costs in ₹ INR | I don't have to convert currencies manually |
| U-08 | Traveller | See a budget breakdown at the end | I know how my money will be spent across hotel, food, activities |
| U-09 | Traveller | See must-try foods at the destination | I don't miss out on the best local food |
| U-10 | Traveller | See practical travel tips | I'm prepared for common challenges at the destination |

---

## 6. Features

### 6.1 Trip Input Form

- **Destination** — free-text input (e.g. "Tokyo, Japan")
- **Number of days** — slider from 1 to 14
- **Travel style** — dropdown: Balanced, Cultural, Adventure, Food & nightlife, Luxury, Budget backpacker
- **Month of travel** — dropdown of all 12 months
- **Budget per person in ₹ INR** — number input excluding flights (min ₹1,000, max ₹10,00,000)
- **Hotel preference** — dropdown: Budget hostel, Mid-range 3-star, Comfortable 4-star, Luxury 5-star (with INR price ranges)
- **Travelling as** — dropdown: Solo, Couple, Family with kids, Group of friends
- **Special interests** — optional free-text (e.g. "anime, street food, hiking")

### 6.2 AI-Generated Itinerary

- **Day-by-day cards** — one card per day with:
  - Theme for the day (e.g. "Ancient Temples & History")
  - Morning activity with specific places and INR costs
  - Afternoon activity with specific places and INR costs
  - Evening activity / dinner recommendation with INR costs
  - Daily food tip with restaurant name and cost in INR
  - Local transport tip with cost in INR
- **Weather info** — what to expect in the selected month and what to pack
- **Hotel recommendation** — specific hotel or area matching the budget, with per-night cost in INR
- **Must-try foods** — displayed as badges
- **Budget breakdown** — hotel total, food total, activities total, local transport total, grand total — all in ₹ INR, with a note on whether it fits the entered budget
- **Practical tips** — 5 tips covering visas, customs, safety, connectivity, etc.
- **Currency note** — local currency and INR exchange rate

### 6.3 UI / UX

- Dark teal gradient hero banner with app name and tagline
- Two-column responsive input form
- Styled day cards with left accent border
- Colour-coded info boxes (weather = blue, hotel = green, budget = green, tips = orange)
- Food badges with pill styling
- Summary metric row (days, budget, month, group type)

---

## 7. Out of Scope (v1.0)

- User authentication / saved itineraries
- Live hotel pricing API integration
- Flight cost estimation
- Map view with pinned locations
- PDF export
- Multi-language support

---

## 8. Success Metrics

| Metric | Target (Demo) |
|--------|--------------|
| Itinerary generation time | < 15 seconds |
| All costs shown in ₹ INR | 100% of outputs |
| Day-by-day plan for N days | All N days generated |
| Budget breakdown included | Every itinerary |
| App loads and runs without errors | Zero crashes in demo |

---

## 9. Constraints

- **Budget:** Zero cost — free-tier Groq API (Llama 3.3 70B)
- **Timeline:** Single hackathon sprint (1 person, 1 day)
- **Team size:** 1 member
- **Deployment:** Streamlit Cloud (free tier)
- **Storage:** No database — stateless, session-based only
