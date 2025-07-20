from flask import Flask
from twilio_handler import handle_call

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>waste time bot</h1>
    <p>bot is running and ready to waste scammer time 🤖👴</p>
    <p>endpoints:</p>
    <ul>
        <li><code>POST /voice</code> - twilio webhook for incoming calls</li>
    </ul>
    '''

@app.route('/voice', methods=['POST'])
def voice():
    return handle_call()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
