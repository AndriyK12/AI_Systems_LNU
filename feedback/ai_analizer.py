from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

reviews = ""

with open("feedback\\reviews.txt", 'r') as file:
    reviews = file.read()

completion = client.chat.completions.create(
  model="local-model",
  messages=[
    {"role": "system", "content": "You are a customer feedback analyst in AR glasses selling company. " 
    + "Your task is to analyze a numerated reviews list. You have to use that reviews and add "
    + "your analysis whether this review is good for every review "
    + " and if it is bad suggest how to fix this."
    + "Highlight wether the review is good or not in [] braces before your analysis."},
    {"role": "user", "content": reviews}
  ],
  temperature=0.1,
)

with open("feedback\\reviews_analysis.txt", 'w') as file:
    file.write(completion.choices[0].message.content)

print(completion.choices[0].message.content)