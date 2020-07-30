from messages.hello_message import HelloMsg
from messages.module_message import ModuleMsg
from messages.alert_message import AlertMessage
import config as cfg
import sys
from data_base import DataBase


class EventsCore:
    def __init__(self):
        self.events_list = {}

    def add_event(self, target_event, func):
        self.events_list[target_event] = func

    def __call__(self, payload, *args, **kwargs):
        if self.events_list.get(payload['type']) is not None:
            # try:
            #     self.events_list[payload['type']](payload, *args, **kwargs)
            # except:
            #     print(f'Unexpected error {sys.exc_info()[0]}')

            self.events_list[payload['type']](payload, *args, **kwargs)

    def __str__(self):
        return str(self.events_list)


def add_new_member(payload, web_client, *args, **kwargs):
    user_id = payload['user']
    if user_id != cfg.bot_info['user_id']:
        """case when new member was added"""
        web_client.chat_postMessage(**HelloMsg(user_id)())
        web_client.chat_postMessage(**ModuleMsg(user_id)())

        data_base = DataBase()
        data_base.add_user(**payload)
        data_base.end_work()
    else:
        """case when bot was added [need to specify correct bot_user_id if config.py]"""
        answer = web_client.conversations_members(channel=payload['channel'])
        print(f'join action return data: {answer}')

        if answer.get('members') is not None:
            data_base = DataBase()
            for member in answer['members']:
                if member != cfg.bot_info['user_id']:
                    web_client.chat_postMessage(**HelloMsg(member)())
                    web_client.chat_postMessage(**ModuleMsg(member)())

                    data_base.add_user(user=member)

            data_base.end_work()


def bot_tag(payload, web_client, *args, **kwargs):
    """get author user id [user if new thread or parent_user_id if old thread]"""
    author_user_id = payload.get('user', '') if payload.get('parent_user_id') is None \
                                             else payload.get('parent_user_id')

    """get randomly chosen user for answering with module > author_user_id.module"""
    data_base = DataBase()
    lead_user = data_base.get_lead_user(user=author_user_id)
    data_base.end_work()

    reply_data = {'thread_ts': payload.get('ts', '') if payload.get('thread_ts') is None
                                                     else payload.get('thread_ts'),
                  'lead_user': lead_user if lead_user is not None else '',
                  }

    web_client.chat_postMessage(**(HelloMsg(payload.get('channel', '')).please_message(**reply_data)))


def task_done(payload, web_client, *args, **kwargs):
    lead_user = payload.get('item_user')

    check_user = payload.get('user')

    if check_user != lead_user:
        data_base = DataBase()
        data_base.update_points(user=lead_user)
        data_base.end_work()

        web_client.chat_postMessage(**AlertMessage(lead_user).success_message())
    else:
        web_client.chat_postMessage(**AlertMessage(check_user)())
