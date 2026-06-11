import streamlit as st
from groq import Groq
import json
import os
import requests

st.set_page_config(
    page_title="WanderAI – Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Sidebar: AI Mode ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ AI Settings")
    st.divider()

    ai_mode = st.radio(
        "🤖 AI Backend",
        ["☁️ Groq API (Cloud)", "🖥️ Ollama (Local)"],
        help="Cloud AI needs an API key. Local AI runs on your machine — no key needed."
    )

    st.divider()

    if ai_mode == "☁️ Groq API (Cloud)":
        st.markdown("**☁️ Groq API — BYOK**")
        st.markdown("Get a free key at [console.groq.com](https://console.groq.com)")

        default_key = ""
        try:
            default_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
        except Exception:
            default_key = os.environ.get("GROQ_API_KEY", "")

        byok_key = st.text_input(
            "🔑 Your Groq API Key",
            value=default_key,
            type="password",
            placeholder="gsk_...",
            help="Paste your Groq API key here. It stays in your browser session only."
        )
        groq_model = st.selectbox(
            "🧠 Model",
            ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
            help="llama-3.3-70b gives best results. 8b is faster."
        )
        st.caption("✅ Free tier — no credit card needed")

    else:
        st.markdown("**🖥️ Ollama — Local Inference**")
        st.markdown("Runs 100% on your machine. No API key. No data sent anywhere.")

        ollama_url = st.text_input(
            "🌐 Ollama URL",
            value="http://localhost:11434",
            help="URL where Ollama is running locally"
        )
        ollama_model = st.selectbox(
            "🧠 Local Model",
            ["llama3.2", "llama3.1", "mistral", "gemma2", "phi3"],
            help="Must be pulled first with: ollama pull llama3.2"
        )

        if st.button("🔌 Test Connection"):
            try:
                r = requests.get(f"{ollama_url}/api/tags", timeout=3)
                if r.status_code == 200:
                    models = [m["name"] for m in r.json().get("models", [])]
                    if models:
                        st.success(f"✅ Connected! Found: {', '.join(models[:3])}")
                    else:
                        st.warning("✅ Connected but no models. Run: `ollama pull llama3.2`")
                else:
                    st.error("❌ Ollama not responding")
            except Exception:
                st.error("❌ Can't connect. Is Ollama running? Try: `ollama serve`")

        st.divider()
        st.markdown("""
**Quick Setup:**
```bash
# 1. Install Ollama
# → https://ollama.com

# 2. Pull a model
ollama pull llama3.2

# 3. Start server
ollama serve
```
""")
        st.caption("💡 Your data never leaves your machine")

