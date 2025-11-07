"""
Example: Direct API usage with Lorica.ai OHTTP

This example demonstrates how to use the lorica ohttp library directly
to make encrypted API calls to Lorica.ai's confidential inference endpoint.

Note: Replace the API key and deployment URL with your own credentials.
"""

from lorica import ohttp
import json

# Create a session object for persistent connections
ohttp_session = ohttp.Session()

# Placeholder for API key and deployment URL
lorica_api_key = "w98Ahk2n.KvOwfLuFYodGkmsZJ5PoKy7tCm8Rqp7S"
deployment_url = "https://e4d9a526.dep.lorica.ai"

# Make a POST request to the chat completions endpoint with streaming enabled
stream = True
resp = ohttp_session.post(
    f"{deployment_url}/v1/chat/completions",
    headers={"Authorization": f"Bearer {lorica_api_key}"},
    json={
        "model": "cortecs/Llama-3.3-70B-Instruct-FP8-Dynamic",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "How many rs in strawberry?"},
        ],
        "temperature": 0.7,
        "max_tokens": 1024,
        "stream": stream,  # Enable streaming for LLMs
    },
    stream=stream  # Handle the response as a stream
)

resp.raise_for_status()

# Process the streaming response incrementally
if stream:
    for line in resp.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data: "):
            continue

        data = line[len("data: "):].strip()
        if data == "[DONE]":
            break

        try:
            chunk = json.loads(data)
        except json.JSONDecodeError:
            continue

        choices = chunk.get("choices") or []
        if choices:
            delta = choices[0].get("delta") or {}
            content = delta.get("content")
            if content:
                print(content, end="", flush=True)
else:
    print(resp.json()["choices"][0]["message"]["content"])

