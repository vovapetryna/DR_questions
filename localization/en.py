"""common words"""

chat_name = 'dru-печеньки'

"""common phrases"""

hello_message = {
                'hello': f"Welcome to *{chat_name}*! :wave: We're so glad you're here. :blush:",
            }

module_message = {
                'button': "Module#{}",
                'select': "Select your current module.",
            }

thx_message = {
                'modules': "Thanks for your answer (module#{})! :thumbsup: \n\n"
                           " Your friends can now help you, and you can help them",
            }

thread_message = {
                'add_lead': 'You <@{}> have already completed this module, please help your friends :pray:',
                'answer_rule': 'After answering, react to it with :heavy_check_mark: \n'
                               ' In this case, you will receive *rating points*.',
            }

alert_message = {
                'rating_cheat': 'Other users should rate your answer, not you :exclamation:',
                'answer_success': 'Your answer helped someone and' \
                                  ' for this you get additional rating points! :thumbsup:',
            }
