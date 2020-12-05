from linebot.models import StickerSendMessage, TextSendMessage
from tokens import line_bot_api

# this where we do our command n shits
def command(event):
    user_msg = event.message.text
    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1', )
    if user_msg == 'p makan':
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text='a'), )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message,
        )
