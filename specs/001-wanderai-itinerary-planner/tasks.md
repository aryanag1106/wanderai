# Tasks: WanderAI — AI Travel Itinerary Planner

**Feature:** 001-wanderai-itinerary-planner  
**Author:** Aryan Agarwal  
**Date:** June 2026  
**Input:** spec.md + plan.md

---

## Phase 0 — Foundational Setup

- [x] **T-01** Initialise project folder `wanderai/`
- [x] **T-02** Create `requirements.txt` with `streamlit` and `groq`
- [x] **T-03** Create `.gitignore` excluding `secrets.toml` and `venv/`
- [x] **T-04** Create `.streamlit/config.toml` with teal/off-white theme
- [x] **T-05** Create `.streamlit/secrets.toml` template (not committed)
- [x] **T-06** Get free Groq API key from console.groq.com
- [x] **T-07** Initialise git repo and push to code.swecha.org

---

## Phase 1 — Core UI [US1]

- [x] **T-08** Set up `st.set_page_config` with title, icon, wide layout
- [x] **T-09** Inject custom CSS — hero banner, day card, tip box, budget box, badge styles
- [x] **T-10** Render hero banner with gradient background and tagline
- [x] **T-11** Build two-column input form with `st.form`
- [x] **T-12** Add `destination` text input with placeholder
- [x] **T-13** Add `days` slider (1–14, default 5)
- [x] **T-14** Add `travel_style` selectbox with 6 options
- [x] **T-15** Add `travel_month` selectbox with all 12 months
- [x] **T-16** Add `budget_per_person` number input in ₹ INR (min 1000, max 1000000, step 1000)
- [x] **T-17** Add `hotel_budget` selectbox with 4 tiers and INR price ranges
- [x] **T-18** Add `travelers` selectbox (Solo, Couple, Family, Friends)
- [x] **T-19** Add optional `interests` text input
- [x] **T-20** Add form submit button "✨ Generate My Itinerary"
- [x] **T-21** Add destination validation — block API call if empty, show error

---

## Phase 2 — AI Integration [US1, US2]

- [x] **T-22** Calculate `per_day_budget = budget_per_person // days`
- [x] **T-23** Build prompt f-string injecting all user inputs
- [x] **T-24** Add `"All prices MUST be in ₹ INR"` instruction to prompt
- [x] **T-25** Define full JSON output schema in prompt
- [x] **T-26** Read API key from `st.secrets` with `os.environ` fallback
- [x] **T-27** Create `Groq` client and call `chat.completions.create`
- [x] **T-28** Set `model="llama-3.3-70b-versatile"`, `temperature=0.7`, `max_tokens=4000`
- [x] **T-29** Strip markdown fences from raw response
- [x] **T-30** Parse JSON response with `json.loads`
- [x] **T-31** Handle parse errors — show error + raw output for debugging
- [x] **T-32** Wrap API call in try/except — show user-friendly error message

---

## Phase 3 — Result Display [US2, US3, US4, US5]

- [x] **T-33** Render destination heading and tagline
- [x] **T-34** Render 4-column metrics row (days, budget, month, group)
- [x] **T-35** Render weather info in `st.info` blue box [US4]
- [x] **T-36** Render hotel recommendation in `st.success` green box [US4]
- [x] **T-37** Render must-try food badges as HTML pills [US5]
- [x] **T-38** Loop through `data["days"]` and render one styled HTML card per day [US2]
- [x] **T-39** Each card shows theme, morning, afternoon, evening, food tip, transport [US2]
- [x] **T-40** Render budget breakdown in green HTML box with all 5 cost lines [US3]
- [x] **T-41** Render practical tips in orange HTML box [US5]
- [x] **T-42** Render packing tips and currency note [US4, US5]
- [x] **T-43** Show `st.success` confirmation at the end

---

## Phase 4 — Deployment

- [x] **T-44** Push code to GitLab (code.swecha.org)
- [x] **T-45** Push code to GitHub for Streamlit Cloud
- [x] **T-46** Deploy on Streamlit Cloud with GROQ_API_KEY in secrets
- [x] **T-47** Verify live URL works end-to-end
- [x] **T-48** Write specs: PRD.md, AI_SPEC.md, DEPLOY_SPEC.md
- [x] **T-49** Write SpecKit: spec.md, plan.md, tasks.md, data-model.md

---

## Summary

| Phase | Tasks | Status |
|-------|-------|--------|
| 0 — Setup | T-01 to T-07 | ✅ Complete |
| 1 — Core UI | T-08 to T-21 | ✅ Complete |
| 2 — AI Integration | T-22 to T-32 | ✅ Complete |
| 3 — Result Display | T-33 to T-43 | ✅ Complete |
| 4 — Deployment | T-44 to T-49 | ✅ Complete |
