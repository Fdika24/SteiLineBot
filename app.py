from flask import Flask, request, abort, redirect, json, jsonify

from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, JoinEvent, TextSendMessage, StickerMessage, SourceGroup, \
    SourceRoom

from tokens import handler, line_bot_api  # token
from private import command
from group import  group_cmd
from room import room_cmd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect("http://farhandika.work/")


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if isinstance(event.source, SourceGroup):
        group_cmd(event)
    elif isinstance(event.source, SourceRoom):
        room_cmd(event)
    else:command(event)


@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Terima kasih udah menerima Eina-chan di group chat anda. \n'),
            TextSendMessage(text='Hallo, perkenalkan namaku Eina-chan, Personal bot kalian.\n'
                                 'Untuk saat ini, belum banyak yang bisa aku lakukan, jadi mohon bantuannya. '),
            StickerMessage(
                package_id=1,
                sticker_id=5,
            )
        ])


if __name__ == '__main__':
    app.run()
