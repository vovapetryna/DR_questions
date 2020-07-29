from messages.hello_message import HelloMsg
from messages.module_message import ModuleMsg
import sys

class EventsCore:
    def __init__(self):
        self.events_list = {}

    def add_event(self, target_event, func):
        self.events_list[target_event] = func

    def __call__(self, payload, web_client):
        if self.events_list.get(payload['type']) is not None:
            try:
                self.events_list[payload['type']](payload, web_client)
            except:
                print(f'Unexpected error {sys.exc_info()[0]}')

    def __str__(self):
        return str(self.events_list)


def add_new_member(payload, web_client):
    user_id = payload['user']
    web_client.chat_postMessage(**HelloMsg(user_id)())
    web_client.chat_postMessage(**ModuleMsg(user_id)())


def bot_tag(payload, web_client):
    print(payload)
