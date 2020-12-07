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

    if user_msg == 'maap typo':
        line_bot_api.push_message(
            'Ude2d6760c5eba4781184c4c8d2a0b94c',
            TextSendMessage(text=f'Group id : {group}')
        )

    if user_msg.startswith('push '):
        data = user_msg.split(' ')[1:]  # this will push something to the group, under consturction
        # group = data[0]
        line_bot_api.push_message(
            'C1528a299c9ba3a5b556fd2148da8b53d', [
                TextSendMessage(text=' '.join(data)),
            ]
        )
