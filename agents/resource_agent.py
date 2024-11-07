import requests

class ResourceAgent:
    def find_datasets(self, use_case):
        search_keywords = "+".join(use_case.split())
        datasets = []
        kaggle_url = f"https://www.kaggle.com/search?q={search_keywords}"
        huggingface_url = f"https://huggingface.co/search?q={search_keywords}"
        datasets.append(f"Kaggle: {kaggle_url}")
        datasets.append(f"HuggingFace: {huggingface_url}")
        return datasets
