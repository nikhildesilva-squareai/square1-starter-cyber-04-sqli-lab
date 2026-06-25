"""SQL Injection Lab — Square 1 AI starter."""
from .detector import is_query_safe, parameterize_query, detect_injection_in_input

__all__ = ["is_query_safe", "parameterize_query", "detect_injection_in_input"]
