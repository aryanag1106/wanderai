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
    with col2:
        budget = st.selectbox("💰 Budget",
            ["Budget (< $50/day)",
             "Mid-range ($50–$150/day)",
             "Comfortable ($150–$300/day)",
             "Luxury ($300+/day)"])
        travelers = st.selectbox("👥 Travelling as",
            ["Solo", "Couple", "Family with kids", "Group of friends"])
        interests = st.text_input("💡 Special interests (optional)",
            placeholder="e.g. anime, street food, hiking, museums")

    submitted = st.form_submit_button("✨ Generate My Itinerary")

if submitted:
    if not destination.strip():
        st.error("Please enter a destination first.")
        st.stop()

    with st.spinner("Planning your perfect trip…"):

        prompt = f"""You are an expert travel planner. Create a detailed, practical {days}-day travel itinerary for {destination}.

Traveller details:
- Travel style: {travel_style}
- Budget: {budget}
- Travelling as: {travelers}
- Special interests: {interests if interests else 'none specified'}

Return ONLY a valid JSON object with this exact structure — no markdown, no extra text:
{{
  "destination": "Full destination name",
  "tagline": "One evocative sentence about this destination",
  "best_time": "Best time of year to visit",
  "currency": "Local currency and rough exchange note",
  "days": [
    {{
      "day": 1,
      "theme": "Theme for the day",
      "morning": "Detailed morning activity with specific places and tips",
      "afternoon": "Detailed afternoon activity with specific places and tips",
      "evening": "Detailed evening activity / dinner recommendation",
      "food_tip": "Must-try food or restaurant today",
      "transport": "How to get around today"
    }}
  ],
  "practical_tips": ["tip1", "tip2", "tip3", "tip4", "tip5"],
  "must_try_foods": ["food1", "food2", "food3", "food4"],
  "estimated_daily_cost": "Rough cost estimate per day based on budget"
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

    st.markdown(f"## 🗺️ {data.get('destination', destination)}")
    st.markdown(f"*{data.get('tagline', '')}*")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("📅 Days", days)
    m2.metric("💰 Budget", budget.split("(")[0].strip())
    m3.metric("🗓️ Best time", data.get("best_time", "Year-round"))
    m4.metric("💵 Daily est.", data.get("estimated_daily_cost", "See tips"))

    st.divider()

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

    tips = data.get("practical_tips", [])
    if tips:
        tips_html = "".join([f"<li>{t}</li>" for t in tips])
        st.markdown(f"""
<div class="tip-box">
  <strong>💡 Practical Tips</strong>
  <ul style="margin-top:0.5rem; padding-left:1.2rem">{tips_html}</ul>
</div>
""", unsafe_allow_html=True)

    st.markdown(f"**💱 Currency:** {data.get('currency', '')}")
    st.success("✅ Itinerary ready! Scroll up to review your full trip plan.")
