import json

from linebot.models import TextSendMessage, FlexSendMessage, StickerSendMessage
from tokens import line_bot_api as api


def einainfo(user_token):
    f = open('flex.json', )
    data = json.load(f)
    flex_message = FlexSendMessage(alt_text="hello", contents=data)
    api.reply_message(
        user_token,
        [
            flex_message,
            TextSendMessage(
                text='Malem All :)\n Aku mau ngomong nih.'
                     'Aku mau nyampein kalau besok ada forum angkatan. Forum ini bakal diadain jam 19.00 WIB '
                     'hari selasa.\nJadi, jangan pada telat ya!! '
            ),
            StickerSendMessage(  # this is sticker
                package_id='1',
                sticker_id='7', )
        ]
    )
