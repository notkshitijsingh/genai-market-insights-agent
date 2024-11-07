import http.client
import json
import yaml

class ResearchAgent:
    def __init__(self, config_path="../configs/config.yaml"):
        with open(config_path) as f:
            config = yaml.safe_load(f)
            self.api_key = config['api_keys']['search_engine_key']

    def research_industry(self, industry_name):
        try:
            conn = http.client.HTTPSConnection("google.serper.dev")
            payload = json.dumps({"q": industry_name})
            headers = {
                'X-API-KEY': self.api_key,
                'Content-Type': 'application/json'
            }
            conn.request("POST", "/search", payload, headers)
            res = conn.getresponse()
            data = res.read()
            response_json = json.loads(data.decode("utf-8"))
            conn.close()
            
            industry_summary = {
                "knowledgeGraph": response_json.get("knowledgeGraph", {}),
                "organic_results": [
                    {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
                    for item in response_json.get("organic", [])
                ],
                "top_stories": [
                    {"title": story["title"], "link": story["link"], "source": story["source"]}
                    for story in response_json.get("topStories", [])
                ]
            }
            return industry_summary
        
        except Exception as e:
            print("Error fetching data:", e)
            return {}
