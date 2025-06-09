from ollama import Client

client = Client(host='http://localhost:11434')  # Ollama's default

prompt = """
You are an expert in woodworking optimization. Given a list of wood panels and desired cut sizes,
suggest the most space-efficient way to cut them, minimizing waste.

Panels:
- 2440mm x 1220mm x 18mm (x4)

Cuts needed:
- 800mm x 600mm x 18mm (x6)
- 300mm x 300mm x 18mm (x10)

Return a JSON list of each panel with cut coordinates and waste percentage.
"""

response = client.chat(model='deepseek-coder:7b-instruct', messages=[
    {"role": "user", "content": prompt}
])

print(response['message']['content'])