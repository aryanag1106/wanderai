import streamlit as st
from groq import Groq
import json
import os

st.set_page_config(
    page_title="WanderAI – Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.hero {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    border-radius: 20px;
    padding: 3rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    color: #f0e6d3;
    margin: 0;
    letter-spacing: -1px;
}
.hero p {
    color: #a8c5d6;
    font-size: 1.1rem;
    margin-top: 0.5rem;
    font-weight: 300;
}
.hero .emoji { font-size: 2.5rem; display: block; margin-bottom: 0.5rem; }

.day-card {
    background: #ffffff;
    border: 1px solid #e8e0d5;
    border-left: 5px solid #2c5364;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.day-card h3 {
    font-family: 'Playfair Display', serif;
    color: #2c5364;
    font-size: 1.3rem;
    margin-top: 0;
    margin-bottom: 0.5rem;
}
.day-card ul { margin: 0.5rem 0; padding-left: 1.2rem; }
.day-card li { margin-bottom: 0.4rem; color: #444; line-height: 1.6; }

.tip-box {
    background: #fff8f0;
    border: 1px solid #f0d9b5;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 1.5rem;
}
.tip-box strong { color: #b07c3f; }

.budget-box {
    background: #f0faf4;
    border: 1px solid #b7e4c7;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-top: 1.5rem;
}
.budget-box strong { color: #1a7f4b; }
.budget-box ul { margin: 0.5rem 0; padding-left: 1.2rem; }
.budget-box li { margin-bottom: 0.3rem; color: #333; }

.badge {
    display: inline-block;
    background: #eaf4fb;
    color: #2c5364;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 2px;
    letter-spacing: 0.3px;
}

.stButton > button {
    background: linear-gradient(135deg, #2c5364, #203a43) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    width: 100%;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.88; }

.meta-row {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <span class="emoji">✈️</span>
  <h1>WanderAI</h1>
  <p>Your AI-powered travel itinerary planner — just tell it where you want to go.</p>
</div>
""", unsafe_allow_html=True)

with st.form("planner_form"):
    col1, col2 = st.columns(2)
    with col1:
        destination = st.text_input("🌍 Destination", placeholder="e.g. Tokyo, Japan")
        days = st.slider("📅 Number of days", 1, 14, 5)
        travel_style = st.selectbox("🎒 Travel style",
            ["Balanced (mix of everything)",
             "Cultural & historical",
             "Adventure & outdoors",
             "Food & nightlife",
             "Luxury & relaxation",
             "Budget backpacker"])
        travel_month = st.selectbox("🗓️ Month of travel",
            ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"])

    with col2:
        budget_per_person = st.number_input(
            "💰 Budget per person (₹) — excluding flights",
            min_value=1000,
            max_value=1000000,
            value=30000,
            step=1000,
            help="Total trip budget per person in Indian Rupees, not including flight tickets"
        )
        hotel_budget = st.selectbox("🏨 Hotel preference",
            ["Budget (Hostel/Guesthouse ₹500–₹1500/night)",
             "Mid-range (3-star ₹1500–₹4000/night)",
             "Comfortable (4-star ₹4000–₹8000/night)",
             "Luxury (5-star ₹8000+/night)"])
        travelers = st.selectbox("👥 Travelling as",
            ["Solo", "Couple", "Family with kids", "Group of friends"])
        interests = st.text_input("💡 Special interests (optional)",
            placeholder="e.g. anime, street food, hiking, museums")

    submitted = st.form_submit_button("✨ Generate My Itinerary")

if submitted:
    if not destination.strip():
        st.error("Please enter a destination first.")
        st.stop()

    # Calculate rough per day budget
    per_day_budget = budget_per_person // days

    with st.spinner("Planning your perfect trip…"):

        prompt = f"""You are an expert travel planner for Indian travellers. Create a detailed, practical {days}-day travel itinerary for {destination}.

Traveller details:
- Travel style: {travel_style}
- Total budget per person (excluding flights): ₹{budget_per_person:,} INR
- Per day budget: ₹{per_day_budget:,} INR
- Hotel preference: {hotel_budget}
- Travelling as: {travelers}
- Travel month: {travel_month}
- Special interests: {interests if interests else 'none specified'}

IMPORTANT: All prices and costs MUST be in Indian Rupees (₹ INR). Convert all local prices to INR.

Return ONLY a valid JSON object with this exact structure — no markdown, no extra text:
{{
  "destination": "Full destination name",
  "tagline": "One evocative sentence about this destination",
  "weather_in_month": "What weather to expect in {travel_month} and what to pack",
  "currency": "Local currency name and approximate exchange rate to INR",
  "hotel_recommendation": "Specific recommended hotel or area to stay matching the budget, with estimated price per night in INR",
  "days": [
    {{
      "day": 1,
      "theme": "Theme for the day",
      "morning": "Detailed morning activity with specific places, entry fees in INR",
      "afternoon": "Detailed afternoon activity with specific places, costs in INR",
      "evening": "Detailed evening activity / dinner recommendation with cost in INR",
      "food_tip": "Must-try food or restaurant today with approximate cost in INR",
      "transport": "How to get around today with cost in INR"
    }}
  ],
  "budget_breakdown": {{
    "hotel_total": "Estimated hotel cost for all {days} nights in INR",
    "food_total": "Estimated food cost for all {days} days in INR",
    "activities_total": "Estimated activities/entry fees for all {days} days in INR",
    "transport_local": "Estimated local transport for all {days} days in INR",
    "total_estimated": "Total estimated spend for {days} days in INR",
    "budget_note": "Note on whether this fits the ₹{budget_per_person:,} budget and any savings tips"
  }},
  "practical_tips": ["tip1", "tip2", "tip3", "tip4", "tip5"],
  "must_try_foods": ["food1", "food2", "food3", "food4"],
  "packing_tips": "Key items to pack for {travel_month} travel to this destination"
}}"""

        try:
            api_key = os.environ.get("GROQ_API_KEY", "")
            try:
                api_key = st.secrets.get("GROQ_API_KEY", api_key)
            except Exception:
                pass

            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=4000,
            )
            raw = response.choices[0].message.content.strip()
        except Exception as e:
            st.error(f"API error: {e}")
            st.stop()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            st.error("Something went wrong parsing the itinerary. Please try again.")
            st.code(raw)
            st.stop()

    # ── Display ───────────────────────────────────────────────────────────────
    st.markdown(f"## 🗺️ {data.get('destination', destination)}")
    st.markdown(f"*{data.get('tagline', '')}*")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("📅 Days", days)
    m2.metric("💰 Budget", f"₹{budget_per_person:,}")
    m3.metric("📅 Travelling in", travel_month)
    m4.metric("👥 Group", travelers)

    st.divider()

    # Weather info
    weather = data.get("weather_in_month", "")
    if weather:
        st.info(f"🌤️ **Weather in {travel_month}:** {weather}")

    # Hotel recommendation
    hotel = data.get("hotel_recommendation", "")
    if hotel:
        st.success(f"🏨 **Hotel Recommendation:** {hotel}")

    # Must-try foods
    foods = data.get("must_try_foods", [])
    if foods:
        st.markdown("**🍜 Must-try foods:**")
        food_html = " ".join([f'<span class="badge">{f}</span>' for f in foods])
        st.markdown(f'<div class="meta-row">{food_html}</div>', unsafe_allow_html=True)

    st.markdown("### 📋 Your Day-by-Day Itinerary")

    for day in data.get("days", []):
        card = f"""
<div class="day-card">
  <h3>Day {day['day']} — {day.get('theme', '')}</h3>
  <ul>
    <li><strong>🌅 Morning:</strong> {day.get('morning', '')}</li>
    <li><strong>☀️ Afternoon:</strong> {day.get('afternoon', '')}</li>
    <li><strong>🌙 Evening:</strong> {day.get('evening', '')}</li>
  </ul>
  <p style="margin-bottom:4px">🍽️ <em>Food tip: {day.get('food_tip', '')}</em></p>
  <p style="margin:0">🚌 <em>Getting around: {day.get('transport', '')}</em></p>
</div>"""
        st.markdown(card, unsafe_allow_html=True)

    # Budget breakdown
    budget_data = data.get("budget_breakdown", {})
    if budget_data:
        budget_items = "".join([
            f"<li>🏨 <strong>Hotel ({days} nights):</strong> {budget_data.get('hotel_total', '')}</li>",
            f"<li>🍽️ <strong>Food ({days} days):</strong> {budget_data.get('food_total', '')}</li>",
            f"<li>🎯 <strong>Activities & Entry fees:</strong> {budget_data.get('activities_total', '')}</li>",
            f"<li>🚌 <strong>Local transport:</strong> {budget_data.get('transport_local', '')}</li>",
            f"<li>💰 <strong>Total estimated:</strong> {budget_data.get('total_estimated', '')}</li>",
        ])
        st.markdown(f"""
<div class="budget-box">
  <strong>💸 Budget Breakdown (per person, excluding flights)</strong>
  <ul style="margin-top:0.5rem">{budget_items}</ul>
  <p style="margin:0.5rem 0 0; font-size:0.9rem; color:#555">📝 {budget_data.get('budget_note', '')}</p>
</div>
""", unsafe_allow_html=True)

    # Practical tips
    tips = data.get("practical_tips", [])
    if tips:
        tips_html = "".join([f"<li>{t}</li>" for t in tips])
        st.markdown(f"""
<div class="tip-box">
  <strong>💡 Practical Tips</strong>
  <ul style="margin-top:0.5rem; padding-left:1.2rem">{tips_html}</ul>
</div>
""", unsafe_allow_html=True)

    packing = data.get("packing_tips", "")
    if packing:
        st.markdown(f"🎒 **Packing tips for {travel_month}:** {packing}")

    st.markdown(f"**💱 Currency:** {data.get('currency', '')}")
    st.success("✅ Itinerary ready! Scroll up to review your full trip plan.")
