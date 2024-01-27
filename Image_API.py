'''
Date: Friday, January 26 2024
Desc: This is the code designed with instructions to
        - Recieve an image url
        - pass the image url to online API
        - Preprocess the information
        - Send the information back to the backend
'''

'''
method accepts ([string] url of image, [string] push/pull)
based 
'''
import requests

# Replace 'your_subscription_key' with your actual subscription key.
subscription_key = 'b2fce44dfd2b448c915051dcdec5426e'
assert subscription_key

# Replace 'base_url' with the actual base URL provided by Microsoft.
base_url = 'https://uofthacks11.cognitiveservices.azure.com//vision/v3.1/describe'
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json'}
params = {
    'language': 'en',  # For example, use 'en' for English
    'maxCandidates': '1',
}
body = {
    'url': 'https://buffer.com/library/content/images/size/w1200/2023/10/free-images.jpg'
}

response = requests.post(base_url, headers=headers, params=params, json=body)
response.raise_for_status()
analysis = response.json()
print(analysis)