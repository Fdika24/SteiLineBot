from linebot.models import TextSendMessage

from einainfo import einainfo
from tokens import line_bot_api


def group_cmd(event):
    user_msg = event.message.text.lower()  # user's msg
    user_token = event.reply_token  # user's token session
    group = event.source.group_id # group id

    if user_msg == 'einainfo': einainfo(user_token)

    if user_msg == 'bye eina':
        line_bot_api.reply_message(
            user_token, TextSendMessage(text='Thank you'))
        line_bot_api.leave_group(event.source.group_id)
