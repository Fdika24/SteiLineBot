from linebot.models import StickerSendMessage, TextSendMessage, SourceGroup, SourceRoom, FlexSendMessage, \
    SeparatorComponent, ButtonComponent, URIAction, BoxComponent, TextComponent, ImageComponent, BubbleContainer
from tokens import line_bot_api

from einainfo import einainfo

import json,requests


# this where we do our command n shits
def command(event):
    response = requests.get('https://kitsu.io/api/edge/anime?filter[text]=$kimetsu')
    user_msg = event.message.text  # user's msg
    user_token = event.reply_token  # user's token session
    profile = line_bot_api.get_profile(event.source.user_id)  # get user's id
    sticker_message = StickerSendMessage(  # this is sticker
        package_id='1',
        sticker_id='7', )
    # do not bother to edit anything here
    # batas suci
    if user_msg == 'flex':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://media.kitsu.io/anime/poster_images/1/original.jpg?1597604210',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Brown Cafe', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            TextComponent(text='4.0', size='sm', color='#999999')
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
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Another day, another bounty—such is the life of the often unlucky crew '
                                             'of the Bebop. However, this routine is interrupted when Faye, '
                                             'who is chasing a fairly worthless target on Mars, witnesses an oil '
                                             'tanker suddenly explode, causing mass hysteria. As casualties mount due '
                                             'to a strange disease spreading through the smoke from the blast, '
                                             'a whopping three hundred million woolong price is placed on the head of '
                                             'the supposed perpetrator.\nWith lives at stake and a solution to their '
                                             'money problems in sight, the Bebop crew springs into action. Spike, '
                                             'Jet, Faye, and Edward, followed closely by Ein, split up to pursue '
                                             'different leads across Alba City. Through their individual '
                                             'investigations, they discover a cover-up scheme involving a '
                                             'pharmaceutical company, revealing a plot that reaches much further than '
                                             'the ragtag team of bounty hunters could have realized.\n[Written by MAL '
                                             'Rewrite]","description":"Another day, another bounty—such is the life '
                                             'of the often unlucky crew of the Bebop. However, this routine is '
                                             'interrupted when Faye, who is chasing a fairly worthless target on '
                                             'Mars, witnesses an oil tanker suddenly explode, causing mass hysteria. '
                                             'As casualties mount due to a strange disease spreading through the '
                                             'smoke from the blast, a whopping three hundred million woolong price is '
                                             'placed on the head of the supposed perpetrator.\nWith lives at stake '
                                             'and a solution to their money problems in sight, the Bebop crew springs '
                                             'into action. Spike, Jet, Faye, and Edward, followed closely by Ein, '
                                             'split up to pursue different leads across Alba City. Through their '
                                             'individual investigations, they discover a cover-up scheme involving a '
                                             'pharmaceutical company, revealing a plot that reaches much further than '
                                             'the ragtag team of bounty hunters could have realized.\n[Written by MAL '
                                             'Rewrite]',
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
                                        text='Time',
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

