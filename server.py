from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

is_first_run = True

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')

    completion = client.chat.completions.create(
        model="local-model",
        messages=[
            {"role": "system", "content": "You are an intelligent assistant in AR glasses selling company chatbot." 
            + "You always provide well-reasoned answers that are both correct and helpful."+
            "If the question has nothing to do with AR-glasses excuse yourself and tell that you can not help with this" +
            "The product description : " +
            "AR-Vision Glasses : Introducing our latest innovation, the AR-Vision Glasses! Experience the future in real time with these state-of-the-art smart glasses. With advanced augmented reality technology, you'll see the world around you transformed into an interactive playground. Navigate maps, translate languages, and even play games – all hands-free."+
            "AR-Life Glasses : Upgrade your daily routine with our AR-Life Glasses. Designed for convenience and style, these sleek glasses blend seamlessly into your life. Stay connected with real-time notifications, make hands-free calls, and enjoy a heads-up display of crucial information – all while keeping your focus on the world around you."+
            "AR-Explorer Glasses : Dive into a new dimension with our AR-Explorer Glasses! These advanced glasses offer an immersive augmented reality experience that brings adventure to your doorstep. Explore hidden wonders, embark on virtual safaris, and learn new skills – all from the comfort of your own home or office."+
            "AR-Professional Glasses : Transform your workday with our AR-Professional Glasses. Engineered for productivity and efficiency, these high-performance glasses help you tackle complex projects with ease. Access real-time data, collaborate with colleagues, and streamline your workflow – all while keeping your hands free to get things done."+
            "AR-Innovation Glasses : Step into a world of limitless possibilities with our AR-Innovator Glasses. These cutting-edge smart glasses are the ultimate tool for creatives, designers, and innovators. Bring your ideas to life with advanced 3D modeling, explore new design concepts, and collaborate with teams in real time – all from the comfort of your own workspace."+
            "AR-Fit Glasses : Experience the future of fitness with our AR-Fit Glasses! Designed to help you reach your health goals, these smart glasses offer personalized coaching, real-time workout tracking, and even virtual training partners. Stay motivated and engaged as you push yourself to new heights – all while enjoying a more immersive and interactive workout experience."+
            "AR-Entertainment Glasses : Discover a new level of entertainment with our AR-Entertainment Glasses! These fun and engaging glasses offer an endless array of games, movies, and interactive experiences that will keep you entertained for hours on end. Immerse yourself in stunning 3D graphics, explore new worlds, and even compete against friends – all from the comfort of your own living room."+
            "AR-News Glasses : Stay informed and connected with our AR-News Glasses! These intelligent glasses provide up-to-the-minute news, weather updates, and social media notifications, so you're always in the know. Customize your feed to suit your interests, and enjoy a more personalized and engaging news experience – all while keeping your hands free to take action."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    bot_response = completion.choices[0].message.content
    return jsonify({'response': bot_response})

@app.route('/feedback', methods=['POST'])
def save_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']

    feedback_message = f"\nName: {name}; Email: {email}; Feedback: {feedback}"

    with open('feedback/reviews.txt', 'a') as f:
        f.write(feedback_message)

    response = jsonify({'message': 'Feedback received and saved successfully!'})

    return response, 200

@app.route('/addInterest', methods=['POST'])
def addInterest():
    global is_first_run
    if is_first_run:
        clear_user_interests()
        is_first_run = False

    user_interest = request.json.get('message')
    append_to_user_interests(user_interest)

    return jsonify({'message': f'"{user_interest}" успішно додано.'})

@app.route('/generateRecommendation', methods=['GET'])
def generateRecommendation():
    with open("Recommendation System\\description.txt", 'r') as file:
        partnerProductDescription = file.read()
    with open("Recommendation System\\usersInterests.txt", 'r') as file:
        listOfUsersInterests = file.read()

    completion = client.chat.completions.create(
        model="local-model",
        messages=[
            {"role": "system", "content": "You are an intelligent assistant in AR glasses selling company."
                                          + "You always provide well-reasoned answers that are both correct and helpful."
                                          + "Your goal is to recommend a relevant product from our product list or from our partners' product list." +
                                          "This is our product list: " +
                                          "AR-Vision Glasses : Introducing our latest innovation, the AR-Vision Glasses! Experience the future in real time with these state-of-the-art smart glasses. With advanced augmented reality technology, you'll see the world around you transformed into an interactive playground. Navigate maps, translate languages, and even play games – all hands-free." +
                                          "AR-Life Glasses : Upgrade your daily routine with our AR-Life Glasses. Designed for convenience and style, these sleek glasses blend seamlessly into your life. Stay connected with real-time notifications, make hands-free calls, and enjoy a heads-up display of crucial information – all while keeping your focus on the world around you." +
                                          "AR-Explorer Glasses : Dive into a new dimension with our AR-Explorer Glasses! These advanced glasses offer an immersive augmented reality experience that brings adventure to your doorstep. Explore hidden wonders, embark on virtual safaris, and learn new skills – all from the comfort of your own home or office." +
                                          "AR-Professional Glasses : Transform your workday with our AR-Professional Glasses. Engineered for productivity and efficiency, these high-performance glasses help you tackle complex projects with ease. Access real-time data, collaborate with colleagues, and streamline your workflow – all while keeping your hands free to get things done." +
                                          "AR-Innovation Glasses : Step into a world of limitless possibilities with our AR-Innovator Glasses. These cutting-edge smart glasses are the ultimate tool for creatives, designers, and innovators. Bring your ideas to life with advanced 3D modeling, explore new design concepts, and collaborate with teams in real time – all from the comfort of your own workspace." +
                                          "AR-Fit Glasses : Experience the future of fitness with our AR-Fit Glasses! Designed to help you reach your health goals, these smart glasses offer personalized coaching, real-time workout tracking, and even virtual training partners. Stay motivated and engaged as you push yourself to new heights – all while enjoying a more immersive and interactive workout experience." +
                                          "AR-Entertainment Glasses : Discover a new level of entertainment with our AR-Entertainment Glasses! These fun and engaging glasses offer an endless array of games, movies, and interactive experiences that will keep you entertained for hours on end. Immerse yourself in stunning 3D graphics, explore new worlds, and even compete against friends – all from the comfort of your own living room." +
                                          "AR-News Glasses : Stay informed and connected with our AR-News Glasses! These intelligent glasses provide up-to-the-minute news, weather updates, and social media notifications, so you're always in the know. Customize your feed to suit your interests, and enjoy a more personalized and engaging news experience – all while keeping your hands free to take action." +
                                          "There is our partners product list:" +
                                          partnerProductDescription},
            {"role": "user",
             "content": "Give a list of recommended products if the user is interested in " + listOfUsersInterests}
        ],
        temperature=0.1
    )

    return completion.choices[0].message.content

def append_to_user_interests(data):
    try:
        with open("Recommendation System\\usersInterests.txt", 'a') as file:
            file.write(data + ', ')
    except Exception as e:
        print("Error:", str(e))

def clear_user_interests():
    print("works")
    try:
        with open("Recommendation System\\usersInterests.txt", 'w') as file:
            file.write('')
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)  # Запуск сервера на localhost:5000
