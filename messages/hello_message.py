import config as cfg

if cfg.lang == 'en':
    import localization.en as msg_cfg
else:
    import localization.ru as msg_cfg


class HelloMsg:
    """Constructs the hello message with respect to
    a config"""

    def __init__(self, channel):
        self.channel = channel
        self.username = cfg.bot_info['name']
        self.icon_emoji = cfg.bot_info['icon_emoji']
        self.timestamp = ""

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                make_section_block(msg_cfg.hello_message['hello'])
            ],
        }

    def get_simple_message_payload(self, text):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                make_section_block(text)
            ],
        }


@staticmethod
def make_section_block(text):
    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text,
        },
    }


@staticmethod
def make_divider_block():
    return {"type": "divider"}
