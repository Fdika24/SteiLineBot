from linebot.models import StickerSendMessage, TextSendMessage, SourceGroup, SourceRoom, FlexSendMessage
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
    if user_msg.startswith('push '):
        '''
        Cara pemakaian :
        push {nomor pack} {nomor sticker} {json file} {pesan}
        ex :push 1 1 hearing.json maap yah
        '''
        data = user_msg.split(' ')[1:]  # this will push something to the group, under consturction
        # group = data[0]
        line_bot_api.push_message(
            'C1528a299c9ba3a5b556fd2148da8b53d', [
                FlexSendMessage(alt_text="hello", contents=json.load(open('flex.json', ))),
                TextSendMessage(text=' '.join(data[2:])),
                StickerSendMessage(
                    package_id=data[0],
                    sticker_id= data[1],
                )
            ]
        )
    if user_msg.startswith('send_all '):  # Brodcast to all who added eina chan
        line_bot_api.broadcast(
            [
                # FlexSendMessage(alt_text="hello", contents=json.load(open('flex.json', ))),
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
