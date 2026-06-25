"""Contract tests — fail against the starter stubs; make them pass.

These test the pure detector functions on tiny in-test strings. No server is
started and the big dataset is never read.
"""
from sqli import is_query_safe, parameterize_query, detect_injection_in_input


def test_is_query_safe():
    # Concatenated / interpolated SQL is UNSAFE.
    name = "ava"
    assert is_query_safe("SELECT * FROM users WHERE name = '" + name + "'") is False
    assert is_query_safe(f"SELECT * FROM users WHERE name = '{name}'") is False
    # A parameterized query is SAFE.
    assert is_query_safe("SELECT * FROM users WHERE name = ?") is True


def test_parameterize_query():
    v = "ava"
    unsafe = "SELECT * FROM users WHERE name = '" + v + "'"
    safe_query, params = parameterize_query(unsafe, v)
    assert "?" in safe_query
    assert v not in safe_query          # the value is no longer inlined
    assert params == (v,)


def test_detect_injection_in_input():
    # Clear injection signatures -> True
    assert detect_injection_in_input("' OR '1'='1") is True
    assert detect_injection_in_input("admin'--") is True
    # URL-encoded payload must be decoded first -> True
    assert detect_injection_in_input("%27%20OR%201%3D1") is True
    # Legitimately-quoted name is benign -> False (precision matters)
    assert detect_injection_in_input("O'Brien") is False
    assert detect_injection_in_input("widget") is False
