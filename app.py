from flask import Flask, request, abort

from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage

from tokens import line_bot_api, handler  # token

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


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
    user_msg = event.message.text
    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1', )

    if user_msg == 'a':
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text='a'),)
    else:
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message,
        )


if __name__ == '__main__':
    app.run()
