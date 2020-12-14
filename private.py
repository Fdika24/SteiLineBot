from linebot.models import StickerSendMessage, TextSendMessage, FlexSendMessage, \
    SeparatorComponent, ButtonComponent, URIAction, BoxComponent, TextComponent, ImageComponent, BubbleContainer
from tokens import line_bot_api

from einainfo import einainfo

import requests


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
        title = new_resp['titles']['en_jp']
        # print(new_resp)
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url=str(new_resp['posterImage']['original']),
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://kitsu.io/anime/{}'.format('-'.join(title.split()))
                                 , label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=title,
                                  weight='bold',
                                  size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            TextComponent(text='{}/100'.format(new_resp['averageRating'])
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
                                        text='About',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text=new_resp['synopsis'],
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
                                        text='Status',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text=new_resp['status'],
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
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='WEBSITE', uri='https://kitsu.io/anime/{}'.format('-'.join(title.split())))
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text=title, contents=bubble)
        line_bot_api.reply_message(
            user_token,
            message
        )
    elif user_msg == 'info_eina':
        line_bot_api.reply_message(
            user_token,[
                TextSendMessage(
                text='Eina sih simpel aja, Eina adalah bot pencari anime, untuk mencari sipnosis, rating, '
                         'maupun banyak episode cukup dengan mengetik anime judul \n '
                         'contohnya : anime naruto\n Jangan lupa ya, untuk commandnya huruf kecil semua'),
                sticker_message,
            ]
              )
    else: line_bot_api.reply_message(
        user_token,
        TextSendMessage(text='Maaf banget, eina kyknya belum bisa mengerti nih maunya kamu apa *cry. Mungkin kamu '
                             'boleh nih liat lagi peraturan eina dengan cara ketik info_eina')
    )



