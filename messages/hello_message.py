import config as cfg

if cfg.lang == 'en':
    import localization.en as msg_cfg
else:
    import localization.ru as msg_cfg

from messages.message_base import MessageBase


class HelloMsg(MessageBase):
    """Constructs the hello message with respect to
    a config based on MessageBase class"""

    def __init__(self, channel):
        MessageBase.__init__(self, channel)

    def __call__(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.make_section_block(msg_cfg.hello_message['hello']),
            ],
        }

    def please_message(self, lead_user, thread_ts):
        return {
            'thread_ts': thread_ts,
            'channel': self.channel,
            'username': self.username,
            'icon_emoji': self.icon_emoji,
            'blocks': [
                self.make_section_block(msg_cfg.thread_message['add_lead'].format(lead_user)),
                MessageBase.DIVIDER_BLOCK,
                self.make_section_block(msg_cfg.thread_message['answer_rule']),
            ],
        }
