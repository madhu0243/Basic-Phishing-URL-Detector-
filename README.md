# 🔐 Basic Phishing URL Detector 

This is a simple Python project that detects potentially phishing URLs using rule-based heuristics — no machine learning required.

## 🎯 Objective
To identify suspicious URLs based on common phishing indicators such as:
- Presence of IP addresses in place of domain names
- Special characters like `@`, `-`, and `//`
- Excessive URL length
- Absence of HTTPS

## ⚙️ Features
- Detects use of IP addresses instead of domains
- Checks for unsafe symbols (`@`, `-`, etc.)
- Flags overly long URLs
- Verifies HTTPS usage

## 🚀 How to Run
1. Save the script as `phishing_detector.py`
2. Open terminal or command prompt
3. Run the script:

```bash
python phishing_detector.py
```

4. Input a URL when prompted

## 🧪 Example

```
Enter URL to check: http://192.168.0.1/secure-login
Phishing suspected 🚨
```
