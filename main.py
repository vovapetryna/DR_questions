import os
import logging
from flask import Flask, request, make_response
from slack import WebClient
from slack.signature import SignatureVerifier
from cores.buttons_core import ButtonCore, module_check
from cores.events_core import EventsCore, add_new_member, bot_tag, task_done
import config as cfg
import json


app = Flask(__name__)
slack_web_client = WebClient(token=cfg.secure['bot_token'])
signature_verifier = SignatureVerifier(cfg.secure['signing_secret'])
button_core = ButtonCore()
event_core = EventsCore()

"""Add all buttons events"""
button_core.add_event('Module#', module_check)

"""Add all simple events"""
event_core.add_event('member_joined_channel', add_new_member)
event_core.add_event('app_mention', bot_tag)
event_core.add_event('reaction_added', task_done)


"""main event processing part"""


@app.route("/slack/events", methods=["POST"])
def slack_app():
    """process all eventsAPI with buttons event and other simple events"""
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)

    if "payload" in request.form:
        payload = json.loads(request.form.get('payload', {}))
        if payload.get('type', '') == 'block_actions':
            button_core(payload, slack_web_client)

        return make_response("", 200)

    elif "event" in request.get_json():
        event_core(request.get_json().get('event', {}), slack_web_client)
        return make_response("", 200)

    return make_response("", 404)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
