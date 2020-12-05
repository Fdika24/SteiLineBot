from linebot.models import StickerSendMessage, TextSendMessage
from tokens import line_bot_api

# this where we do our command n shits
def command(event):
    user_msg = event.message.text
    user_token = event.reply_token
    profile = line_bot_api.get_profile(event.user_id)
    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1', )
    if user_msg == 'p makan':
        line_bot_api.reply_message(user_token,
                                   TextSendMessage(text='a'), )
    else:
        line_bot_api.reply_message(
            user_token,
            sticker_message,
        )
