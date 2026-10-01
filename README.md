# Build Your First AI Agent

A hands-on workshop: build a working AI agent in Python that helps a patient find
clinical trials — and watch the same question get dramatically better as you add
**grounding** (RAG) and a **tool + reasoning loop**.

Built with the open-source [Strands Agents SDK](https://strandsagents.com) from
AWS, running Claude Sonnet 4.5 on Amazon Bedrock.

## The idea

You ask **one** question at three levels of capability:

| Stage | What you add | The answer becomes |
|-------|-------------|--------------------|
| **1 · Baseline** | Just the model + a system prompt | Vague, generic, may invent trials |
| **2 · RAG** ★ | Retrieval from a Bedrock Knowledge Base | Grounded — names real trials, cites NCT IDs |
| **3 · Tool + loop** | A live ClinicalTrials.gov API tool | Actionable — a ranked shortlist of recruiting trials |

The question:

> *"I'm a 55-year-old female ER+/HER2- disease free breast cancer survivor who
> has been on letrozole for 7 years and now is suffering from severe side
> effects. Are there clinical trials I might qualify for?"*

## Files

- `agent.py` — **the file you edit.** Ships as the Stage 1 baseline.
- `config.py` / `config.json` — model id, region, Knowledge Base id.
- `data/cached_trials.json` — bundled real-trial snapshot (Stage 3 fallback).
- `solutions/` — complete reference `agent.py` for each stage.
- `requirements.txt` — `strands-agents`, `boto3`, `requests`.

## Run it

```bash
pip install -r requirements.txt
python agent.py
```

On the workshop desktop everything is pre-installed and `config.json` is already
filled in with your Knowledge Base id. Running locally later? Copy
`config.example.json` to `config.json`, add your KB id, and make sure your AWS
credentials can call Bedrock in your region.

## Resources — build your next agent

- **Strands Agents SDK** — https://strandsagents.com (docs, model providers, tools, MCP)
- **Amazon Bedrock** — https://docs.aws.amazon.com/bedrock/
- **Bedrock Knowledge Bases** (managed RAG) — https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
  - The Strands-native way to query a KB: `MemoryManager` + `BedrockKnowledgeBaseStore(writable=False)`
- **Kiro** — https://kiro.dev (the AI IDE used to build this)
- **ClinicalTrials.gov API v2** — https://clinicaltrials.gov/data-api/api

### Where to take it next
- Add more tools that hit your own internal data sources and APIs.
- Hand off tasks to other agents (multi-agent).
- Add guardrails and grow the system prompt / context.

---
*Clinical-trial data © ClinicalTrials.gov (public domain). This workshop is for
education, not medical advice.*
