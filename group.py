from linebot.models import TextSendMessage

from tokens import line_bot_api


def group_cmd(event):
    user_msg = event.message.text.lower()  # user's msg
    user_token = event.reply_token  # user's token session
    group = event.source.group_id

    if user_msg == 'bye eina':
        line_bot_api.reply_message(
            user_token, TextSendMessage(text='Thank you'))
        line_bot_api.leave_group(event.source.group_id)

    if user_msg == 'notify_me':  # this will push something to the user , to be continue
        line_bot_api.push_message(
            group, [
                TextSendMessage(text='PUSH!'),
            ]
        )
