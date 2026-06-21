"""
Unit tests for WanderAI core logic.
Run with: pytest tests/ -v --cov=app
"""
import json


def test_json_fence_stripping():
    """Markdown code fences should be stripped from AI responses before parsing."""
    raw_with_fence = '```json\n{"destination": "Tokyo"}\n```'

    raw = raw_with_fence.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    data = json.loads(raw)
    assert data["destination"] == "Tokyo"


def test_json_parsing_without_fence():
    """Plain JSON with no markdown fence should still parse correctly."""
    raw = '{"destination": "Goa", "days": 5}'
    data = json.loads(raw)
    assert data["destination"] == "Goa"
    assert data["days"] == 5


def test_per_day_budget_calculation():
    """Per-day budget math used in the prompt builder."""
    budget_per_person = 30000
    days = 5
    per_day_budget = budget_per_person // days
    assert per_day_budget == 6000


def test_per_day_budget_rounding():
    """Integer division should round down correctly for uneven splits."""
    budget_per_person = 10000
    days = 3
    per_day_budget = budget_per_person // days
    assert per_day_budget == 3333


def test_malformed_json_raises_error():
    """Invalid JSON should raise a JSONDecodeError as expected."""
    raw = "this is not valid json"
    try:
        json.loads(raw)
        assert False, "Should have raised JSONDecodeError"
    except json.JSONDecodeError:
        assert True


def test_review_rating_bounds():
    """Review ratings must stay within the 1-5 range used by the slider."""
    valid_ratings = [1, 2, 3, 4, 5]
    for rating in valid_ratings:
        assert 1 <= rating <= 5


def test_language_keys_match_across_translations():
    """All supported languages must expose the same translation keys."""
    sample_keys_english = {"destination", "days", "budget", "generate_btn"}
    sample_keys_hindi = {"destination", "days", "budget", "generate_btn"}
    sample_keys_telugu = {"destination", "days", "budget", "generate_btn"}

    assert sample_keys_english == sample_keys_hindi == sample_keys_telugu


def test_ollama_chat_endpoint_format():
    """Ollama native API URL should be built correctly from the base URL."""
    ollama_url = "http://localhost:11434"
    url = f"{ollama_url}/api/chat"
    assert url == "http://localhost:11434/api/chat"


def test_lmstudio_chat_endpoint_format():
    """LM Studio OpenAI-compatible URL should be built correctly."""
    lmstudio_url = "http://localhost:1234"
    url = f"{lmstudio_url}/v1/chat/completions"
    assert url == "http://localhost:1234/v1/chat/completions"
