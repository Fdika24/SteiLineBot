from linebot.models import TextSendMessage

from tokens import line_bot_api


def group_cmd(event):
    user_msg = event.message.text.lower()  # user's msg
    user_token = event.reply_token  # user's token session
    group = event.source.group_id # group id

    if user_msg == 'bye eina':
        line_bot_api.reply_message(
            user_token, TextSendMessage(text='Thank you'))
        line_bot_api.leave_group(event.source.group_id)

    if user_msg == 'getdata':
        line_bot_api.reply_message(
            user_token,
            TextSendMessage(text=f'Group id : {group}')
        )

    if user_msg.startwith('push '):
        data = user_msg.split(' ')[1:]  # this will push something to the user , to be continue
        group = data[0]
        line_bot_api.push_message(
            group, [
                TextSendMessage(text=' '.join(data[1:])),
            ]
        )
