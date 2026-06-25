# SQL Injection Lab — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · Cybersecurity · Project 4.**

✅ **Data included.** The dataset is committed in [`dataset/`](dataset/) and is the **same standardized dataset every learner uses** — so results are comparable. It is 100% synthetic and Square 1-owned (no third-party or personal data). You can also download it as a single file from the project page on Square 1.

🛡️ **Defensive & self-contained.** The core task runs offline on the included synthetic data (or a bundled local app on `127.0.0.1`) — no live targets, cloud, or network needed, and **no answer key ships**. All techniques are for **authorized testing on the provided material only**. The named heavy tool is a **stretch goal**.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# SQL Injection Lab — starter

Starter for Square 1 AI **Cybersecurity · Project 4**. Exploit a vulnerable app, fix it properly, and build the detector that stops the bug recurring.

> **Authorized use only.** Everything here is a self-contained, offline lab. The bundled `app.py` is **deliberately vulnerable** and exists solely as your local target. Run it on your own machine, attack **only this app and the provided corpus**, never expose it beyond `127.0.0.1`, and never point these techniques at any system you don't own or have written permission to test.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## The data
The data ships in `dataset/`: `app.db` (synthetic users + products with a planted, obviously-fake admin flag), `seed.sql` (rebuilds it), and `payloads.csv` (labelled injection strings). It's **synthetic, Square 1-owned, free**. See `dataset/data_dictionary.md`.

## Your task
Three tests define the contract — they fail until you implement the stubs in `sqli/detector.py`:
```bash
pytest -q
```
- `test_is_query_safe` — flag concatenated/interpolated SQL vs a parameterized query.
- `test_parameterize_query` — rewrite a simple concatenated query to use a `?` placeholder + bound values.
- `test_detect_injection_in_input` — classify an input as injection vs benign, after URL-decoding, **without** flagging legitimately-quoted names like `O'Brien`.

Then run the lab end to end:
```bash
python app.py            # serves the vulnerable app on http://127.0.0.1:5000
```
1. **Exploit** — use `payloads.csv` to bypass `/login` and make `/search?q=` leak internal (`listed=0`) rows and the admin secret. Record which payloads succeed.
2. **Fix** — rewrite `get_user` / `search_products` in `app.py` with parameterized queries + allow-listing. Re-run the payloads: unauthorized access must reach **0**.
3. **Measure & report** — payloads succeeding pre-fix vs post-fix, plus your detector's precision/recall on `payloads.csv`. Write `REMEDIATION.md` for the owning team.

Full brief, rubric, and references are on your Square 1 project page. MIT licensed.
