import requests
import yaml

class UseCaseAgent:
    def __init__(self, config_path="../configs/config.yaml"):
        with open(config_path) as f:
            config = yaml.safe_load(f)
            self.api_key = config['api_keys']['gemini_key']

    def generate_use_cases(self, industry_insights):
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
        
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": (
                                f"Based on the industry insights: {industry_insights}, suggest several innovative AI use cases "
                                "for improving operational efficiency, customer satisfaction, or competitive positioning."
                            )
                        }
                    ]
                }
            ]
        }
        params = {
            "key": self.api_key
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, params=params)
            response.raise_for_status()
            
            response_content = response.json()
            use_cases_text = response_content['candidates'][0]['content']['parts'][0]['text']
            use_cases = use_cases_text.strip().split('\n')
            return [use_case for use_case in use_cases if use_case]
        
        except Exception as e:
            print(f"Error generating use cases: {e}")
            return []
