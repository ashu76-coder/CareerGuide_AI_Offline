from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    user_input = request.form['user_input'].lower()

    responses = {
        "data science": [
            "Start with Python and libraries like Pandas, NumPy, and Matplotlib.",
            "Learn statistics, machine learning basics, and data visualization tools.",
            "Build projects using real datasets — like predicting trends or customer analysis."
        ],
        "web development": [
            "Start learning HTML, CSS, and JavaScript.",
            "Then move to frameworks like React (frontend) and Django or Flask (backend).",
            "Create portfolio websites and deploy them on GitHub Pages or Render."
        ],
        "ai": [
            "Learn Python and ML libraries like Scikit-learn, TensorFlow, or PyTorch.",
            "Understand neural networks and natural language processing (NLP).",
            "Build a chatbot or recommendation system for your portfolio."
        ],
        "default": [
            "Explore your interests first — start with basic computer skills and online courses.",
            "Try building small projects to understand what field excites you the most."
        ]
    }

    # Select matching response
    for key in responses:
        if key in user_input:
            advice = random.choice(responses[key])
            break
    else:
        advice = random.choice(responses["default"])

    return advice

if __name__ == '__main__':
    app.run(debug=True)
