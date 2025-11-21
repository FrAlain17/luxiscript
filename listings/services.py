import requests
import os
from django.conf import settings

def generate_listing_description(data):
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        return "Error: DeepSeek API key not configured."

    url = "https://api.deepseek.com/v1/chat/completions" # Verify endpoint, usually standard OpenAI compatible
    # DeepSeek usually uses OpenAI compatible endpoint, let's assume standard chat completion
    
    prompt = f"""
    Generate a compelling real estate listing description for a {data.get('property_type')} in {data.get('location')}.
    
    Details:
    - Price: {data.get('price')}
    - Size: {data.get('size')}
    - Bedrooms: {data.get('bedrooms')}
    - Bathrooms: {data.get('bathrooms')}
    - Features: {data.get('features')}
    - Condition: {data.get('condition')}
    
    Tone: {data.get('tone')}
    
    Highlight the lifestyle, location benefits, and key features. Do not mention negative aspects.
    """

    payload = {
        "model": "deepseek-chat", # Check model name
        "messages": [
            {"role": "system", "content": "You are a professional real estate copywriter."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"DeepSeek API Error: {e}")
        return "Error generating description. Please try again later."
