# 🛡️ Homoglyph Domain Detector – PoC

##  Objective
Detect domain names that use **Unicode homoglyphs** to impersonate real websites like `ɡoogle.com` instead of `google.com`. These homoglyph attacks can lead to phishing, identity theft, or malware infections.

---

##  Problem

Attackers use **visually identical characters** from Unicode to create fake domains:
- `ɡoogle.com` → `ɡ` is not regular `g` (it's Unicode U+0261)
- `facebооk.com` → Cyrillic `о`, not English `o`

Users don’t notice the difference. Our tool solves this.

---

##  Solution

This tool:
- Maps homoglyphs to ASCII characters
- Normalizes input domains
- Compares them with a whitelist of real domains
- Flags suspicious look-alike domains

---

## 🧩 Project Structure