# ── Translations ──────────────────────────────────────────────────────────────
LANG = {
    "English": {
        "tagline": "Your AI-powered travel itinerary planner — just tell it where you want to go.",
        "destination": "🌍 Destination",
        "destination_placeholder": "e.g. Tokyo, Japan",
        "days": "📅 Number of days",
        "travel_style": "🎒 Travel style",
        "travel_style_options": [
            "Balanced (mix of everything)",
            "Cultural & historical",
            "Adventure & outdoors",
            "Food & nightlife",
            "Luxury & relaxation",
            "Budget backpacker"
        ],
        "travel_month": "🗓️ Month of travel",
        "months": ["January","February","March","April","May","June",
                   "July","August","September","October","November","December"],
        "budget": "💰 Budget per person (₹) — excluding flights",
        "budget_help": "Total trip budget per person in Indian Rupees, not including flight tickets",
        "hotel": "🏨 Hotel preference",
        "hotel_options": [
            "Budget (Hostel/Guesthouse ₹500–₹1500/night)",
            "Mid-range (3-star ₹1500–₹4000/night)",
            "Comfortable (4-star ₹4000–₹8000/night)",
            "Luxury (5-star ₹8000+/night)"
        ],
        "travelers": "👥 Travelling as",
        "travelers_options": ["Solo", "Couple", "Family with kids", "Group of friends"],
        "interests": "💡 Special interests (optional)",
        "interests_placeholder": "e.g. anime, street food, hiking, museums",
        "generate_btn": "✨ Generate My Itinerary",
        "error_destination": "Please enter a destination first.",
        "spinner": "Planning your perfect trip…",
        "weather_label": "🌤️ Weather in",
        "hotel_label": "🏨 Hotel Recommendation:",
        "foods_label": "**🍜 Must-try foods:**",
        "itinerary_label": "### 📋 Your Day-by-Day Itinerary",
        "day_label": "Day",
        "morning": "🌅 Morning:",
        "afternoon": "☀️ Afternoon:",
        "evening": "🌙 Evening:",
        "food_tip": "🍽️ Food tip:",
        "transport": "🚌 Getting around:",
        "budget_breakdown": "💸 Budget Breakdown (per person, excluding flights)",
        "hotel_nights": "🏨 Hotel",
        "nights": "nights",
        "food_days": "🍽️ Food",
        "days_label": "days",
        "activities": "🎯 Activities & Entry fees:",
        "local_transport": "🚌 Local transport:",
        "total": "💰 Total estimated:",
        "tips_label": "💡 Practical Tips",
        "packing_label": "🎒 Packing tips for",
        "currency_label": "**💱 Currency:**",
        "success": "✅ Itinerary ready! Scroll up to review your full trip plan.",
        "metric_days": "📅 Days",
        "metric_budget": "💰 Budget",
        "metric_month": "📅 Travelling in",
        "metric_group": "👥 Group",
        "prompt_lang": "English",
    },
    "हिन्दी (Hindi)": {
        "tagline": "आपका AI यात्रा योजनाकार — बस बताइए कहाँ जाना है।",
        "destination": "🌍 गंतव्य (Destination)",
        "destination_placeholder": "जैसे Tokyo, Japan",
        "days": "📅 दिनों की संख्या",
        "travel_style": "🎒 यात्रा शैली",
        "travel_style_options": [
            "संतुलित (सब कुछ मिला-जुला)",
            "सांस्कृतिक और ऐतिहासिक",
            "साहसिक और आउटडोर",
            "खाना और नाइटलाइफ",
            "लग्ज़री और आराम",
            "बजट बैकपैकर"
        ],
        "travel_month": "🗓️ यात्रा का महीना",
        "months": ["जनवरी","फ़रवरी","मार्च","अप्रैल","मई","जून",
                   "जुलाई","अगस्त","सितंबर","अक्टूबर","नवंबर","दिसंबर"],
        "budget": "💰 प्रति व्यक्ति बजट (₹) — फ्लाइट के अलावा",
        "budget_help": "भारतीय रुपये में प्रति व्यक्ति कुल यात्रा बजट, फ्लाइट टिकट शामिल नहीं",
        "hotel": "🏨 होटल प्राथमिकता",
        "hotel_options": [
            "बजट (हॉस्टल/गेस्टहाउस ₹500–₹1500/रात)",
            "मध्यम (3-स्टार ₹1500–₹4000/रात)",
            "आरामदायक (4-स्टार ₹4000–₹8000/रात)",
            "लग्ज़री (5-स्टार ₹8000+/रात)"
        ],
        "travelers": "👥 किसके साथ यात्रा",
        "travelers_options": ["अकेले", "जोड़ा", "बच्चों के साथ परिवार", "दोस्तों का समूह"],
        "interests": "💡 विशेष रुचियाँ (वैकल्पिक)",
        "interests_placeholder": "जैसे anime, स्ट्रीट फूड, हाइकिंग, संग्रहालय",
        "generate_btn": "✨ मेरी यात्रा योजना बनाएं",
        "error_destination": "कृपया पहले गंतव्य दर्ज करें।",
        "spinner": "आपकी परफेक्ट यात्रा की योजना बन रही है…",
        "weather_label": "🌤️ मौसम —",
        "hotel_label": "🏨 होटल सुझाव:",
        "foods_label": "**🍜 जरूर खाएं:**",
        "itinerary_label": "### 📋 दिन-दर-दिन यात्रा कार्यक्रम",
        "day_label": "दिन",
        "morning": "🌅 सुबह:",
        "afternoon": "☀️ दोपहर:",
        "evening": "🌙 शाम:",
        "food_tip": "🍽️ खाने की टिप:",
        "transport": "🚌 आवागमन:",
        "budget_breakdown": "💸 बजट विवरण (प्रति व्यक्ति, फ्लाइट के अलावा)",
        "hotel_nights": "🏨 होटल",
        "nights": "रातें",
        "food_days": "🍽️ खाना",
        "days_label": "दिन",
        "activities": "🎯 गतिविधियाँ और प्रवेश शुल्क:",
        "local_transport": "🚌 स्थानीय परिवहन:",
        "total": "💰 कुल अनुमानित:",
        "tips_label": "💡 व्यावहारिक सुझाव",
        "packing_label": "🎒 पैकिंग टिप्स —",
        "currency_label": "**💱 मुद्रा:**",
        "success": "✅ यात्रा योजना तैयार! ऊपर स्क्रॉल करके देखें।",
        "metric_days": "📅 दिन",
        "metric_budget": "💰 बजट",
        "metric_month": "📅 यात्रा माह",
        "metric_group": "👥 समूह",
        "prompt_lang": "Hindi",
    },
    "తెలుగు (Telugu)": {
        "tagline": "మీ AI ట్రావెల్ ప్లానర్ — మీరు ఎక్కడికి వెళ్ళాలో చెప్పండి.",
        "destination": "🌍 గమ్యస్థానం (Destination)",
        "destination_placeholder": "ఉదా: Tokyo, Japan",
        "days": "📅 రోజుల సంఖ్య",
        "travel_style": "🎒 ప్రయాణ శైలి",
        "travel_style_options": [
            "సమతుల్య (అన్నీ కలిపి)",
            "సాంస్కృతిక & చారిత్రక",
            "సాహసం & అడవి",
            "భోజనం & నైట్‌లైఫ్",
            "విలాసవంతమైన & విశ్రాంతి",
            "బడ్జెట్ బ్యాక్‌ప్యాకర్"
        ],
        "travel_month": "🗓️ ప్రయాణ నెల",
        "months": ["జనవరి","ఫిబ్రవరి","మార్చి","ఏప్రిల్","మే","జూన్",
                   "జూలై","ఆగస్టు","సెప్టెంబర్","అక్టోబర్","నవంబర్","డిసెంబర్"],
        "budget": "💰 తలసరి బడ్జెట్ (₹) — విమానం మినహా",
        "budget_help": "విమాన టికెట్లు మినహా భారతీయ రూపాయలలో తలసరి మొత్తం బడ్జెట్",
        "hotel": "🏨 హోటల్ ప్రాధాన్యత",
        "hotel_options": [
            "బడ్జెట్ (హాస్టల్/గెస్ట్‌హౌస్ ₹500–₹1500/రాత్రి)",
            "మధ్యస్థ (3-స్టార్ ₹1500–₹4000/రాత్రి)",
            "సౌకర్యవంతమైన (4-స్టార్ ₹4000–₹8000/రాత్రి)",
            "విలాసవంతమైన (5-స్టార్ ₹8000+/రాత్రి)"
        ],
        "travelers": "👥 ఎవరితో ప్రయాణం",
        "travelers_options": ["ఒంటరిగా", "జంట", "పిల్లలతో కుటుంబం", "స్నేహితుల బృందం"],
        "interests": "💡 ప్రత్యేక ఆసక్తులు (ఐచ్ఛికం)",
        "interests_placeholder": "ఉదా: anime, వీధి ఆహారం, హైకింగ్, మ్యూజియంలు",
        "generate_btn": "✨ నా యాత్రా ప్రణాళిక రూపొందించండి",
        "error_destination": "దయచేసి ముందుగా గమ్యస్థానం నమోదు చేయండి.",
        "spinner": "మీ పర్ఫెక్ట్ ట్రిప్ ప్లాన్ చేయబడుతోంది…",
        "weather_label": "🌤️ వాతావరణం —",
        "hotel_label": "🏨 హోటల్ సిఫారసు:",
        "foods_label": "**🍜 తప్పకుండా తినండి:**",
        "itinerary_label": "### 📋 రోజువారీ యాత్రా కార్యక్రమం",
        "day_label": "రోజు",
        "morning": "🌅 ఉదయం:",
        "afternoon": "☀️ మధ్యాహ్నం:",
        "evening": "🌙 సాయంత్రం:",
        "food_tip": "🍽️ ఆహార చిట్కా:",
        "transport": "🚌 రవాణా:",
        "budget_breakdown": "💸 బడ్జెట్ వివరాలు (తలసరి, విమానం మినహా)",
        "hotel_nights": "🏨 హోటల్",
        "nights": "రాత్రులు",
        "food_days": "🍽️ ఆహారం",
        "days_label": "రోజులు",
        "activities": "🎯 కార్యకలాపాలు & ప్రవేశ రుసుములు:",
        "local_transport": "🚌 స్థానిక రవాణా:",
        "total": "💰 మొత్తం అంచనా:",
        "tips_label": "💡 ఆచరణాత్మక చిట్కాలు",
        "packing_label": "🎒 ప్యాకింగ్ చిట్కాలు —",
        "currency_label": "**💱 కరెన్సీ:**",
        "success": "✅ యాత్రా ప్రణాళిక సిద్ధం! పైకి స్క్రోల్ చేయండి.",
        "metric_days": "📅 రోజులు",
        "metric_budget": "💰 బడ్జెట్",
        "metric_month": "📅 ప్రయాణ నెల",
        "metric_group": "👥 బృందం",
        "prompt_lang": "Telugu",
    }
}

