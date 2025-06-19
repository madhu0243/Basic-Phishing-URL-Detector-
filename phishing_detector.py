import re

def is_phishing(url):
    score = 0

    if re.match(r"https?:\/\/\d+\.\d+\.\d+\.\d+", url):
        score += 1
    if '@' in url:
        score += 1
    if len(url) > 75:
        score += 1
    if not url.startswith('https://'):
        score += 1
    if '-' in url:
        score += 1

    if score >= 3:
        return "Phishing suspected 🚨"
    else:
        return "Probably safe ✅"

# Example usage
url_input = input("Enter URL to check: ")
print(is_phishing(url_input))
