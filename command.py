from linebot.models import StickerSendMessage, TextSendMessage, SourceGroup, SourceRoom

from tokens import line_bot_api


# this where we do our command n shits
def command(event):
    user_msg = event.message.text  # user's msg
    user_token = event.reply_token  # user's token session
    profile = line_bot_api.get_profile(event.source.user_id)  # get user's id
    sticker_message = StickerSendMessage(  # this is sticker
        package_id='1',
        sticker_id='1', )

    if user_msg == 'p makan':
        line_bot_api.reply_message(user_token,
                                   TextSendMessage(text='a'), )
    if user_msg == 'myprofile':
        line_bot_api.reply_message(
            user_token,
            [
                TextSendMessage(text="@{}".format(profile.display_name)),
                TextSendMessage(text="Status : {}".format(profile.status_message)),
                sticker_message,
            ],
        )

    if user_msg == 'push':
        line_bot_api.push_message(
            event.source.user_id, [
                TextSendMessage(text='PUSH!'),
            ]
        )
    if user_msg == 'multicast':
        line_bot_api.multicast(
            [event.source.user_id], [
                TextSendMessage(text='THIS IS A MULTICAST MESSAGE'),
            ]
        )
    if user_msg == 'broadcast':
        line_bot_api.broadcast(
            [
                TextSendMessage(text='THIS IS A BROADCAST MESSAGE'),
            ]
        )
    if user_msg.startswith('broadcast '):  # broadcast 20190505
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


