from flask import Flask, request, abort, redirect, json , jsonify

from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage

from tokens import handler  # token
from command import command


app = Flask(__name__)


@app.route('/add', methods=['POST'])


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
    command(event)


if __name__ == '__main__':
    app.run()
