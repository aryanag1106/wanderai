# WanderAI — User Manual

## What is WanderAI?
WanderAI is an AI-powered travel itinerary planner built for Indian travellers. Enter your destination, budget in ₹ INR, travel month, and preferences — get a complete day-by-day trip plan in seconds.

## Getting Started

### Step 1 — Choose your AI Backend (sidebar)
- **☁️ Groq API (Cloud):** Paste your free Groq API key from [console.groq.com](https://console.groq.com)
- **🖥️ Ollama (Local):** Run AI on your own machine — no key needed

### Step 2 — Fill in your trip details
| Field | Description |
|-------|-------------|
| 🌍 Destination | Where you want to go (e.g. Tokyo, Japan) |
| 📅 Number of days | Slide to select 1–14 days |
| 🗓️ Month of travel | Select your travel month for weather info |
| 💰 Budget per person (₹) | Your total budget excluding flights, in INR |
| 🏨 Hotel preference | Budget hostel to 5-star luxury |
| 🎒 Travel style | Cultural, Adventure, Food, Luxury, etc. |
| 👥 Travelling as | Solo, Couple, Family, or Friends |
| 💡 Interests | Optional: anime, hiking, street food, etc. |

### Step 3 — Generate
Click **✨ Generate My Itinerary** and wait ~10 seconds.

## Reading Your Itinerary

### Summary Row
Shows your key trip details at a glance — days, budget, month, group type.

### Weather Info (blue box)
What weather to expect in your travel month and what to pack.

### Hotel Recommendation (green box)
A specific hotel or area recommendation with estimated INR price per night.

### Must-Try Foods
Local dishes shown as badge pills — don't miss these!

### Day Cards
One card per day showing:
- 🌅 Morning activity with place names and INR costs
- ☀️ Afternoon activity with place names and INR costs
- 🌙 Evening activity / dinner recommendation
- 🍽️ Daily food tip with cost
- 🚌 How to get around with cost

### Budget Breakdown (green box)
Full breakdown of estimated spend:
- Hotel total for all nights
- Food total for all days
- Activities and entry fees
- Local transport
- Grand total vs your budget

### Practical Tips (orange box)
5 tips covering visas, safety, connectivity, customs, and more.

## Language Support
Select your preferred language at the top:
- 🇬🇧 English
- 🇮🇳 हिन्दी (Hindi)
- 🇮🇳 తెలుగు (Telugu)

The AI responds in your selected language.

## Leaving a Review
Scroll to the bottom → fill in your name, review, star rating, and destination → click **Submit Review**.

## AI Backend Setup

### Groq API (Cloud) — Free
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up → API Keys → Create Key
3. Paste the key in the sidebar

### Ollama (Local)
1. Install from [ollama.com](https://ollama.com)
2. Run: `ollama pull phi3`
3. Run: `ollama serve`
4. Select Ollama in sidebar → URL: `http://localhost:11434`

### LM Studio (Local, easier)
1. Install from [lmstudio.ai](https://lmstudio.ai)
2. Download phi-3-mini model
3. Start Local Server
4. Select Ollama → LM Studio in sidebar

## Troubleshooting

| Problem | Solution |
|---------|---------|
| API error | Check your Groq key is correct |
| Ollama can't connect | Make sure `ollama serve` is running |
| JSON parse error | Click Generate again |
| Slow response | Switch to `llama-3.1-8b-instant` model |