# ── Language Selector ─────────────────────────────────────────────────────────
lang_choice = st.selectbox("🌐 Language / भाषा / భాష", list(LANG.keys()), label_visibility="visible")
t = LANG[lang_choice]

# ── Styles ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@300;400;500;600&family=Noto+Sans+Telugu:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', 'Noto Sans Devanagari', 'Noto Sans Telugu', sans-serif; }

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
.hero p { color: #a8c5d6; font-size: 1.1rem; margin-top: 0.5rem; font-weight: 300; }
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
.day-card h3 { font-family: 'Playfair Display', serif; color: #2c5364; font-size: 1.3rem; margin-top: 0; margin-bottom: 0.5rem; }
.day-card ul { margin: 0.5rem 0; padding-left: 1.2rem; }
.day-card li { margin-bottom: 0.4rem; color: #444; line-height: 1.6; }

.tip-box { background: #fff8f0; border: 1px solid #f0d9b5; border-radius: 10px; padding: 1rem 1.2rem; margin-top: 1.5rem; }
.tip-box strong { color: #b07c3f; }

.budget-box { background: #f0faf4; border: 1px solid #b7e4c7; border-radius: 10px; padding: 1rem 1.2rem; margin-top: 1.5rem; }
.budget-box strong { color: #1a7f4b; }
.budget-box ul { margin: 0.5rem 0; padding-left: 1.2rem; }
.budget-box li { margin-bottom: 0.3rem; color: #333; }

.badge { display: inline-block; background: #eaf4fb; color: #2c5364; border-radius: 20px; padding: 3px 12px; font-size: 0.78rem; font-weight: 600; margin: 2px; letter-spacing: 0.3px; }

.stButton > button {
    background: linear-gradient(135deg, #2c5364, #203a43) !important;
    color: white !important; border: none !important; border-radius: 10px !important;
    padding: 0.6rem 2rem !important; font-size: 1rem !important; font-weight: 500 !important;
    width: 100%; transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.88; }
.meta-row { display: flex; gap: 0.6rem; flex-wrap: wrap; margin-bottom: 1.5rem; justify-content: center; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <span class="emoji">✈️</span>
  <h1>WanderAI</h1>
  <p>{t["tagline"]}</p>
</div>
""", unsafe_allow_html=True)

# ── Input Form ────────────────────────────────────────────────────────────────
with st.form("planner_form"):
    col1, col2 = st.columns(2)
    with col1:
        destination = st.text_input(t["destination"], placeholder=t["destination_placeholder"])
        days = st.slider(t["days"], 1, 14, 5)
        travel_style = st.selectbox(t["travel_style"], t["travel_style_options"])
        travel_month = st.selectbox(t["travel_month"], t["months"])

    with col2:
        budget_per_person = st.number_input(
            t["budget"], min_value=1000, max_value=1000000, value=30000, step=1000, help=t["budget_help"]
        )
        hotel_budget = st.selectbox(t["hotel"], t["hotel_options"])
        travelers = st.selectbox(t["travelers"], t["travelers_options"])
        interests = st.text_input(t["interests"], placeholder=t["interests_placeholder"])

    submitted = st.form_submit_button(t["generate_btn"])

# ── Generation ────────────────────────────────────────────────────────────────
if submitted:
    if not destination.strip():
        st.error(t["error_destination"])
        st.stop()

    per_day_budget = budget_per_person // days

    with st.spinner(t["spinner"]):
        prompt = f"""You are an expert travel planner for Indian travellers. Create a detailed, practical {days}-day travel itinerary for {destination}.
Respond entirely in {t["prompt_lang"]} language.

Traveller details:
- Travel style: {travel_style}
- Total budget per person (excluding flights): ₹{budget_per_person:,} INR
- Per day budget: ₹{per_day_budget:,} INR
- Hotel preference: {hotel_budget}
- Travelling as: {travelers}
- Travel month: {travel_month}
- Special interests: {interests if interests else 'none specified'}

IMPORTANT: All prices and costs MUST be in Indian Rupees (₹ INR). Convert all local prices to INR.
Respond entirely in {t["prompt_lang"]} language for all text values in the JSON.

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
            if ai_mode == "☁️ Groq API (Cloud)":
                # ── Groq BYOK ──────────────────────────────────────────────
                key = byok_key.strip() if byok_key.strip() else os.environ.get("GROQ_API_KEY", "")
                if not key:
                    st.error("⚠️ Please enter your Groq API key in the sidebar.")
                    st.stop()
                client = Groq(api_key=key)
                response = client.chat.completions.create(
                    model=groq_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=4000,
                )
                raw = response.choices[0].message.content.strip()

            else:
                # ── Ollama Local Inference ─────────────────────────────────
                url = f"{ollama_url}/api/chat"
                payload = {
                    "model": ollama_model,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                    "options": {"temperature": 0.7, "num_predict": 4000}
                }
                r = requests.post(url, json=payload, timeout=120)
                if r.status_code != 200:
                    st.error(f"❌ Ollama error {r.status_code}: {r.text[:200]}")
                    st.stop()
                raw = r.json()["message"]["content"].strip()

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
    m1.metric(t["metric_days"], days)
    m2.metric(t["metric_budget"], f"₹{budget_per_person:,}")
    m3.metric(t["metric_month"], travel_month)
    m4.metric(t["metric_group"], travelers)

    st.divider()

    weather = data.get("weather_in_month", "")
    if weather:
        st.info(f"{t['weather_label']} {travel_month}: {weather}")

    hotel = data.get("hotel_recommendation", "")
    if hotel:
        st.success(f"{t['hotel_label']} {hotel}")

    foods = data.get("must_try_foods", [])
    if foods:
        st.markdown(t["foods_label"])
        food_html = " ".join([f'<span class="badge">{f}</span>' for f in foods])
        st.markdown(f'<div class="meta-row">{food_html}</div>', unsafe_allow_html=True)

    st.markdown(t["itinerary_label"])

    for day in data.get("days", []):
        card = f"""
<div class="day-card">
  <h3>{t["day_label"]} {day['day']} — {day.get('theme', '')}</h3>
  <ul>
    <li><strong>{t["morning"]}</strong> {day.get('morning', '')}</li>
    <li><strong>{t["afternoon"]}</strong> {day.get('afternoon', '')}</li>
    <li><strong>{t["evening"]}</strong> {day.get('evening', '')}</li>
  </ul>
  <p style="margin-bottom:4px">🍽️ <em>{t["food_tip"]} {day.get('food_tip', '')}</em></p>
  <p style="margin:0">🚌 <em>{t["transport"]} {day.get('transport', '')}</em></p>
</div>"""
        st.markdown(card, unsafe_allow_html=True)

    budget_data = data.get("budget_breakdown", {})
    if budget_data:
        budget_items = "".join([
            f"<li>{t['hotel_nights']} ({days} {t['nights']}): {budget_data.get('hotel_total', '')}</li>",
            f"<li>{t['food_days']} ({days} {t['days_label']}): {budget_data.get('food_total', '')}</li>",
            f"<li>{t['activities']} {budget_data.get('activities_total', '')}</li>",
            f"<li>{t['local_transport']} {budget_data.get('transport_local', '')}</li>",
            f"<li>{t['total']} {budget_data.get('total_estimated', '')}</li>",
        ])
        st.markdown(f"""
<div class="budget-box">
  <strong>{t["budget_breakdown"]}</strong>
  <ul style="margin-top:0.5rem">{budget_items}</ul>
  <p style="margin:0.5rem 0 0; font-size:0.9rem; color:#555">📝 {budget_data.get('budget_note', '')}</p>
</div>
""", unsafe_allow_html=True)

    tips = data.get("practical_tips", [])
    if tips:
        tips_html = "".join([f"<li>{tip}</li>" for tip in tips])
        st.markdown(f"""
<div class="tip-box">
  <strong>{t["tips_label"]}</strong>
  <ul style="margin-top:0.5rem; padding-left:1.2rem">{tips_html}</ul>
</div>
""", unsafe_allow_html=True)

    packing = data.get("packing_tips", "")
    if packing:
        st.markdown(f"🎒 **{t['packing_label']} {travel_month}:** {packing}")

    st.markdown(f"{t['currency_label']} {data.get('currency', '')}")
    st.success(t["success"])
