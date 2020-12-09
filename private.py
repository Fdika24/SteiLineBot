from linebot.models import StickerSendMessage, TextSendMessage, SourceGroup, SourceRoom, FlexSendMessage, \
    SeparatorComponent, ButtonComponent, URIAction, BoxComponent, TextComponent, ImageComponent, BubbleContainer
from tokens import line_bot_api

from einainfo import einainfo

import json,requests


# this where we do our command n shits
def command(event):
    user_msg = event.message.text  # user's msg
    user_token = event.reply_token  # user's token session
    profile = line_bot_api.get_profile(event.source.user_id)  # get user's id
    sticker_message = StickerSendMessage(  # this is sticker
        package_id='1',
        sticker_id='7', )
    # do not bother to edit anything here
    # batas suci
    if user_msg.startswith('anime '):  # cara pakai anime {nama anime}
        response = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={user_msg.split()[1:]}')
        print(response.status_code)
        new_resp = response.json()['data'][0]['attributes']
        # print(new_resp)
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url=str(new_resp['posterImage']['original']),
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=new_resp['titles']['en_jp'],
                                  weight='bold',
                                  size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            TextComponent(text=new_resp['averageRating']
                                          , size='sm'
                                          , color='#999999')
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Synopsis',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='new_resp[]',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Total Episodes',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='CALL', uri='tel:000000'),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='WEBSITE', uri="https://example.com")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            user_token,
            message
        )

