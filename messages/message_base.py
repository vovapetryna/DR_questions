import config as cfg


class MessageBase:
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = cfg.bot_info['name']
        self.icon_emoji = cfg.bot_info['icon_emoji']
        self.timestamp = ""

    def text(self, text):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.make_section_block(text),
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
