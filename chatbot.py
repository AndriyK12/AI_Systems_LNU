# from openai import OpenAI

# client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# message = input("Please enter your prompt :\n")

# completion = client.chat.completions.create(
#   model="local-model",
#   messages=[
#     {"role": "system", "content": "You are an intelligent assistant in AR glasses selling company chatbot." 
#      + "You always provide well-reasoned answers that are both correct and helpful."+
#       "The product description : " +
#       "AR-Vision Glasses : Introducing our latest innovation, the AR-Vision Glasses! Experience the future in real time with these state-of-the-art smart glasses. With advanced augmented reality technology, you'll see the world around you transformed into an interactive playground. Navigate maps, translate languages, and even play games – all hands-free."+
#       "AR-Life Glasses : Upgrade your daily routine with our AR-Life Glasses. Designed for convenience and style, these sleek glasses blend seamlessly into your life. Stay connected with real-time notifications, make hands-free calls, and enjoy a heads-up display of crucial information – all while keeping your focus on the world around you."+
#       "AR-Explorer Glasses : Dive into a new dimension with our AR-Explorer Glasses! These advanced glasses offer an immersive augmented reality experience that brings adventure to your doorstep. Explore hidden wonders, embark on virtual safaris, and learn new skills – all from the comfort of your own home or office."+
#       "AR-Professional Glasses : Transform your workday with our AR-Professional Glasses. Engineered for productivity and efficiency, these high-performance glasses help you tackle complex projects with ease. Access real-time data, collaborate with colleagues, and streamline your workflow – all while keeping your hands free to get things done."+
#       "AR-Innovation Glasses : Step into a world of limitless possibilities with our AR-Innovator Glasses. These cutting-edge smart glasses are the ultimate tool for creatives, designers, and innovators. Bring your ideas to life with advanced 3D modeling, explore new design concepts, and collaborate with teams in real time – all from the comfort of your own workspace."+
#       "AR-Fit Glasses : Experience the future of fitness with our AR-Fit Glasses! Designed to help you reach your health goals, these smart glasses offer personalized coaching, real-time workout tracking, and even virtual training partners. Stay motivated and engaged as you push yourself to new heights – all while enjoying a more immersive and interactive workout experience."+
#       "AR-Entertainment Glasses : Discover a new level of entertainment with our AR-Entertainment Glasses! These fun and engaging glasses offer an endless array of games, movies, and interactive experiences that will keep you entertained for hours on end. Immerse yourself in stunning 3D graphics, explore new worlds, and even compete against friends – all from the comfort of your own living room."+
#       "AR-News Glasses : Stay informed and connected with our AR-News Glasses! These intelligent glasses provide up-to-the-minute news, weather updates, and social media notifications, so you're always in the know. Customize your feed to suit your interests, and enjoy a more personalized and engaging news experience – all while keeping your hands free to take action."},
#     {"role": "user", "content": message}
#   ],
#   temperature=0.7,
# )


# print(completion.choices[0].message.content)


# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

history = [
    {"role": "system", "content": "You are an intelligent assistant in AR glasses selling company chatbot." 
     + "You always provide well-reasoned answers that are both correct and helpful."+
      "The product description : " +
      "AR-Vision Glasses : Introducing our latest innovation, the AR-Vision Glasses! Experience the future in real time with these state-of-the-art smart glasses. With advanced augmented reality technology, you'll see the world around you transformed into an interactive playground. Navigate maps, translate languages, and even play games – all hands-free."+
      "AR-Life Glasses : Upgrade your daily routine with our AR-Life Glasses. Designed for convenience and style, these sleek glasses blend seamlessly into your life. Stay connected with real-time notifications, make hands-free calls, and enjoy a heads-up display of crucial information – all while keeping your focus on the world around you."+
      "AR-Explorer Glasses : Dive into a new dimension with our AR-Explorer Glasses! These advanced glasses offer an immersive augmented reality experience that brings adventure to your doorstep. Explore hidden wonders, embark on virtual safaris, and learn new skills – all from the comfort of your own home or office."+
      "AR-Professional Glasses : Transform your workday with our AR-Professional Glasses. Engineered for productivity and efficiency, these high-performance glasses help you tackle complex projects with ease. Access real-time data, collaborate with colleagues, and streamline your workflow – all while keeping your hands free to get things done."+
      "AR-Innovation Glasses : Step into a world of limitless possibilities with our AR-Innovator Glasses. These cutting-edge smart glasses are the ultimate tool for creatives, designers, and innovators. Bring your ideas to life with advanced 3D modeling, explore new design concepts, and collaborate with teams in real time – all from the comfort of your own workspace."+
      "AR-Fit Glasses : Experience the future of fitness with our AR-Fit Glasses! Designed to help you reach your health goals, these smart glasses offer personalized coaching, real-time workout tracking, and even virtual training partners. Stay motivated and engaged as you push yourself to new heights – all while enjoying a more immersive and interactive workout experience."+
      "AR-Entertainment Glasses : Discover a new level of entertainment with our AR-Entertainment Glasses! These fun and engaging glasses offer an endless array of games, movies, and interactive experiences that will keep you entertained for hours on end. Immerse yourself in stunning 3D graphics, explore new worlds, and even compete against friends – all from the comfort of your own living room."+
      "AR-News Glasses : Stay informed and connected with our AR-News Glasses! These intelligent glasses provide up-to-the-minute news, weather updates, and social media notifications, so you're always in the know. Customize your feed to suit your interests, and enjoy a more personalized and engaging news experience – all while keeping your hands free to take action."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."}
  ]

while True:
    completion = client.chat.completions.create(
        model="local-model",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    
    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})