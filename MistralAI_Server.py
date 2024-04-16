from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

message = input("Please enter your prompt :\n")

completion = client.chat.completions.create(
  model="local-model",
  messages=[
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": message}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)