from flask import Flask, request, jsonify, send_from_directory
from chatbot.jpy_v_02_01 import OpenRouterChatBot

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

chatbot = OpenRouterChatBot()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        response = chatbot.get_response(user_input)
        return jsonify({'response': response})
    return jsonify({'error': 'No message provided'}), 400

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

    