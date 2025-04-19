from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hi' in incoming_msg:
        msg.body('Hello! This is Dr. Felix’s bot. How can I help you today?')
    else:
        msg.body('I received your message! I’ll get back to you shortly.')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
