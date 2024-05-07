from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

reviews = ""

with open("pricing\\our_prices.txt", 'r') as file:
    our_prices = file.read()

with open("pricing\\other_companies_prices.txt", 'r') as file:
    other_companies_prices = file.read()

completion = client.chat.completions.create(
  model="local-model",
  messages=[
    {"role": "system", "content": "You are prices analyst in AR glasses selling company. " 
    + "Your task is to analyze a list of our prices and prices of our competitors. You have to try to adjust our prices to be the best "
    + "on the market. You have to return adjusted prices only."
    },
    {"role": "user", "content": "Our pricecs : " + our_prices + " Competitors prices : " + other_companies_prices}
  ],
  temperature=0.1,
)

with open("pricing\\adjusted_prices.txt", 'w') as file:
    file.write(completion.choices[0].message.content)

print(completion.choices[0].message.content)