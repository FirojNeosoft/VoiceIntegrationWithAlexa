"""
VoiceIntegration application
"""
from flask import *
from actions import Action

from flask_ask import Ask, statement

action_obj = Action()

# application
app = Flask('VoiceIntegration')
ask = Ask(app, '/')


# @ask.intent('GreetingIntent')
@app.route("/")
def home():
    speech_text = action_obj.greetings()
    return speech_text
    # return statement(speech_text).simple_card('Home', speech_text)


# @ask.intent('BalanceCheckingIntent')
@app.route("/balance")
def get_balance():
    speech_text = action_obj.get_customer_balance('srujal')
    return jsonify(result=speech_text)
    # return statement(speech_text).simple_card('BalanceChecking', speech_text)


if __name__ == "__main__":
    """
    Main program
    """
    app.run(debug=True)
