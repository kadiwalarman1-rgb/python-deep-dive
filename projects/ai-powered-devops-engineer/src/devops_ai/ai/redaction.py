"""Best-effort redaction for common secrets before optional external AI calls."""

from __future__ import annotations

import re

_PATTERNS = (
    (re.compile(r"(?i)\b(authorization\s*[:=]\s*bearer)\s+[A-Za-z0-9._~+/\-=]+"), r"\1 [REDACTED]"),
    (re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*([^\s,;]+)"), r"\1=[REDACTED]"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "[REDACTED_AWS_ACCESS_KEY]"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.DOTALL), "[REDACTED_PRIVATE_KEY]"),
)


def redact_sensitive_text(value: str, *, max_chars: int = 12_000) -> str:
    text = value[:max_chars]
    for pattern, replacement in _PATTERNS:
        text = pattern.sub(replacement, text)
    return text
