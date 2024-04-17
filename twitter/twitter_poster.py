import tweepy
from openai import OpenAI

consumer_key = "JW4lv8NbyRSrNov2Pf4CjLgLl"
consumer_secret = "SCaXJJGz0vwAl5bby8nvp7nNyVEuEYgYld3DmhJtdnVYiqzHyI"
access_token = "1780312820518674433-TL0dNvWZH2RX8lJRxsMPkrcgqNwGfA"
access_token_secret = "CTrnEUbopBflE3kp09QjXQyHWogBzk2hpNxxpJqJmG8Xm"
twitter_client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

posts = ""

with open("twitter\\description.txt", 'r') as file:
    posts = file.read()

completion = client.chat.completions.create(
  model="local-model",
  messages=[
    {"role": "system", "content": "You are a twitter admin in AR glasses selling company. "
    + "Your task is to generate a post. You are forbiden to type more than 30 words. You are forbiden to use emojis. "
    + "You are forbiden to use more then 2 hastags. "
    + "You get a description and previous posts. "
    + "You can use previous posts as a source of inspiration. "
    + "You have to write a new post about different type of AR Glasses then the previous post. "
    + "Posts must be interesting and engaging to buy our AR glasses. "},
    {"role": "user", "content": posts}
  ],
  temperature=0.1,
)

newPost = completion.choices[0].message.content
resource = twitter_client.create_tweet(text=newPost)

with open("twitter\\description.txt", 'a') as file:
    file.write("\nPost\n" + newPost + "\n")