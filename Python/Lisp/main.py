import requests

url = 'http://fuperfiberneticinterpolator.challs.open.ecsc2024.it/interpolate'
payload = {
    "template": "Hello, {name}! Your age is {age}.",
    "substitutions": [
        {"name": "Alice"},
        {"age": 30}
    ],
    "template-supplied-p": True
}

response = requests.post(url, json=payload)
print(response.text)
