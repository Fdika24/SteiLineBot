from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('6zD7qNcZHoTJKL//r0odUpgEQCZghzMEtrxLyDliXevFF0K7bcf2HYzplYH1jmre7wqWYu/kaCgQ8QGQ7Da/FLmvPHSbiDefh0DUCF8WZCNxxuuWBrzG4WCLazxIbok+oZf0GuUNQxGEpNPnwl2J6QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f35b52879515aa305b5f87011a00518d')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='a')
    )


if __name__ == '__main__':
    app.run()
