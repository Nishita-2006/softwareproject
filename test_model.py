import requests

url = "http://127.0.0.1:5000/analyze_text"
test_cases = [
    "I am feeling very happy and excited today!",
    "I feel so lonely and sad, nothing seems to go right.",
    "I am so angry at how things turned out.",
    "It's just a normal day, nothing special."
]

for text in test_cases:
    try:
        response = requests.post(url, json={"text": text})
        if response.status_code == 200:
            data = response.json()
            print(f"Text: {text}")
            print(f"  Emotion: {data['emotion']}, Severity: {data['severity']}, Confidence: {data['confidence']}")
            print(f"  Headline: {data['headline']}")
            print("-" * 30)
        else:
            print(f"Error for '{text}': {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to connect to server: {e}")
