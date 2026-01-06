import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load .env safely
load_dotenv()



client = AzureOpenAI(
    azure_endpoint="https://foundryagentreminder.cognitiveservices.azure.com/",
    api_key="EXJ95r7DrnsQ9fqTXSBl7btGMLNSzAfGjQOBRezwR8jLDYR0tqgBJQQJ99CAACHYHv6XJ3w3AAAAACOGVn2n",
    api_version= "2024-12-01-preview"
)

def chat(question: str, context: str = "") -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{context}\n\nQuestion: {question}"}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content
