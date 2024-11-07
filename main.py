from agents.research_agent import ResearchAgent
from agents.use_case_agent import UseCaseAgent
from agents.resource_agent import ResourceAgent
import yaml

def generate_insights(industry_name):
    config_path = "configs/config.yaml"
    research_agent = ResearchAgent(config_path)
    use_case_agent = UseCaseAgent(config_path)
    resource_agent = ResourceAgent()

    industry_info = research_agent.research_industry(industry_name)
    if not industry_info:
        return None

    use_cases = use_case_agent.generate_use_cases(industry_info)
    if not use_cases:
        return None

    markdown_content = f"# Insights for {industry_name}\n\n"
    for i, case in enumerate(use_cases, start=1):
        markdown_content += f"## Use Case {i}: {case}\n"
        dataset_links = resource_agent.find_datasets(case)
        for link in dataset_links:
            markdown_content += f"- [{link.split(': ')[1]}]({link.split(': ')[1]})\n"
        markdown_content += "\n"
    
    with open("outputs/insights.md", "w") as file:
        file.write(markdown_content)

    return markdown_content
