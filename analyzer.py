from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key = API_KEY)

def analyze_job(job):
    prompt = f""" 
    Analyze this job:

    Title: {job['title']}
    Company: {job['company']}

    Give:
    - Short summary
    - Required skills
    - Level (junior/mid/senior)
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content