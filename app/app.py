from flask import Flask, request, jsonify
from dal import add_question_answer
from openai_integration import get_openai_answer
from models import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
#with app.app_context():
#    db.create_all() 
    
# Route to accept a question and return an answer
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()  # Get JSON data from the request
    question = data.get('question')  # Extract the 'question' field
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # Get the answer from OpenAI API
    answer = get_openai_answer(question)
    
    # Save question and answer to the database
    add_question_answer(question, answer)
    
    # Return the question and answer as a JSON response
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
