"""Workshop configuration.

Reads config.json if it exists (the workshop desktop ships one, pre-filled with
your Knowledge Base ID), otherwise falls back to environment variables and
sensible defaults. You should not need to edit this file during the workshop.
"""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_HERE, "config.json")

_cfg = {}
if os.path.exists(_CONFIG_PATH):
    with open(_CONFIG_PATH) as fh:
        _cfg = json.load(fh)

# Claude Sonnet 4.5 on Amazon Bedrock (US cross-region inference profile).
MODEL_ID = _cfg.get("model_id") or os.environ.get(
    "MODEL_ID", "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
)
REGION = _cfg.get("region") or os.environ.get("AWS_REGION", "us-east-1")

# Pre-built Amazon Bedrock Knowledge Base (Stage 2). Empty until you paste it in
# or the workshop desktop provides it.
KNOWLEDGE_BASE_ID = _cfg.get("knowledge_base_id") or os.environ.get(
    "KNOWLEDGE_BASE_ID", ""
)
