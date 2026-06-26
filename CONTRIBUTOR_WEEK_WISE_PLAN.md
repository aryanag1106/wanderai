# Week-wise Plan: Increasing the Contributor Base

**Project:** WanderAI — AI Travel Itinerary Planner
**Author:** Aryan Agarwal
**Status:** Hackathon submission — forward-looking growth plan

This covers growing the number of people who **contribute code, translations,
or docs** to WanderAI — distinct from growing end-users of the app.

## How I plan to increase the contributor base

WanderAI already has the groundwork most new contributors look for before
sending a PR: an AGPLv3 license, a `CONTRIBUTING.md` with setup steps, linting
via `ruff`/`mypy`, pre-commit hooks (ruff, mypy, gitleaks, pip-audit), and a
spec-kit (`specs/`) documenting the PRD, architecture, and task breakdown. The
plan below uses that foundation rather than starting from zero.

| Week | Activities & Targets |
|------|------------------------|
| **Week 1** | Polish the contributor experience: expand `CONTRIBUTING.md` with a "first PR" walkthrough, tag 4–5 small, well-scoped tasks from the PRD's "Secondary Goals" (PDF export, map view, etc.) as **good-first-issue**. Publish the project on code.swecha.org's project explore page. Target: project discoverable with clear entry points for newcomers. |
| **Week 2** | Reach out directly to fellow hackathon participants and college FOSS/coding clubs who are already on code.swecha.org. Share the issue list and the spec docs (`specs/PRD.md`, `specs/AI_SPEC.md`) so newcomers can understand the "why" before the "how." Target: 3–5 people fork/clone the repo. |
| **Week 3** | Run a small "contribution sprint": pick 2–3 of the tagged good-first-issues, pair briefly with anyone interested (a 15-minute call or async chat), and get the first external PR merged. Make sure the CI pipeline (lint → security → test → build → deploy) gives fast, clear feedback on every PR so contributors aren't blocked guessing why a check failed. Target: 1–2 merged external PRs. |
| **Week 4** | Recognise contributors publicly — add a "Contributors" section to `README.md` crediting everyone who merged a PR or improved a translation. Open a lightweight Telegram/Discord channel for contributor coordination and ongoing task triage. Target: a small but real recurring contributor group (3+ people) instead of a one-off PR. |

## How I plan to keep contributors engaged long-term

- **Low-friction onboarding:** setup is already just `git clone` → `pip install -r requirements.txt` → `streamlit run app.py`, with no database or paid API required to run locally (Ollama/LM Studio path needs no API key at all).
- **Fast feedback loop:** the 5-stage CI pipeline means a contributor's PR gets lint/security/test results within minutes, not days.
- **Clear task pipeline:** the `specs/001-wanderai-itinerary-planner/tasks.md` file already tracks completed vs. open tasks, giving contributors an obvious backlog to pick from instead of having to invent work.
- **Conventional commits + auto-changelog:** commits follow a `feat:`/`fix:`/`doc:` convention (`cliff.toml`), so every contributor's work is automatically credited in the changelog on release.
