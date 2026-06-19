import os
from openai import OpenAI

# Use environment variable for API key - never commit secrets to git
API_KEY = os.getenv("OPENAI_API_KEY", "your_api_key_here")
client = OpenAI(api_key=API_KEY)
Text_to_summarize = input("Enter the text you want to summarize :")
prompt = (f"Please provide a concise, clear summery of the following text in bullet points\n{Text_to_summarize}" )

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= [
        {"role": "user", "content" : prompt}
    ]
)

with open("summary.txt", "w") as file:
    file.write("-----YOUR SUMMARY-----")
    file.write(f"{response.choices[0].message.content}")
print("your summary is successfully created watch it in the summary.txt")