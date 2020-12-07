from linebot.models import StickerSendMessage, TextSendMessage, SourceGroup, SourceRoom
from tokens import line_bot_api

from einainfo import einainfo

import json


# this where we do our command n shits
def command(event):
    user_msg = event.message.text.lower()  # user's msg
    user_token = event.reply_token  # user's token session
    profile = line_bot_api.get_profile(event.source.user_id)  # get user's id
    sticker_message = StickerSendMessage(  # this is sticker
        package_id='1',
        sticker_id='7', )
    # do not bother to edit anything here
    # batas suci
    if user_msg == 'einainfo': einainfo(user_token)

    if user_msg == 'myprofile':
        line_bot_api.reply_message(
            user_token,
            [
                TextSendMessage(text="@{}".format(profile.display_name)),
                TextSendMessage(text="Status : {}".format(profile.status_message)),
                TextSendMessage(text = "User ID : {}".format(profile.user_id)),
                sticker_message,
            ],
        )

    if user_msg == 'notify_me':  # this will push something to the user , to be continue
        line_bot_api.push_message(
            event.source.user_id, [
                TextSendMessage(text='PUSH!'),
            ]
        )
    if user_msg.startswith('send_all '):  # Brodcast to all who added eina chan
        line_bot_api.broadcast(
            [
                TextSendMessage(text=' '.join(user_msg.split(' ')[1:])),
            ]
        )
    if user_msg.startswith('broadcast '):  # broadcast 20190505 , tbh idk what this does till now
        date = user_msg.split(' ')[1]
        print("Getting broadcast result: " + date)
        result = line_bot_api.get_message_delivery_broadcast(date)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='Number of sent broadcast messages: ' + date),
                TextSendMessage(text='status: ' + str(result.status)),
                TextSendMessage(text='success: ' + str(result.success)),
            ]
        )
