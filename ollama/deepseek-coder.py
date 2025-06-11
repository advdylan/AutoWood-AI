from ollama import Client

client = Client(host='http://localhost:11434')  # Ollama's default

prompt = """
This is my first local prompt. 
Hello World!
"""

response = client.chat(model='deepseek-coder:6.7b-instruct-q4_K_M', messages=[
    {"role": "user", "content": prompt}
])

print(response['message']['content'])