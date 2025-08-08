from difflib import SequenceMatcher

# Load homoglyph mapping
HOMOGLYPHS = {
    'а': 'a',  # Cyrillic a
    'е': 'e',  # Cyrillic e
    'і': 'i',  # Cyrillic i
    'о': 'o',  # Cyrillic o
    'р': 'p',  # Cyrillic p
    'с': 'c',  # Cyrillic c
    'у': 'y',  # Cyrillic y
    'х': 'x',  # Cyrillic x
    'ɡ': 'g',  # Latin small script g
    'ꞯ': 'd',
    'ａ': 'a',
    'Ｇ': 'G'
}

def normalize_url(url):
    return ''.join(HOMOGLYPHS.get(char, char) for char in url)

def is_similar(normalized_url, safe_domains):
    for domain in safe_domains:
        ratio = SequenceMatcher(None, normalized_url, domain).ratio()
        if ratio > 0.8:
            return domain, ratio
    return None, 0

def detect_from_file(test_file, safe_file):
    with open(safe_file, 'r', encoding='utf-8') as f:
        safe_domains = [line.strip() for line in f.readlines()]

    with open(test_file, 'r', encoding='utf-8') as f:
        test_urls = [line.strip() for line in f.readlines()]

    for url in test_urls:
        normalized = normalize_url(url)
        matched_domain, score = is_similar(normalized, safe_domains)
        print(f"🔍 Testing: {url}")
        print(f"🔧 Normalized: {normalized}")
        if matched_domain:
            print(f"⚠️ Suspicious! Looks like '{matched_domain}' (score: {score:.2f})\n")
        else:
            print("✅ Looks safe.\n")

# Run detection
detect_from_file('test_urls.txt', 'safe_domains.txt')

