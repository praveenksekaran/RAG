from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(); 

client = OpenAI(    
    api_key="YOUR_OPENAI_PROJECT_API_KEY"
)

vs_id = "YOUR_VS_ID"

def ask(q):
    r = client.responses.create(
        input=q, model="gpt-4o-mini",
        tools=[{"type": "file_search", "vector_store_ids":[vs_id]}]
    )
    return r.output[-1].content[0].text

print(ask("what are the aws experiences of this candidate?"))