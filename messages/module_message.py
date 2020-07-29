import config as cfg

if cfg.lang == 'en':
    import localization.en as msg_cfg
else:
    import localization.ru as msg_cfg

from messages.message_base import MessageBase


class ModuleMsg(MessageBase):
    """Constructs the module asking message with Buttons
     based on MessageBase class"""

    def __init__(self, channel):
        MessageBase.__init__(self, channel)

    def __call__(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.make_section_block(msg_cfg.module_message['select']),
                self.get_buttons(),
            ],
        }

    @staticmethod
    def get_buttons():
        def button(text):
            return {
                "type": 'button',
                "text": {
                    "type": "plain_text",
                    "text": text,
                    "emoji": False,
                }
            }
        return {
            "type": 'actions',
            "elements": [button(msg_cfg.module_message['button'].format(i))
                         for i in range(1, cfg.module_number+1)],
        }

