import config as cfg

if cfg.lang == 'en':
    import localization.en as msg_cfg
else:
    import localization.ru as msg_cfg

from messages.message_base import MessageBase


class ThxMessage(MessageBase):
    """Constructs the Thx messages with custom cores"""

    def __init__(self, channel):
        MessageBase.__init__(self, channel)

    def __call__(self, purpose='modules', *args, **kwargs):
        print(args)
        """puprpose values = ['modules', ]"""
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.make_section_block(msg_cfg.thx_message[purpose].format(*args),)
            ],
        }



