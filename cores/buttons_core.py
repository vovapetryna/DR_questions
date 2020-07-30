import re
from data_base import DataBase
from messages.thx_message import ThxMessage

class ButtonCore:
    def __init__(self):
        self.events_list = {}

    def add_event(self, target_event, func):
        self.events_list[target_event] = func

    def __call__(self, payload, *args, **kwargs):
        for action in payload['actions']:
            for key, func in self.events_list.items():
                if ButtonCore.lexi_classifier(action, key):
                    func(payload, *args, **kwargs)

    @staticmethod
    def lexi_classifier(action, template):
        """need to be updated"""
        if template in action['text']['text']:
            return  True
        return False

    def __str__(self):
        return str(self.events_list)


def module_check(payload, web_client):
    module_number = int(re.findall(r'\d+', payload['actions'][0]['text']['text'])[-1])

    """add to payload -> to form dict -> to pass it to the DataBase method (with user data)"""
    sql_data = {'user': payload['user']['id'],
                'module': module_number}

    data_base = DataBase()
    data_base.update_module(**sql_data)
    data_base.end_work()

    web_client.chat_postMessage(**ThxMessage(payload['user']['id'])('modules', module_number))
    """response to the user with correct module selected"""
