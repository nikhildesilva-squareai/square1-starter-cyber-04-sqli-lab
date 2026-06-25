"""
The detector — three pure functions. No database, no server: these operate on
plain strings so they're fast, testable, and safe to run anywhere. The contract
tests in tests/test_sqli.py pin down the exact behaviour; make them pass, then
use these to screen the fixed app and to score payloads.csv.
"""
from __future__ import annotations


def is_query_safe(query: str) -> bool:
    """Return True if `query` looks parameterized, False if it concatenates input.

    A *safe* query keeps user values out of the SQL text and uses placeholders
    (e.g. `?` or `:name`). An *unsafe* query is built by gluing values into the
    string — `"... WHERE u = '" + name + "'"`, an f-string with `{name}`, or
    `%`/`.format()` interpolation of values.

    TODO:
      - return True when the query uses placeholders and no value interpolation
      - return False when the query shows string concatenation / f-string /
        %-formatting / .format() of values into the SQL
    """
    raise NotImplementedError("Implement is_query_safe")


def parameterize_query(query: str, value: str) -> tuple:
    """Rewrite a simple single-value concatenated query into a parameterized one.

    Given a query whose text ends by appending one quoted user value, return
    `(safe_query, params)` where `safe_query` uses a `?` placeholder in place of
    the inlined value and `params` is the tuple of bound values.

    Example:
      parameterize_query("SELECT * FROM users WHERE name = '" + v + "'", v)
        -> ("SELECT * FROM users WHERE name = ?", (v,))

    TODO:
      - replace the inlined, quoted value with a single `?` placeholder
      - return (safe_query, (value,))
    """
    raise NotImplementedError("Implement parameterize_query")


def detect_injection_in_input(value: str) -> bool:
    """Return True if `value` is an injection attempt, False if it's benign.

    Decode first (URL/percent-encoding) so encoded payloads aren't missed, then
    decide. The hard part is precision: a lone apostrophe in `O'Brien` or
    `5'9" shelf` is ordinary data, NOT an attack — don't flag it. Look for input
    that breaks out of a string literal and adds SQL logic (e.g. `' OR `,
    `'--`, `UNION SELECT`, a trailing comment after a closed quote).

    TODO:
      - URL-decode the value
      - return True for clear injection signatures, False for benign text
      - keep legitimately-quoted names (O'Brien, d'Angelo) as False
    """
    raise NotImplementedError("Implement detect_injection_in_input")
