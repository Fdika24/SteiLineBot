from linebot.models import StickerSendMessage, TextSendMessage
from tokens import line_bot_api

# this where we do our command n shits
def command(event):
    user_msg = event.message.text # user's input message
    user_token = event.reply_token # user's session token
    profile = line_bot_api.get_profile(event.user_id) # get user's profile
    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1', )
    if user_msg == 'p makan':
        line_bot_api.reply_message(user_token,
                                   TextSendMessage(text='a'), )
    if user_msg == 'myusername':
        line_bot_api.reply_message(
            user_token,
            TextSendMessage(text="{}".format(profile.display_name) # benernya ga harus gini si, cuma ya gitu, biar estetis aja
        )
