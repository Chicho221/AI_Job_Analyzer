from openai import OpenAI
from openai import RateLimitError
from configPRIV import API_KEY

client = OpenAI(api_key = API_KEY)

def analyze_jobAI(job):
    # Fake AI Function Result 
    # return f"""
    # Summary: This is a {job['title']} role at {job['company']}.
    # Skills: Skills
    # Level: Junior/Mid/Senior"""

    # OpenAI Logic
    # Start of prompt ===
    prompt = f""" 
    Analyze this job:

    Title: {job['title']}
    Company: {job['company']}

    Respond in format:
    Summary:
    Skills:
    Level:
    """
    # End of prompt ===
    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
        )
        return response.choices[0].message.content
    except RateLimitError:
        print("Rate limit exceeded!")
        return
