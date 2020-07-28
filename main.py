import os
import logging
from flask import Flask
from slack import WebClient
from message import OnboardingTutorial
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter('97dc871214d1284acda832372929a19a', "/slack/events", app)
slack_web_client = WebClient(token='xoxb-1262742172500-1260429747301-YDLTuN5pUueGYCWYBoQNnTTQ')

@app.route('/')
def index():
    return 'run from git)'

@app.route('/inc/<id>/')
def get_id(id):
    return f'requested page with id = {id} returned id = {int(id) + 1}'

@app.route('/sendmsg/<text>')
def send_msg(text):
    onboarding_tutorial = OnboardingTutorial('C017BQA2RM4')
    message = onboarding_tutorial.get_message_payload()
    slack_web_client.chat_postMessage(**message)
    return f'message with text = {text} sent!!!'

@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
  emoji = event_data["event"]["reaction"]
  onboarding_tutorial = OnboardingTutorial('C017BQA2RM4')
  message = onboarding_tutorial.get_message_payload()
  slack_web_client.chat_postMessage(**message)
  print(emoji)


if __name__ == '__main__':
    app.run(debug=True, port=3000)