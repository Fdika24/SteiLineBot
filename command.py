from linebot.models import StickerSendMessage, TextSendMessage, SourceGroup, SourceRoom
from linebot.models import FlexSendMessage, ImageSendMessage
from tokens import line_bot_api

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
    f = open('flex.json', )
    data = json.load(f)
    # batas suci
    if profile.display_name.lower() == 'farhandika':
        if user_msg == 'einainfo':
            flex_message = FlexSendMessage(alt_text="hello", contents=data)
            line_bot_api.reply_message(
                user_token,
                [
                    flex_message,
                    TextSendMessage(
                        text='Malem All :)\n Aku mau ngomong nih. '
                             'Aku mau nyampein nih kalau besok ada forum angkatan. Forum ini bakal diadain jam 19.00 WIB '
                             'hari selasa.\nJadi, jangan pada telat ya!! '
                    ),
                    sticker_message,
                ]
            )

    if user_msg == 'myprofile':
        line_bot_api.reply_message(
            user_token,
            [
                TextSendMessage(text="@{}".format(profile.display_name)),
                TextSendMessage(text="Status : {}".format(profile.status_message)),
                sticker_message,
            ],
        )

    if user_msg == 'flexmsg':
        flex_message = FlexSendMessage(alt_text="hello", contents=data)
        line_bot_api.reply_message(
            user_token,
            [
                sticker_message,
                flex_message,
            ]
        )

    if user_msg == 'notify_me':  # this will push something to the user , to be continue
        line_bot_api.push_message(
            event.source.user_id, [
                TextSendMessage(text='PUSH!'),
            ]
        )
    if user_msg.startswith('send_all '):  # Boradcast to all who added eina chan
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

    if user_msg == 'bye bot':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Thank you'))
            line_bot_api.leave_group(event.source.group_id)
        if isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Thank you'))
            line_bot_api.leave_group(event.source.room_id)
