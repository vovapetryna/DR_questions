import os
import logging
from flask import Flask
from slack import WebClient
from messages.hello_message import HelloMsg
from messages.base_message import OnboardingTutorial
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter('97dc871214d1284acda832372929a19a', "/slack/events", app)
slack_web_client = WebClient(token='xoxb-1262742172500-1260429747301-YDLTuN5pUueGYCWYBoQNnTTQ')

@app.route('/')
def index():
    return 'run from git test 2)'

@app.route('/inc/<id>/')
def get_id(id):
    return f'requested page with id = {id} returned id = {int(id) + 1}'

@app.route('/sendmsg/<text>')
def send_msg(text):
    msg = OnboardingTutorial('C017BQA2RM4')
    message = msg.get_message_payload()
    return message
    # slack_web_client.chat_postMessage(**message)
    # return f'message with text = {text} sent!!!'

if __name__ == '__main__':
    app.run(debug=True, port=3000)