class ButtonCore:
    def __init__(self):
        self.events_list = {}

    def add_event(self, target_event, func):
        self.events_list[target_event] = func

    def __call__(self, payload):
        for action in payload['actions']:
            for key, func in self.events_list.items():
                if ButtonCore.lexi_classifier(action, key):
                    func(payload)

    @staticmethod
    def lexi_classifier(action, template):
        """need to be updated"""
        if template in action['text']['text']:
            return  True
        return False

    def __str__(self):
        return str(self.events_list)


def module_check(payload):
    print(payload['actions'][0]['text']['text'])
